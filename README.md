# Agent Stack Control Registry

Control plane for the reusable builder/agent stack.

## Census

- Repository entries: **94**
- Verified in this first research pass: **10**
- Pending canonical/license verification: **84**
- Target owner: **PapiDee09**
- Intended control repo: **PapiDee09/agent-stack**

## Current GitHub access

The connected GitHub app currently exposes only `PapiDee09/Donald`, `PapiDee09/Obagi-Java-Applications`, and `PapiDee09/Vegaflair`. Direct lookup for `PapiDee09/agent-lab` returned 404. The current connector also does not expose repository creation/fork creation, so no unrelated repo has been repurposed.

## Ownership model

Each upstream stays in its own fork/mirror. This control repo stores upstream URL, tier/category, licensing status, mirror policy, and later the tested tag/commit and sync state. Do not flatten all third-party histories into one monorepo.

## Policy meanings

- `fork_or_mirror`: candidate for an owned GitHub copy once verification passes.
- `reference_only_until_verified`: no public redistribution until terms are checked.
- `selective_mirror_by_subtree`: mixed licensing; only approved portions.
- `code_mirror_only_weights_separate`: source and model weights are governed separately.
- `mirror_with_copyleft_review`: mirror is possible, but copyleft obligations must stay explicit.

## Verified in this pass

Codex (Apache-2.0), Kimi Code (MIT), MengTo Skills (MIT), Agent Skills spec (Apache-2.0), Anthropic Skills (mixed: many Apache-2.0 plus source-available document skills), MCP reference servers (Apache-2.0/new contributions with legacy MIT), ThreeUI Community (MIT code with asset/font notices), Three.js (MIT), Tailwind CSS (MIT), and LTX-Video code (Apache-2.0; model terms separate).

## Next pass

1. Verify every pending entry against current LICENSE/NOTICE.
2. Resolve all mixed/open-core/research/model terms.
3. Add `default_branch`, `latest_tag`, `pinned_commit`, `last_verified_at`.
4. Create/fork safe repos under the GitHub owner.
5. Add upstream remotes and weekly drift checks.
6. Smoke-test the core repos and pin known-good revisions.
