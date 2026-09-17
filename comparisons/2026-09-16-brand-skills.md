# Brand Skills — Stack Evaluation

Date: 2026-09-16

## Candidate

- Name: Brand Skills
- Upstream: https://github.com/cofoundy/brand-skills
- Evaluated commit: c50d6c9988e22b39031266924ae7d87f643e34bf
- Category: brand-agent-skills
- License files: LICENSE + NOTICE

## Evaluation

Static inspection identified 15 specialist brand skills covering:

- brand architecture
- brand audit
- brand context
- brand guidelines
- brand identity
- brand initialization
- brand messaging
- brand positioning
- brand story
- brand strategy
- brand voice
- competitor branding
- naming
- rebranding
- target audience

The naming workflow has an outbound network surface including WHOIS,
curl, package registries, GitHub and other availability checks.

No credentials are required for the core brand workflow.

## Acceptance Gate

- skill validation: PASS
- validation exit: 0
- checkout mutation: none observed
- control repository mutation: none observed

## Decision

PUSH as an optional reusable brand-specialist capability.

Use it to create and maintain persistent structured brand context rather
than recreating brand identity and strategy independently for every
project.

Keep network-enabled naming/availability checks permission-scoped.

Do not classify as universal agent runtime infrastructure.
