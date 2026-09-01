#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PATH = ROOT / "repos.json"

data = json.loads(PATH.read_text())
repos = data["repositories"]

REVIEW_LICENSE_MARKERS = (
    "PROPRIETARY",
    "CUSTOM",
    "NONCOMMERCIAL",
    "NO_REDISTRIBUTION",
    "AGPL",
    "GPL",
    "MPL",
    "SUSTAINABLE",
    "SOURCE_AVAILABLE",
    "COMMERCIAL",
    "MODEL_TERMS",
    "THIRD_PARTY_TERMS",
    "WATERMARK",
)

REVIEW_POLICY_MARKERS = (
    "reference_only",
    "review",
    "selective",
    "code_mirror_only",
    "special_usage",
    "private_internal",
)

SAFE_LICENSE_PREFIXES = (
    "MIT",
    "Apache-2.0",
    "BSD-2-Clause",
    "BSD-3-Clause",
    "PostgreSQL",
)

SAFE_EXCEPTIONS = {
    "ThreeUI",
}


def dependency_policy(repo):
    name = repo["name"]
    license_name = str(repo.get("license", ""))
    mirror_policy = str(repo.get("mirror_policy", ""))

    if name in SAFE_EXCEPTIONS:
        return "safe_default"

    if any(marker in license_name for marker in REVIEW_LICENSE_MARKERS):
        return "review_required"

    if any(marker in mirror_policy for marker in REVIEW_POLICY_MARKERS):
        return "review_required"

    if license_name == "MIT_OR_APACHE-2.0":
        return "safe_default"

    if license_name.startswith(SAFE_LICENSE_PREFIXES):
        return "safe_default"

    return "review_required"


def mirror_eligibility(repo):
    policy = str(repo.get("mirror_policy", ""))

    if "no_redistribution" in policy:
        return "reference_only"

    if "reference_only" in policy:
        return "reference_only"

    if "private_internal" in policy:
        return "private_only"

    if (
        "selective" in policy
        or "code_mirror_only" in policy
        or "core_only" in policy
    ):
        return "selective"

    return "legal"


def sync_policy(repo):
    dependency = repo["dependency_policy"]
    eligibility = repo["mirror_eligibility"]
    mirror_policy = str(repo.get("mirror_policy", ""))

    if eligibility == "reference_only":
        return "none"

    if eligibility in {"selective", "private_only"}:
        return "review"

    if dependency == "review_required":
        return "review"

    if "fork_or_mirror" in mirror_policy:
        return "auto"

    return "manual"


changed = 0

for repo in repos:
    before = dict(repo)

    repo.setdefault(
        "dependency_policy",
        dependency_policy(repo),
    )

    repo.setdefault(
        "mirror_eligibility",
        mirror_eligibility(repo),
    )

    repo.setdefault(
        "sync_policy",
        sync_policy(repo),
    )

    if repo != before:
        changed += 1

PATH.write_text(json.dumps(data, indent=2) + "\n")

print(f"Repositories: {len(repos)}")
print(f"Backfilled: {changed}")
print(
    "Safe default:",
    sum(
        r["dependency_policy"] == "safe_default"
        for r in repos
    ),
)
print(
    "Review required:",
    sum(
        r["dependency_policy"] == "review_required"
        for r in repos
    ),
)
print(
    "Prohibited:",
    sum(
        r["dependency_policy"] == "prohibited"
        for r in repos
    ),
)
