# Wave H — Bulk Agent Lab Capability Intake

Date: 2026-09-18

## Scope

Thirty repositories were reviewed in a separate Wave H workspace.

The intake performed:

- canonical shallow checkout
- commit capture
- root-license discovery
- manifest discovery
- static authority-surface scanning
- Python parse screening
- skill and AGENTS.md inventory
- lifecycle-script discovery
- explicit risk-line extraction
- worktree mutation verification

No credentials were supplied.
No project dependencies were installed.
No third-party project code was intentionally executed.
All 30 review worktrees remained clean.
BigBag Emporium remained outside the Wave H workspace.

Static regex matches are trust-boundary indicators, not vulnerability findings.

## PUSH candidates

### Cloudflare Security Audit Skill

Classification: PUSH — OPTIONAL SECURITY-AUDIT SPECIALIST

Distinct job:
Structured agent-driven security auditing with reconnaissance, coverage tracking, isolated hunting, independent validation, machine-readable findings and defensive reporting.

Boundary:
Target-controlled builds, tests, browsers, fuzzers or fixtures require an OS-enforced sandbox with sanitized environment, network restrictions, resource limits and scratch-only writes.

Do not grant production credentials or unrestricted execution authority.

### Trail of Bits Skills

Classification: PUSH — CURATED SECURITY / ENGINEERING SKILL SOURCE

Distinct job:
Reusable security-analysis, static-analysis, testing and engineering workflows from a security-focused skill marketplace.

Boundary:
Admit skills selectively.
Do not automatically import the entire marketplace or grant individual skills shell, network, filesystem or credential authority.

### OpenResearch

Classification: PUSH — OPTIONAL RESEARCH HARNESS

Distinct job:
Turns coding agents into research agents with isolated worktrees, parallel exploration, reproducible experiments and evidence-linked artifacts.

Boundary:
Local-first usage preferred.
Managed compute, external search integrations and account-backed services remain optional/high-trust surfaces.

### MCP Toolbox for Databases

Classification: PUSH — OPTIONAL DATABASE TOOLING SPECIALIST

Distinct job:
Controlled database tools for agents with predefined tool logic, structured queries, connection management, authentication and observability.

Boundary:
Database credentials and write-capable tools remain workload-specific.
Prefer least-privilege read-only tools until a task explicitly requires mutation.

### Supervision

Classification: PUSH — OPTIONAL COMPUTER-VISION SPECIALIST

Distinct job:
Model-agnostic computer-vision utilities for detections, segmentation, tracking, datasets, annotation and video/image pipelines.

Boundary:
Core library can remain provider-neutral.
Hosted inference/API-key integrations are optional and must not become required dependencies.

### Astryx

Classification: PUSH — OPTIONAL AGENT-READABLE UI SPECIALIST

Distinct job:
Candidate machine-readable UI/component capability for agent-driven frontend work.

Boundary:
Keep optional until a contained frontend acceptance benchmark establishes concrete advantage over existing UI/design stack.

### Addy Osmani Agent Skills

Classification: PUSH — CURATED ENGINEERING SKILL SOURCE

Distinct job:
Reusable engineering and agent workflow skills.

Boundary:
Curate individual skills rather than bulk-installing every skill.
Deduplicate against existing stack skills before admission.

## BENCHMARK candidates

### Sandbox cluster

- CubeSandbox
- Kubernetes Agent Sandbox
- E2B Runtime

Classification: BENCHMARK — SANDBOX RUNTIME COMPETITION

Required comparison:
Isolation strength, local usability, startup latency, resource overhead, networking controls, filesystem controls, credential isolation, reproducibility and rollback.

Do not install all three as permanent stack dependencies.

### Memory cluster

- Beads
- MemOS
- existing Codebase Memory MCP

Classification: BENCHMARK — MEMORY / PERSISTENCE COMPETITION

Required comparison:
Codebase retrieval, task memory, cross-session persistence, provenance, storage overhead, context savings and failure recovery.

### BrowserSkill

Classification: BENCHMARK — HIGH-TRUST BROWSER SPECIALIST

Compare against existing Magnitude/browser-agent capability.

