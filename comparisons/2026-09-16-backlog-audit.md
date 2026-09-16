# 16 September 2026 — remaining stack backlog audit

Baseline: `agent-stack` reports 117 repository entries / 117 verified / 0 canonical-license pending. This audit reconciles the post-103 backlog against the current GitHub owner state and the standing admission policy.

## EXISTS — remove from unpushed queue

| Candidate | Current owned repo/state | Decision |
|---|---|---|
| Magnitude browser agent | `PapiDee09/browser-agent` | EXISTS — already mirrored; benchmark/promotion remains separate |
| Anthropic commerce-agents | `PapiDee09/commerce-agents` | EXISTS — already mirrored |
| Shotcraft | `PapiDee09/video-shotcraft` | EXISTS — already mirrored |

## READY for controlled intake / mirror

| Candidate | Canonical source | License / fit | Intake policy |
|---|---|---|---|
| Sona UI / skill | `Dinil-Thilakarathne/sona-ui` + Sona registry skill | MIT; React/Tailwind, registry-first agent skill, accessibility/reduced-motion guidance | Optional, review_required; mirror OSS repo/skill only |
| AICSS | `kvnkld/aicss` | MIT; React AI-agent conversation components + CLI; pro components are external/private | Optional, review_required; mirror public OSS repo only |
| Transitions.dev | `Jakubantalik/transitions.dev` | MIT for public repo/skill; useful motion recipes + agent skill | Optional, review_required; keep premium/auth content out of mirror |
| Brand Skills | `cofoundy/brand-skills` | MIT with NOTICE; portable agent skills and git-tracked brand package | Optional, review_required; preserve NOTICE |
| Hummingbot | `hummingbot/hummingbot` | Apache-2.0; strong modular trading-agent architecture reference, not a default product dependency | Reference/optional, review_required; no credentials/live trading by default |
| ArchiveBox | `ArchiveBox/ArchiveBox` | MIT; durable web evidence capture, AGENTS.md/skills present | Optional research/provenance infra, review_required |

## HOLD — do not mirror yet

| Candidate | Reason |
|---|---|
| Canvas UI | Exact intended upstream is ambiguous. `DavidHDev/canvas-ui` uses MIT + Commons Clause restricting resale/redistribution of components; `canvas-ui/*` projects include AGPL/commercial dual licensing. Resolve target and redistribution model first. |
| Lovart / OpenLovart | Search surfaces community clones/implementations rather than a clearly canonical open Lovart upstream. Provenance and licensing must be resolved before mirroring. |
| changedetection.io | Strong fit for monitoring and has Apache-2.0 source, but upstream also ships `COMMERCIAL_LICENCE.md` and resale/commercial wording. Reconcile those terms before owned redistribution. |
| Video Talkcraft | PolyForm Noncommercial 1.0.0; commercial toolkit use requires authorization. Keep reference-only until permission/terms change. |
| Infinite | Canonical repo not yet uniquely resolved in this audit. Hold until exact upstream, license and distinct job are verified. |
| AutoSocial | Canonical repo not yet uniquely resolved in this audit. Hold until exact upstream, license and credential/posting boundaries are verified. |

## METADATA / REFERENCE ONLY — not fork targets

| Candidate | Decision |
|---|---|
| GPT-6 Astra | Proprietary OpenAI model/runtime. Track model ID, availability, pricing/capabilities and runtime acceptance evidence; do not treat as a repo mirror. |
| Lyria 3.5 | Proprietary Google music model/API. Track as specialist audio capability and provider metadata; do not treat as a repo mirror. |
| Grokbot.dev | Catalog/directory/reference only. No stack dependency or owned fork required. |

## Queue after reconciliation

- 3 backlog items are already mirrored: Magnitude/browser-agent, commerce-agents, Shotcraft/video-shotcraft.
- 6 candidates are source/license-fit READY for controlled intake: Sona UI, AICSS, Transitions.dev, Brand Skills, Hummingbot, ArchiveBox.
- 6 candidates remain HOLD pending provenance/license/canonical verification: Canvas UI, Lovart, changedetection.io, Video Talkcraft, Infinite, AutoSocial.
- 3 items are metadata/reference-only rather than fork targets: GPT-6 Astra, Lyria 3.5, Grokbot.dev.

The counts overlap the historical 16-item wave because ArchiveBox and changedetection.io were added later and the historical list contained metadata/reference items that were never intended to become forks.

## Promotion rule

Mirroring is not core promotion. New mirrors enter `optional` / `review_required`. Promotion requires reproducible live tests, rollback, sanitized evidence, and an independently verified result. No trading credentials, social-posting credentials, production deployment, or destructive actions are authorized by this audit.
