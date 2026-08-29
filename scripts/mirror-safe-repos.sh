#!/usr/bin/env bash
set -euo pipefail
OWNER="${OWNER:-PapiDee09}"
REGISTRY="${REGISTRY:-repos.json}"
DRY_RUN="${DRY_RUN:-1}"
command -v gh >/dev/null || { echo "GitHub CLI (gh) required"; exit 1; }
command -v jq >/dev/null || { echo "jq required"; exit 1; }
gh auth status
jq -c '.repositories[]' "$REGISTRY" | while read -r row; do
  name=$(jq -r '.name' <<<"$row")
  upstream=$(jq -r '.upstream' <<<"$row")
  policy=$(jq -r '.mirror_policy' <<<"$row")
  verified=$(jq -r '.verified' <<<"$row")
  case "$policy" in
    fork_or_mirror|fork_or_mirror_preserve_notices|fork_or_mirror_core_only|mirror_reference_not_daily_fork) ;;
    *) echo "SKIP  $name — $policy"; continue ;;
  esac
  [[ "$verified" == "true" ]] || { echo "HOLD  $name — verification pending"; continue; }
  repo=$(basename "$upstream")
  echo "READY $name — $upstream -> $OWNER/$repo"
  if [[ "$DRY_RUN" == "0" ]]; then
    if gh repo view "$OWNER/$repo" >/dev/null 2>&1; then
      echo "EXISTS $OWNER/$repo"
    else
      gh repo fork "$upstream" --clone=false
    fi
  fi
done
echo "DRY_RUN=$DRY_RUN (set DRY_RUN=0 only after review)"
