#!/usr/bin/env bash

set -euo pipefail

DRY_RUN="${DRY_RUN:-1}"
OWNER="${OWNER:-PapiDee09}"
REGISTRY="${REGISTRY:-repos.json}"

command -v gh >/dev/null 2>&1 || {
  echo "GitHub CLI (gh) required"
  exit 1
}

command -v jq >/dev/null 2>&1 || {
  echo "jq required"
  exit 1
}

gh auth status

echo

ready_count=0
exists_count=0
skip_count=0
hold_count=0
conflict_count=0
error_count=0

jq -c '.repositories[]' "$REGISTRY" | while read -r repo; do
  name="$(jq -r '.name' <<<"$repo")"
  upstream="$(jq -r '.upstream' <<<"$repo")"
  verified="$(jq -r '.verified' <<<"$repo")"
  policy="$(jq -r '.mirror_policy' <<<"$repo")"

  upstream_repo="${upstream#https://github.com/}"
  upstream_repo="${upstream_repo%.git}"

  upstream_owner="${upstream_repo%%/*}"
  target_name="${upstream_repo##*/}"
  target="${OWNER}/${target_name}"

  case "$policy" in
    fork_or_mirror|fork_or_mirror_preserve_notices)
      ;;
    *)
      echo "SKIP     $name — $policy"
      skip_count=$((skip_count + 1))
      continue
      ;;
  esac

  if [[ "$verified" != "true" ]]; then
    echo "HOLD     $name — verification pending"
    hold_count=$((hold_count + 1))
    continue
  fi

  # Query GitHub through GraphQL.
  # A genuinely missing repository returns repository=null without
  # confusing that condition with API/network/authentication failures.
  lookup="$(
    gh api graphql \
      -f query='
        query($owner: String!, $name: String!) {
          repository(owner: $owner, name: $name) {
            nameWithOwner
            isFork
            parent {
              nameWithOwner
            }
          }
        }
      ' \
      -F owner="$OWNER" \
      -F name="$target_name" \
      2>/dev/null || true
  )"

  # Empty/invalid output means an actual API/network/auth failure.
  if ! jq -e . >/dev/null 2>&1 <<<"$lookup"; then
    echo "ERROR    $name — invalid GitHub response for $target"
    error_count=$((error_count + 1))
    continue
  fi

  existing="$(jq -r '.data.repository // empty' <<<"$lookup")"

  if [[ -n "$existing" ]]; then
    is_fork="$(jq -r '.data.repository.isFork' <<<"$lookup")"
    parent="$(jq -r '.data.repository.parent.nameWithOwner // empty' <<<"$lookup")"

    parent_lower="$(printf '%s' "$parent" | tr '[:upper:]' '[:lower:]')"
    upstream_lower="$(printf '%s' "$upstream_repo" | tr '[:upper:]' '[:lower:]')"

    if [[ "$is_fork" == "true" && "$parent_lower" == "$upstream_lower" ]]; then
      echo "EXISTS   $name — $target ← $parent"
      exists_count=$((exists_count + 1))
      continue
    fi

    if [[ "$is_fork" == "true" ]]; then
      echo "CONFLICT $name — $target exists but parent is ${parent:-UNKNOWN}"
      echo "         expected parent: $upstream_repo"
      conflict_count=$((conflict_count + 1))
      continue
    fi

    echo "CONFLICT $name — $target exists but is not a fork"
    echo "         expected parent: $upstream_repo"
    conflict_count=$((conflict_count + 1))
    continue
  fi

  echo "READY    $name — $upstream_repo -> $target"
  ready_count=$((ready_count + 1))

  if [[ "$DRY_RUN" == "0" ]]; then
    if gh repo fork "$upstream_repo" --clone=false; then
      echo "CREATED  $name — $target"
    else
      echo "FAILED   $name — could not fork $upstream_repo"
      error_count=$((error_count + 1))
    fi
  fi
done

echo
echo "DRY_RUN=$DRY_RUN"
