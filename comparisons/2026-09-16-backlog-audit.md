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
| AutoSocial | `Katzca/AutoSocial` | MIT; local Node/Playwright multi-account posting dashboard for TikTok/Instagram/YouTube | Optional specialist distribution layer, review_required; no credentials or autonomous posting by default |

## READY as reference / install-at-use, not owned mirror

| Candidate | Canonical source | Reason |
|---|---|---|
| Canvas UI | `DavidHDev/canvas-ui` | MIT + Commons Clause permits use in our apps but restricts reselling/redistributing the component library itself. Keep as reference/install-at-use; do not mirror components into a public owned distribution repo. |
| Lovart Skill | `lovartai/lovart-skill` | Official Lovart OpenAPI skill for image/video/visual generation. Treat as provider skill/reference with credentials kept external; do not rely on community Lovart clones. |

## HOLD — do not mirror yet

| Candidate | Reason |
|---|---|
| changedetection.io | Strong fit for monitoring and Apache-2.0 is present, but upstream also publishes commercial-license/resale wording that is currently ambiguous. Keep HOLD until redistribution/commercial terms are reconciled. |
| Video Talkcraft | PolyForm Noncommercial 1.0.0; commercial use of the toolkit requires prior authorization. Reference-only unless permission/terms change. |
| Infinite | Exact historical target remains unresolved. `InfiniteRoomLabs/agent-ops` is a plausible MIT agent/skills architecture candidate, while `polyuiislab/infiAgent` is a distinct GPL-3.0 long-horizon runtime. Do not guess which one the backlog item referred to; resolve target before intake. |

## METADATA / REFERENCE ONLY — not fork targets

| Candidate | Decision |
|---|---|
| GPT-6 Astra | Proprietary OpenAI model/runtime. Track model ID, availability, pricing/capabilities and runtime acceptance evidence; do not treat as a repo mirror. |
| Lyria 3.5 | Proprietary Google music model/API. Track as specialist audio capability and provider metadata; do not treat as a repo mirror. |
| Grokbot.dev | Catalog/directory/reference only. No stack dependency or owned fork required. |

## Queue after reconciliation

- 3 backlog items are already mirrored: Magnitude/browser-agent, commerce-agents, Shotcraft/video-shotcraft.
- 7 candidates are source/license-fit READY for controlled owned intake: Sona UI, AICSS, Transitions.dev, Brand Skills, Hummingbot, ArchiveBox, AutoSocial.
- 2 candidates are READY for reference/install-at-use but should not become owned public mirrors: Canvas UI, official Lovart Skill.
- 3 candidates remain HOLD: changedetection.io, Video Talkcraft, Infinite.
- 3 items are metadata/reference-only rather than fork targets: GPT-6 Astra, Lyria 3.5, Grokbot.dev.

The counts overlap the historical 16-item wave because ArchiveBox and changedetection.io were added later and the historical list contained metadata/reference items that were never intended to become forks.

## Promotion rule

Mirroring is not core promotion. New mirrors enter `optional` / `review_required`. Promotion requires reproducible live tests, rollback, sanitized evidence, and an independently verified result. No trading credentials, social-posting credentials, provider secrets, production deployment, or destructive actions are authorized by this audit.
