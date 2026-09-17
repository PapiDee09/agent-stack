# Anthropic Commerce Agents Evaluation — 2026-09-16

## Decision

**KEEP OPTIONAL — validated commerce architecture / specialist reference**

Upstream:
https://github.com/anthropics/commerce-agents

Evaluated commit:
`fd4d59224ab96b43c6dc6888207c67b3bd5a24cf`

License:
Apache-2.0

Registry classification:
- category: commerce-agent
- tier: optional
- dependency policy: review_required
- sync policy: review

## Static review

The repository contains shopping-agent and merchant-agent implementations,
shared commerce infrastructure, multiple runtime integrations, managed-agent
deployment paths, example storefronts and merchant applications.

Credential and external execution surfaces include Anthropic API credentials,
Claude Agent SDK integration, managed-agent deployment scripts, subprocess
execution and network deployment paths.

Those surfaces remain trust boundaries and are not enabled merely by this
evaluation.

## Python compatibility gate

The initial review used system Python 3.9.6 and could not satisfy the pinned
dependency set because `annotated-types==0.8.0` requires Python >=3.10.

This was classified as an environment incompatibility rather than an
implementation failure.

The evaluation was repeated in an isolated Python 3.12 virtual environment.

Dependency installation then completed successfully.

## Functional verification

Under Python 3.12:

- dependency installation: PASS
- repository consistency: PASS
- pytest suite: PASS
- shopping managed-agent deployment dry-run: PASS
- merchant managed-agent deployment dry-run: PASS
- retail storefront build: PASS
- retail merchant build: PASS
- travel storefront build: PASS
- travel merchant build: PASS
- telecom storefront build: PASS
- telecom merchant build: PASS
- entertainment storefront build: PASS
- entertainment merchant build: PASS

No live managed-agent deployment was performed.

No API credential was required for the acceptance gate.

## Ruff observation

The aggregate verification initially reported lint/format failures because
Ruff traversed the disposable `.review-venv` and inspected third-party
site-packages.

Evidence included paths under:

`.review-venv/lib/python3.12/site-packages/`

Therefore that aggregate Ruff result is not treated as evidence of thousands
of upstream source defects.

The review virtual environment is not part of the upstream source and remains
untracked.

## Admission assessment

Commerce Agents demonstrates useful reusable patterns for:

- shopping and merchant agent separation
- commerce tool orchestration
- session and role boundaries
- guarded write operations
- deployment abstraction
- multi-vertical commerce applications
- agent/runtime architecture

However, its credential surfaces, provider/runtime coupling and larger
dependency footprint do not justify making it universal stack infrastructure.

### Result

**RETAIN as an optional validated commerce-agent/reference capability.**

Do not promote it to universal/core infrastructure.

Live deployment, credentials and production merchant writes remain separately
review-gated.
