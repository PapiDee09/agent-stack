# Transitions.dev — Intake / Acceptance

## Upstream

- Repository: https://github.com/Jakubantalik/transitions.dev
- Pinned review commit: `598d3d6ad89dabb4bdf742fd2e887ca53914a888`
- CLI package: `transitions-dev` 0.3.0
- Refine package: `transitions-refine` 0.3.34

## Capability

The repository provides:

- transitions.dev motion recipes
- motion-token vocabulary
- transitions polish skill
- free transition CLI
- deterministic Refine token-alignment engine
- agent-driven live Refine/write-back system

The deterministic engine evaluates duration, easing, scale, blur, and
translation distance against the transitions.dev motion-token vocabulary.
Its matching includes usage-aware decisions for applicable token classes.

## Acceptance Evidence

- `npm run build`: PASS.
- Build rendered 34 transition/skill artifacts from `index.html`.
- Correct CLI entrypoint:
  `cli/bin/transitions-dev.mjs`
- Core CLI help: PASS.
- Deterministic `motion-tokens.mjs` load: PASS.
- Deliberately off-token sandbox fixture hash was unchanged after deterministic
  module load.
- Review checkout restored to pinned commit and clean.
- Control repository remained clean.

## Refine Agent Findings

A supposed passive `--help` invocation of the Refine CLI was not passive.

It:

- injected a timeline into `index.html`
- created `.agents/skills/refine-live`
- started a relay on localhost
- detected Claude Code
- selected:
  `claude -p --dangerously-skip-permissions`

The invocation was stopped and its generated changes were subsequently
removed. The checkout was restored cleanly.

Refine also supports Codex and Cursor agent execution. Agent commands are
spawned by the relay.

## Write-Boundary Finding

The live write-back implementation does not satisfy the control repository's
containment requirement at the reviewed commit.

Its source-file resolution considers candidates including:

- `join(WORKSPACE, componentHint)`
- `join(WORKSPACE, "..", componentHint)`
- `join(process.cwd(), componentHint)`

`handleApply()` then writes a resolved existing file using `writeFileSync`.

The reviewed path did not demonstrate a canonicalized realpath containment
check immediately before this write. In particular, the explicit
`WORKSPACE/..` candidate can resolve outside the declared workspace.

Therefore agent-driven Refine is not approved for production repositories.

## Overlap

The repository overlaps with Motion.dev, Anime.js and existing motion/design
references, but its motion-token vocabulary, recipe library, polish workflow,
and deterministic refinement logic provide a distinct reusable motion-quality
layer.

It should complement rather than replace the existing animation runtimes.

## Decision

**PUSH — CORE TRANSITIONS CAPABILITY AS OPTIONAL SPECIALIST**

Admit the core recipes, motion-token system, CLI and deterministic refinement
patterns as an optional specialist capability.

**HOLD — AGENT-DRIVEN REFINE / WRITE-BACK**

Do not run the current agent-driven Refine/write-back path against production
projects. Reconsider only after workspace containment is enforced and
reproducibly tested, and agent execution no longer requires an unacceptable
permission bypass for the selected runtime.
