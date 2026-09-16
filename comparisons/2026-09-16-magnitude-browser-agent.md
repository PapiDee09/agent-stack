# Magnitude Browser Agent — Live Acceptance Review

Date: 2026-09-16
Decision: OPTIONAL / REVIEW_REQUIRED
Promotion: NOT PROMOTED
Category: browser-agent

## Source

- Upstream: magnitudedev/browser-agent
- Fork: PapiDee09/browser-agent
- License: Apache-2.0
- Upstream commit tested: f1b587c
- magnitude-test: 0.3.13
- magnitude-core: 0.3.1
- magnitude-mcp observed: 0.1.3

## Test Environment

The live acceptance test was executed in an isolated sandbox rather than
against a production application or authenticated browser profile.

Fixture:

- local HTTP server on 127.0.0.1:4173
- verification phrase input
- submit control
- asynchronous result state
- expected phrase: AP STACK VERIFIED
- expected result: MAGNITUDE_PASS

Telemetry was explicitly disabled in Magnitude configuration.

No production credentials, BigBag/AP application data, personal browser
profile, or authenticated production account was used.

## Static / Trust Review

Magnitude provides visual browser-agent execution and supports multiple
LLM provider configurations.

Observed trust-boundary considerations:

- localhost/private URL testing may involve Magnitude's external tunnel path
- browser execution can use persistent profiles/CDP in other configurations
- magnitude-test webServer configuration can spawn commands through a shell
- configuration therefore belongs inside the trusted execution boundary
- LLM inference introduces an external provider dependency
- model behavior and structured-output compatibility affect test reliability

These characteristics prevent automatic core-stack promotion.

## Live Results

### Runtime and browser bootstrap

PASS

- magnitude-test installed successfully
- isolated Chromium installed successfully
- Magnitude CLI started successfully
- Chrome for Testing launched successfully
- local fixture loaded successfully

### Provider authentication

PASS after replacing the initial invalid OpenRouter key.

A direct OpenRouter key-authentication request succeeded.

### Paid-model attempt

BLOCKED

The fixed Gemini route returned HTTP 402 because the free-tier account could
not satisfy Magnitude's requested maximum token allowance.

This was classified as a provider-credit preflight failure rather than a
browser-agent failure.

### Free-router behavioral run

PARTIAL / INCONCLUSIVE

Magnitude successfully:

- visually located the verification input
- focused the input
- detected existing incorrect content
- selected and cleared existing content
- entered `AP STACK VERIFIED`
- visually identified the submit control
- clicked the submit control
- noticed an incorrect intermediate state
- attempted recovery
- relocated the input
- cleared and re-entered the correct phrase
- completed the first agent step
- advanced to the second explicit test step

Observed run usage before failure:

- input tokens: 15,535
- output tokens: 5,566
- elapsed time: approximately 274 seconds
- completed steps: 2
- completed checks: 0

The run then failed at the LLM/BAML structured-output boundary:

`BamlValidationError: Missing required field: reasoning`

The final `MAGNITUDE_PASS` assertion was therefore never executed.

## Behavioral Finding: Action Boundaries

During the first instruction, which asked the agent to find the input and
enter the provided phrase, the planner also attempted to click the submit
control.

This crossed the intended boundary between two explicit test steps.

For low-risk browser testing this may be recoverable, but it is material for
workflows involving destructive or consequential actions such as purchase,
publish, send, delete, account mutation, or deployment.

A future promotion benchmark must therefore include an action-boundary test.

## Recovery Finding

The live run produced useful evidence of visual recovery behavior.

After observing incorrect input/state, the agent:

1. reconsidered the visible location,
2. refocused the input,
3. cleared the incorrect value,
4. re-entered the expected phrase,
5. continued toward submission.

This supports continued evaluation as a specialist browser-agent capability.

It does not constitute a full acceptance pass because the final assertion was
not reached.

## Reproducibility

The `openrouter/free` router is unsuitable as the final admission benchmark
because the underlying model may vary.

A reproducible promotion test requires a pinned compatible model.

No paid inference was purchased solely to complete this review.

## Admission Decision

KEEP OPTIONAL / REVIEW_REQUIRED.

Do not add Magnitude Browser Agent to `stack-state.json`.

Do not classify the current benchmark as PASS.

Do not classify the browser-agent capability itself as a definitive FAIL.

Promotion requires:

- pinned model/provider
- successful baseline test
- successful mutation/recovery test
- final assertion completion
- action-boundary discipline test
- acceptable latency/token cost
- documented tunnel/egress containment
- reproducible sanitized evidence

Until those conditions are satisfied, Magnitude remains available for
specialist evaluation but is not a safe-default or core dependency.