Authenticated sessions, cookies, personal browser profiles, posting, purchasing and external account actions remain explicitly gated.

### Open Code Review

Classification: BENCHMARK — CODE-REVIEW SPECIALIST

Determine whether it adds deterministic/reproducible review value beyond existing coding agents and security skills.

Postinstall behavior requires inspection before dependency installation.

### OpenObserve

Classification: BENCHMARK — OBSERVABILITY INFRASTRUCTURE

Evaluate as an agent trace/log/metrics backend before accepting infrastructure cost and operational complexity.

### Strands Harness SDK

Classification: BENCHMARK — AGENT-HARNESS ALTERNATIVE

Compare against existing orchestration/control-plane capability.
Do not create another default agent runtime without measurable advantage.

### WeKnora

Classification: BENCHMARK — KNOWLEDGE / RAG SPECIALIST

Compare retrieval quality, provenance, operational complexity and overlap with existing memory/research layers.

### Voicebox

Classification: BENCHMARK — VOICE SPECIALIST

Compare with existing VoxCPM capability on local operation, quality, latency, language coverage, deployment complexity and licensing.

### FastVideo

Classification: BENCHMARK — VIDEO INFERENCE SPECIALIST

Hardware-heavy inference requires a separate machine-capability benchmark.
Do not download large model weights during registry admission.

### Remotion

Classification: BENCHMARK / UPSTREAM FOUNDATION

Determine which capability is already inherited through Shotcraft and whether direct Remotion admission adds a reusable layer rather than duplicate dependency surface.

## REFERENCE / ARCHITECTURE

### Coder

Classification: REFERENCE — SECURE DEVELOPMENT ENVIRONMENT ARCHITECTURE

Useful architecture for isolated development environments.
Do not add large infrastructure merely to make Agent Lab appear more capable.

### Temporal

Classification: REFERENCE — DURABLE WORKFLOW ARCHITECTURE

Potential future durable-execution layer.
Promote only when Agent Lab has workflows requiring crash recovery, long-running state or durable retries.

### NATS Server

Classification: REFERENCE — EVENT / MESSAGING ARCHITECTURE

Potential future event bus.
Not justified as a default dependency while simpler process boundaries suffice.

### Vault

Classification: REFERENCE — SECRETS / IDENTITY ARCHITECTURE

Use as an architectural reference and possible production infrastructure.
Do not introduce operational Vault infrastructure merely for local development.

### LocalMiniDrama

Classification: REFERENCE — LOCAL VIDEO PIPELINE PATTERNS

Study reusable pipeline and orchestration patterns.
Existing video capabilities remain preferred unless a distinct production advantage is demonstrated.

## HOLD / CURATE

### ECC

Classification: HOLD — CURATE BEFORE ADMISSION

The review checkout exposed 903 SKILL.md documents.
Bulk import would violate the minimum-toolset policy.

Required:
Cluster skills, identify provenance, remove duplicates and select only high-value capability gaps.

### Anthropic Knowledge Work Plugins

Classification: HOLD — CURATE / DEDUPLICATE

Large skill surface.
Select only distinct workflows not already covered by the stack.

### OpenSRE

Classification: HOLD — SPECIALIST REVIEW

Potentially valuable SRE capability, but runtime/version assumptions and authority surface need targeted acceptance before admission.

### Multica

Classification: HOLD — COLLABORATION ARCHITECTURE REVIEW

Potential multi-agent collaboration value.
Requires a concrete comparison against the existing control plane before dependency admission.

### Caveman

Classification: HOLD — TOKEN-EFFICIENCY BENCHMARK

Potential context/token optimization value.
Requires measurable token reduction, quality retention and operational-overhead evidence.

## Admission rule

PUSH does not mean core.

Wave H registry admission, when approved, means optional/review-required capability registration only.

It does not authorize:

- credentials
- production data
- unrestricted shell execution
- personal browser sessions
- MCP installation
- external account actions
- model downloads
- privileged containers
- deployment
- stack-state promotion

Core promotion requires a reproducible workload-specific benchmark, rollback path and independently verified evidence.
