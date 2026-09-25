# AI builder runtime and security review — 2026-09-25

Status: **REVIEW QUEUE — no automatic promotion**

This record consolidates the consequential runtime, MCP, evaluation and deployment decisions from the 2026-09-19 through 2026-09-25 builder briefings. It records candidate versions and promotion gates without changing active runtime pins.

## Decision summary

| Component | Candidate | Decision | Required gate |
|---|---:|---|---|
| Codex | 0.156.1 | TEST / REVIEW | Pin the model; disable voice when unused; verify default worktree isolation, resume behavior, sandbox boundaries and removal of `thread/rollback`. |
| Claude Code | 2.1.282 | TEST / REVIEW | Keep `review_required`; pin the model; validate delegated-session policy inheritance, symlink boundaries, restored approvals and project telemetry restrictions. |
| Kimi Code | 2.1.1 | HOLD / CONTAINER ONLY | Disable watchers for unattended evaluation; use restricted network, no credentials and no writable host mounts; test malicious repository Git config, symlinks and `local.toml`. |
| n8n | 2.40.6 | STAGE | Test queue workers, community nodes, credentials, fallback models, job timeouts, telemetry after restart and license-certificate reporting. |
| MCP Python SDK | 2.2.0 | TEST → CORE only after pass | Run redirect-origin, OAuth issuer, session-timeout and session-limit compatibility tests in Python 3.12. |
| Langfuse | 4.41 | WATCH | Do not add unless lightweight JSON/pytest and Claude plugin evaluations are insufficient; account for the 4.39 gateway metadata namespace change. |
| OpenAI Agents Python / JS | 0.22.3 / 0.18.0 | EXISTING INTEGRATIONS ONLY | Upgrade only where already used; keep file-I/O and sandbox regression gates. |
| LiteLLM | 1.101+ | WATCH | Add only when centralized routing, budgets and shadow evaluation become an actual requirement. |

## Registry policy changes in this review

- **Codex:** `safe_default/auto` → `review_required/review`. Recent releases change model selection, voice/worktree defaults and sandbox behavior; automatic promotion would make comparisons unreliable.
- **Kimi Code:** `safe_default/auto` → `review_required/manual`. Version 2.1.1 deliberately reverted post-trust symlink, Git-config and project-local configuration hardening.

Claude Code, n8n and Langfuse already have suitably conservative registry policies, so their registry entries remain unchanged.

## Promotion order

1. Claude Code 2.1.282 after the delegated-policy canary.
2. Codex 0.156.1 after the worktree/sandbox and model-pin canary.
3. n8n 2.40.6 after staging and restart/worker tests.
4. MCP Python SDK 2.2.0 after the Python 3.12 security-compatibility canary.
5. Kimi remains blocked from unattended production regardless of feature parity until external-containment tests pass and the upstream trust-boundary decision changes.

## Sources

- [Codex 0.156.0](https://github.com/openai/codex/releases/tag/rust-v0.156.0) and [0.156.1](https://github.com/openai/codex/releases/tag/rust-v0.156.1)
- [Claude Code 2.1.281](https://github.com/anthropics/claude-code/releases/tag/v2.1.281) and [2.1.282](https://github.com/anthropics/claude-code/releases/tag/v2.1.282)
- [Kimi Code 2.1.0](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%402.1.0), [2.1.1](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%402.1.1), and [trust-boundary reversion](https://github.com/MoonshotAI/kimi-code/pull/4013)
- [n8n 2.40.6](https://github.com/n8n-io/n8n/releases/tag/n8n%402.40.6)
- [MCP Python SDK 2.2.0](https://github.com/modelcontextprotocol/python-sdk/releases/tag/v2.2.0)
- [Langfuse 4.41.0](https://github.com/langfuse/langfuse/releases/tag/v4.41.0)
