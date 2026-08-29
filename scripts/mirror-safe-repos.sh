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

jq -c '.repositories[]' "$REGISTRY" | while read -r repo; do
  name="$(jq -r '.name' <<<"$repo")"
  upstream="$(jq -r '.upstream' <<<"$repo")"
  verified="$(jq -r '.verified' <<<"$repo")"
  policy="$(jq -r '.mirror_policy' <<<"$repo")"

  upstream_repo="${upstream#https://github.com/}"
  upstream_repo="${upstream_repo%.git}"
  target_name="${upstream_repo##*/}"
  target="${OWNER}/${target_name}"

  case "$policy" in
    fork_or_mirror|fork_or_mirror_preserve_notices)
      ;;
    *)
      echo "SKIP  $name — $policy"
      continue
      ;;
  esac

  if [[ "$verified" != "true" ]]; then
    echo "HOLD  $name — verification pending"
    continue
  fi

  if gh repo view "$target" >/dev/null 2>&1; then
    echo "EXISTS $name — $target"
    continue
  fi

  echo "READY $name — $upstream -> $target"

  if [[ "$DRY_RUN" == "0" ]]; then
    gh repo fork "$upstream_repo" \
      --clone=false \
      --remote=false
  fi
done

echo
echo "DRY_RUN=$DRY_RUN"
