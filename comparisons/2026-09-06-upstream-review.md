# Upstream review queue — 6 September 2026

Status: **review pending**. This document records isolated upstream update branches and draft pull requests. It does not change active stack pins or authorize merges.

## Review rules

- Keep every pull request in draft until its required checks pass.
- Do not promote a canary or unreleased mainline commit as a production dependency.
- Update `repos.json` pins only in a follow-up PR after compatibility is demonstrated.
- Preserve each current default-branch tip as the rollback point.
- Kimi CLI remains available until the Kimi Code migration and rollback checks pass.

## Pending updates

| Component | Target | Fork delta | Draft PR | Review focus | Promotion rule |
|---|---:|---:|---|---|---|
| SeaweedFS | `e6f2386` | 108 commits | [PapiDee09/seaweedfs#1](https://github.com/PapiDee09/seaweedfs/pull/1) | CVE-2026-46603, admin binding, S3 secret redaction | Security tests and admin compatibility must pass |
| Codex | `rust-v0.153.4` | 128 commits | [PapiDee09/codex#1](https://github.com/PapiDee09/codex/pull/1) | MCP, plugins, TUI sessions, Guardian | Stable-tag CI and agent smoke tests must pass |
| OpenTelemetry Collector | `v0.160.0 / v1.66.0` | 8 commits | [PapiDee09/opentelemetry-collector#1](https://github.com/PapiDee09/opentelemetry-collector/pull/1) | Go 1.26 and HTTP keepalive configuration | Build/config/exporter tests must pass |
| Next.js mirror | `v16.4.0-canary.19` | 52 commits | [PapiDee09/next.js#1](https://github.com/PapiDee09/next.js/pull/1) | Mirror freshness only | Production projects remain pinned to stable `v16.3.4` |
| Vitest | `v5.0.0` | 17 commits | [PapiDee09/vitest#1](https://github.com/PapiDee09/vitest/pull/1) | Node 22, Vite 6.4, removed APIs and output changes | Full compatibility matrix must pass |
| Kimi Code | `0.41.0` package commit | 81 commits | [PapiDee09/kimi-code#1](https://github.com/PapiDee09/kimi-code/pull/1) | Permission modes, guardrails, file history and migration | Security review and Kimi CLI rollback test must pass |
| Ray | `317c288` | 85 commits | [PapiDee09/ray#1](https://github.com/PapiDee09/ray/pull/1) | Per-sandbox network namespace behavior | Deployment-environment network matrix must pass |

## Initial CI state

GitHub Actions started automatically for SeaweedFS, Next.js and Vitest. Some upstream workflows do not automatically run in their forks or require fork-specific permissions/secrets; absence of a run is not a pass.

SeaweedFS CI produced two distinct blockers:

- **Dependency Review — repository configuration:** GitHub reports that dependency review is unsupported because the fork's dependency graph is disabled. This is not a code regression, but the security gate is unavailable until that setting is enabled.
- **Telemetry Integration Test — code/build:** the Go 1.26 build of `telemetry/server` reports that `go.mod` requires `go mod tidy`, so the integration test never starts. This is a merge blocker until the module diff is reviewed and the job passes.

The remaining SeaweedFS matrix and the queued Next.js/Vitest workflows are still pending. Neither SeaweedFS failure was rerun because neither is transient.

## Next decisions

1. Review and correct SeaweedFS module metadata, then rerun its telemetry job.
2. Enable the SeaweedFS fork's dependency graph before relying on dependency review.
3. Run reusable-stack smoke tests against Codex, Next.js stable, Vitest and Kimi Code.
4. Test SeaweedFS and Ray security behavior in representative Linux environments.
5. If a component passes, open a separate control-registry PR that records its tested tag, pinned commit, verification date and rollback commit.
6. If it fails, keep the current pin and document the blocker in its draft PR.
