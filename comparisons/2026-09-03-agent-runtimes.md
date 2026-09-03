# Agent runtime update comparison — 3 September 2026

## Decision

Accept all three releases into the comparison queue. **Promote none yet.**
Official release and top-level license checks pass; relevance to the existing
stack passes review. Live acceptance, migration, and cost checks have not run.
HOLD means missing evidence, not a demonstrated regression.

Baseline: `PapiDee09/agent-stack` commit
`9efa5bca197e7e5d4f473fb104823ddebe6cac0b`.
The machine-readable record is [2026-09-03-agent-runtimes.json](2026-09-03-agent-runtimes.json).
It is an intake record, not an installer or an active runtime configuration.

## Comparison

| Runtime | Candidate | Fit | Main migration risk | Promotion |
| --- | --- | --- | --- | --- |
| Codex | 0.153.0 | Improves MCP account separation and session recovery | Approval-mode behavior and experimental context portability | HOLD: live regression tests missing |
| Claude Code | 2.1.259 | Improves unattended execution and concurrent workflows | Managed MCP allowlist semantics changed | HOLD: authentication and policy tests missing |
| Kimi Code | 0.40.1, including 0.40.0 changes | Improves guards and configuration handling | Default model pool, ACP engine, and Bash cwd behavior changed | HOLD: authentication, containment, routing and cost tests missing |

### Codex

The release scopes remembered MCP approvals to an app account and improves
recovery across disconnects, restarts, and compaction. Full Access changes
Guardian review handling. Experimental context management is off by default
and excludes API-key/custom-provider sessions.

Keep the portable baseline free of that experiment. Test the macOS MCP path
fix, approval separation, and restart behavior before changing a tested pin.
The candidate's top-level LICENSE matches the registry's Apache-2.0 label;
retain license/NOTICE obligations. This is not a transitive-license audit.

Sources: [release](https://github.com/openai/codex/releases/tag/rust-v0.153.0),
[tagged LICENSE](https://github.com/openai/codex/blob/rust-v0.153.0/LICENSE).

### Claude Code

The release adds unattended prompt denial, fixes indirect file-read deny gaps,
and addresses concurrent configuration loss and duplicate/still-running agents.
`allowedMcpServers` now filters user-added servers; managed exclusions need
`deniedMcpServers`. Invalid managed policy prevents startup.

Preserve `reference_only`, `review_required`, and `sync_policy: none`.
The tagged license points to Anthropic commercial terms; this review does not
grant redistribution rights or waive the existing usage review.

Sources: [release](https://github.com/anthropics/claude-code/releases/tag/v2.1.259),
[tagged license](https://github.com/anthropics/claude-code/blob/v2.1.259/LICENSE.md).

### Kimi Code

Version 0.40.1 fixes migration prompting. Version 0.40.0 changes the default
subagent pool and ACP engine, removes the Bash cwd workspace restriction,
adds a dangerous-command guard, and changes the default folder-trust selection.

Keep the guard enabled and use external containment. Start comparison runs
with the secondary-model pool explicitly disabled, then measure it separately.
Retain the MIT policy and copyright notice. Keep modern Kimi Code and
Kimi CLI Legacy distinct; their version numbers are not interchangeable.

Sources: [official release history](https://github.com/MoonshotAI/kimi-code/releases),
[tagged LICENSE](https://github.com/MoonshotAI/kimi-code/blob/@moonshot-ai/kimi-code@0.40.1/LICENSE).

## Evidence boundaries

- `repos.json` keeps all existing dependency, mirror, tier and sync policies.
- `stack-state.json` records Codex as EXECUTION_READY and Claude/Kimi as
  AUTH_REQUIRED. These are existing recorded states, not fresh device checks.
- Its `upstream_commit` values are observed upstream baselines, not proof of
  installed versions or tested production pins. Installed versions are unknown.
- `codex`, `claude`, and `kimi` were absent from PATH in the evaluation
  workspace. No live agent acceptance or macOS test was executed.
- The existing 140 offline tests recorded for the control plane do not certify
  these new runtime releases. No new runtime test pass is claimed.
- No software was installed, no authentication was changed, no upstream mirror
  was synchronized, and no active runtime state or pin was modified.

## Promotion checklist

This is the conservative checklist for this intake, not a claim that these exact
thresholds previously existed. Preserve stricter project rules if present.

1. Capture installed baseline version, candidate tag/commit, configuration hash,
   OS/architecture, model/provider, and a reproducible rollback procedure.
2. Confirm entitlement/authentication in an isolated test environment. Use only
   dummy secrets and test accounts; never publish credentials or raw sensitive logs.
3. Run the same small Python bug-fix and TypeScript/API task against baseline
   and candidate, with the same project contract and skill contents. Evaluate
   the patch independently with tests; verify instruction loading per runtime.
4. Exercise runtime-enforced deny rules, attempted outside-workspace access,
   stop/resume, and applicable MCP migration/account separation. Require zero
   secret disclosures, unauthorized writes, duplicate actions, or hanging prompts.
   Test dangerous commands through mocks or a disposable container, never the host.
5. Record task success, elapsed time, token/usage data and cost. No unsupported
   model routing or unexplained material cost regression is acceptable.
6. Link sanitized, version-bound results for every required JSON check. A missing
   or NOT_RUN check blocks promotion. Human review is needed for any justified N/A.
7. Only after all checks pass, record the tested version/commit and evidence in
   the canonical registry using a reviewed, rollbackable change. Preserve unrelated
   state and all licensing restrictions. Do not equate mirror freshness with
   runtime safety, or turn AUTH_REQUIRED into EXECUTION_READY without a real test.

## First test to run

Prioritize Claude's unattended deny regression, then Codex account/resume tests,
then Kimi containment/ACP/routing tests. For Claude, use a disposable repo with
a runtime-denied dummy secret and one harmless allowed test command. Run the
headless session with `--permission-prompts none`, inspect attempted tool actions
and output, and verify both successful allowed execution and blocked secret access.
A task that never attempts the denied action is inconclusive, not a pass.

The remaining blocker is access to an authenticated, isolated runtime test
environment, including the target Mac for macOS-specific checks.
