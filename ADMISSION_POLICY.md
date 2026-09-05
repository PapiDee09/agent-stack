# Stack admission policy

The stack stays lean, reusable, production-oriented, and open-source-first.
An important release or tool is reviewed automatically, but importance alone
does not make it active or core.

## Intake gate

Classify every candidate as `READY`, `EXISTS`, `HOLD`, or `SKIP` after checking:

1. Canonical upstream, current release status, license/NOTICE, and redistribution rights.
2. A distinct reusable job in the Python, TypeScript/Node.js, React/Next.js,
   REST/API, LLM, n8n, SQL, Git/GitHub, agent, skill, MCP, evaluation,
   security, or deployment workflow.
3. Interoperability with the portable `AGENTS.md` contract and project-scoped
   skills, with Codex, Claude Code, and Kimi Code considered first-class runtimes.
4. Security boundaries, required permissions, credential handling, destructive
   operations, deployment impact, and rollback.
5. Reliability evidence, maintenance activity, total cost, vendor lock-in, and
   overlap with tools already in the registry.

## Decision rules

- `READY`: source and fit checks pass and all version-bound live acceptance tests pass.
- `EXISTS`: capability is already covered; update evidence or the tested pin only.
- `HOLD`: potentially useful, but live, security, cost, licensing, or migration evidence is missing.
- `SKIP`: redundant, prohibited, unmaintained, insufficiently reusable, or fails the license/security bar.
- New tools that pass source and fit review may enter `repos.json` as `optional`
  and `review_required`; this does not authorize installation, credentials, MCP
  connection, mirroring, production deployment, or core promotion.
- Core promotion requires reproducible tests, explicit rollback, sanitized evidence,
  and an independently verified task result. Missing or `NOT_RUN` checks block promotion.
- Proprietary tools remain `reference_only` unless their terms allow more. Mixed,
  copyleft, model-weight, and unclear licenses keep their stricter existing policy.
- Prefer the minimum toolset. Do not add a second tool for a job already covered
  unless measured reliability, portability, cost, or maintenance gains justify it.

## Recurring release handling

For consequential updates to registered tools, create a dated comparison record.
Supersede stale candidates with the newest verified stable release, but never
silently change an installed version, tested pin, model default, permission mode,
or runtime state. Security fixes increase test priority; they do not waive the gate.
