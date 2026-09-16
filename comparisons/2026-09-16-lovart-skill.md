# Lovart Skill — Stack Evaluation

Date: 2026-09-16

## Candidate

- Name: Lovart Skill
- Upstream: https://github.com/lovartai/lovart-skill
- Evaluated commit: 3ea0f8e76f9e7b96b6f87969f0ea4f7a1d4cfd30
- Category: media-generation-agent-skill

## Evaluation

The skill exposes an external Lovart-backed generation workflow.

Credential surface:

- LOVART_ACCESS_KEY
- LOVART_SECRET_KEY

The reviewed client performs authenticated requests using those
credentials.

No production credentials were supplied during evaluation.

## Acceptance Gate

- Python compile: PASS
- CLI --help: PASS
- compile exit: 0
- help exit: 0
- Lovart state before/after gate: none observed
- checkout mutation: none observed
- control repository mutation: none observed
- paid/live generation: NOT RUN

## Decision

REFERENCE / OPTIONAL SPECIALIST.

Retain as a specialist production capability candidate, but do not make
it a core dependency.

Admission to an active project remains conditional on:

- actual need for Lovart-specific capability
- approved credentials
- acceptable service cost
- privacy/data-flow review
- live output-quality benchmark

Do not store Lovart credentials in the control repository.
