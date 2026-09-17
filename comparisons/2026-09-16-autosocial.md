# AutoSocial — Intake / Acceptance

## Capability

AutoSocial is a local social-media distribution workflow with queue,
scheduling, browser automation, video tooling and dashboard functionality.

Reviewed command surface includes:

- login
- post
- daemon
- uniquify
- video-info

The project contains actual browser-side publish-control discovery and click
logic, so authenticated execution is a meaningful external-action boundary.

## Acceptance Evidence

- Dependency installation: PASS.
- 83 packages installed / 84 audited.
- Upstream test suite: PASS.
- Tests: 22.
- Passed: 22.
- Failed: 0.
- CLI `--help`: PASS and passive in the acceptance run.
- No TikTok, Instagram, YouTube, Facebook or AutoSocial credential variable
  was intentionally supplied.
- Review checkout remained clean.
- Control repository remained clean.
- No login, upload, publish, scheduler daemon or authenticated browser action
  was executed.

Test coverage observed during acceptance included:

- safe debug cleanup targets
- `.env.example` personal-content defaults
- queue ordering and sidecars
- dashboard request guards
- cross-origin mutation rejection
- schedule normalization/timezone handling
- onboarding-folder exposure
- TikTok publish-control discrimination
- optional logo handling

## Dependency / Security Notes

The acceptance install reported two npm audit findings:

- one low severity
- one moderate severity

Reported packages included `body-parser` and `qs`.

Upstream reported fixes are available, but the benchmark checkout was not
modified with an automatic audit fix.

Install-script policy also reported a blocked `fsevents` install script.
No approval was granted during acceptance.

## Trust Boundary

AutoSocial can persist authenticated browser sessions and perform real
publishing actions.

Therefore passing tests do not authorize unattended posting from production
accounts.

Account login, persisted sessions, scheduled posting and autonomous publish
actions should remain explicitly configured high-trust capabilities with
separate operational review.

## Fit

The queue/scheduler/dashboard/browser architecture is useful for the reusable
stack's specialist distribution layer.

Its value is distinct from content generation: it handles the operational
handoff from prepared media into distribution workflows.

## Decision

**PUSH — OPTIONAL DISTRIBUTION SPECIALIST**

Retain AutoSocial as an optional specialist distribution capability and
architecture reference.

Do not enable authenticated autonomous publishing by default. Production
account/session access and unattended posting require separate explicit
configuration and acceptance.
