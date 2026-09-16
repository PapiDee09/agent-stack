# Video Shotcraft Evaluation — 2026-09-16

## Decision

**PUSH — specialist video-production capability**

Upstream:
https://github.com/Vincentwei1021/video-shotcraft

Evaluated commit:
`5e71af35a2daee492dd3ea93e5e8903f32dcd13c`

License:
Apache-2.0

Registry classification:
- category: media-video-production
- tier: optional
- dependency policy: review_required
- sync policy: review

## Static review

The repository exposes a comparatively small root execution surface and
contains a reusable Shotcraft skill, production template, motion assets,
Workbench, Remotion integrations, React, Three.js and React Three Fiber
capabilities.

No credential requirement was necessary for the acceptance tests.

## Dependency gate

Root npm installation completed successfully.

npm reported two moderate-severity dependency findings. No forced audit fix
was applied because doing so could introduce unreviewed breaking dependency
changes.

npm also blocked install scripts for esbuild and fsevents pending explicit
approval. No blanket install-script approval was granted.

## Unit acceptance

Root Vitest suite:

- test files: 1 passed
- tests: 23 passed
- failures: 0
- install exit: 0
- test exit: 0

Coverage exercised deterministic motion helpers including:

- mulberry32
- velocityAt
- lagged
- dampedSettle
- handheld

## Production smoke test

The supplied Remotion production template was installed and rendered.

Result:

- template installation succeeded
- render succeeded
- `out/promo.mp4` was created
- resulting artifact size: 20,835,435 bytes

This provides runtime evidence beyond static inspection and unit tests.

## Admission assessment

Shotcraft provides a distinct reusable job in the stack: structured
video-production and motion-shot capability.

It aligns with the existing React / Three.js production toolchain while
remaining separable from core agent infrastructure.

### Result

**ADMIT as a specialist capability.**

Keep it optional rather than universal/core. Consumers should opt into the
video-production layer when required.

Do not run automatic `npm audit fix --force`; dependency upgrades remain
review-gated.

Upstream changes remain subject to the stack sync/review policy.
