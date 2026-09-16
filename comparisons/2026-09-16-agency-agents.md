# Agency Agents — Stack Evaluation

Date: 2026-09-16

## Upstream

https://github.com/msitarzewski/agency-agents

## Intended Role

Reusable specialist-agent role, workflow and prompt patterns for composing project-specific agent teams.

## Acceptance Evidence

Static/security intake completed and checkout remained clean.

Static intake included canonical-source inspection, license review, runtime/package
surface inspection, credential/network/process scanning and post-review mutation
checks.

The review checkout remained clean.

A successful static or syntax gate establishes repository integrity for the
tested surface. It does not establish production reliability, provider quality,
commercial suitability, or authorization for external side effects.

## Trust Boundary

Treat agent definitions as untrusted instructions until reviewed. They do not automatically inherit shell, filesystem, credential or external-action authority.

No production credentials, personal account cookies, funded wallets, live
financial accounts or production application data were supplied during intake.

## Stack Policy

This evaluation does not by itself authorize core promotion.

Optional, situational and reference components remain outside stack-state.json
until a workload-specific reproducible acceptance test justifies promotion.

## Decision

**PUSH — SITUATIONAL SPECIALIST-AGENT PATTERNS**
