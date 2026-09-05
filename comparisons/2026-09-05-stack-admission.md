# Stack admission review — 5 September 2026

## Decision

Add **Catalyst Agent Skills** to the registry as `optional`, `review_required`,
and review-synced. It passes canonical-source, Apache-2.0 license, portability,
and stack-relevance checks, but its infrastructure-writing Zoho MCP path and
Catalyst platform coupling prevent core/default status without a real project need
and isolated acceptance tests.

Keep Codex, Claude Code, and Kimi Code in their existing registry roles. Update
their comparison candidates to the newest verified stable releases, but promote
none: no authenticated version-bound test evidence was produced in this review.

Machine-readable evidence: [2026-09-05-stack-admission.json](2026-09-05-stack-admission.json).

## Decisions

| Candidate | Registry decision | Active/pin decision | Reason |
| --- | --- | --- | --- |
| Codex 0.153.4 | `EXISTS` as core | `HOLD` | The release can make Astra the bundled default when no model is explicit; pin the model before evaluation. |
| Claude Code 2.1.261 | `EXISTS` as core/reference-only | `HOLD` | It includes the 2.1.260 permission fixes and adds skill/context diagnostics, but authenticated policy tests remain missing. |
| Kimi Code 0.41.0 | `EXISTS` as core | `HOLD` | Auto permission mode no longer blocks dangerous or statically unanalyzable commands; external containment must be demonstrated. |
| Catalyst Agent Skills | `READY` for optional registry intake | `HOLD` for installation/MCP use | Portable Apache-2.0 skill library with Node.js, Python, REST, data and deployment guidance; provider overlap and privileged operations require opt-in review. |
| Zoho Catalyst platform | `SKIP` as core; watch/reference only | No deployment change | Proprietary hosted platform overlaps Supabase, hosting and observability choices and has unverified account, region, cost and exit assumptions. |

## Runtime candidate notes

### Codex 0.153.4

The 0.153.3–0.153.4 patches add Astra to additional model catalogs and make it
the bundled default when no model is explicitly configured. Before testing or
upgrading, record and explicitly pin the current model so a runtime update does
not also become an unmeasured model migration.

Sources: [0.153.4 release](https://github.com/openai/codex/releases/tag/rust-v0.153.4),
[tagged Apache-2.0 license](https://github.com/openai/codex/blob/rust-v0.153.4/LICENSE).

### Claude Code 2.1.261

This stable release supersedes 2.1.260. It retains the permission-rule fixes
that motivated the regression matrix and adds `/skill-doctor`, organization-policy
diagnostics, output-size controls, resume/interrupt fixes, and broader dangerous-`rm`
detection. Keep `reference_only`, `review_required`, and `sync_policy: none`.

Sources: [2.1.261 release](https://github.com/anthropics/claude-code/releases/tag/v2.1.261),
[tagged commercial license](https://github.com/anthropics/claude-code/blob/v2.1.261/LICENSE.md).

### Kimi Code 0.41.0

The release improves compaction recovery, persisted subagent resume, and file
history, but changes auto permission mode so dangerous and statically
unanalyzable commands are no longer blocked. Treat `Never Ask`/auto execution as
unsafe without a disposable container and runtime-independent filesystem/process
controls. Do not enable experimental Tower mode in the portable baseline.

Sources: [0.41.0 release](https://github.com/MoonshotAI/kimi-code/releases/tag/%40moonshot-ai/kimi-code%400.41.0),
[tagged MIT license](https://github.com/MoonshotAI/kimi-code/blob/%40moonshot-ai/kimi-code%400.41.0/LICENSE).

## Catalyst Agent Skills boundary

The repository has 16 `SKILL.md` files covering Catalyst functions, AppSail,
Slate, data, storage, auth, Node.js/Python/Web SDKs, pricing, and Zoho MCP. It
also includes lightweight behavior-eval cases. Its instructions prefer direct
MCP infrastructure operations and include deploy, overwrite, and delete paths;
therefore the library is useful only as a project-scoped, provider-specific pack.

Admission does **not** connect Zoho MCP, install the skills globally, deploy to
Catalyst, create a mirror, or grant production credentials. A first test must
copy only the needed skill subtree into a disposable project, keep MCP disconnected
or development-scoped, and compare it with the existing deployment guidance.

Sources: [repository](https://github.com/catalystbyzoho/agent-skills),
[Apache-2.0 license](https://github.com/catalystbyzoho/agent-skills/blob/a720b7b629f7d2736a999a76683291de4f9d5a99/LICENSE),
[eval instructions](https://github.com/catalystbyzoho/agent-skills/blob/a720b7b629f7d2736a999a76683291de4f9d5a99/evals/README.md).

## Promotion order

1. Claude Code 2.1.261 permission-rule matrix in a disposable repository.
2. Codex 0.153.4 with an explicit model pin, then account/resume tests.
3. Kimi Code 0.41.0 containment and permission tests; reject the candidate if
   dangerous commands escape the external sandbox.
4. Catalyst Agent Skills only when a Catalyst deployment is a real contender;
   run its AppSail evals plus an independent no-MCP planning task first.

Until these pass, `repos.json` policy and recorded runtime states remain the
enforcement source. Registry presence is not execution readiness.
