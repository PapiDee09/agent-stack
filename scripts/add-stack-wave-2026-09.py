#!/usr/bin/env python3

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPOS_PATH = ROOT / "repos.json"
SOURCES_PATH = ROOT / "sources.json"

data = json.loads(REPOS_PATH.read_text())
repos = data["repositories"]

additions = [
    {
        "name": "VoltAgent",
        "category": "agent-framework",
        "tier": "optional",
        "upstream": "https://github.com/VoltAgent/voltagent",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
    {
        "name": "Codebase Memory MCP",
        "category": "agent-code-intelligence",
        "tier": "core",
        "upstream": "https://github.com/DeusData/codebase-memory-mcp",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
    {
        "name": "Orca",
        "category": "agent-orchestration",
        "tier": "core-specialist",
        "upstream": "https://github.com/stablyai/orca",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
    {
        "name": "Agency Agents",
        "category": "agent-skills",
        "tier": "situational",
        "upstream": "https://github.com/msitarzewski/agency-agents",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "review_required",
        "sync_policy": "auto",
    },
    {
        "name": "Google Maps Scraper",
        "category": "growth-research",
        "tier": "situational",
        "upstream": "https://github.com/omkarcloud/google-maps-scraper",
        "license": "MIT_WITH_USAGE_COMPLIANCE_NOTICE",
        "mirror_policy": "fork_or_mirror_preserve_notices",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "review_required",
        "sync_policy": "auto",
    },
    {
        "name": "Emil Kowalski Skills",
        "category": "design-engineering-skills",
        "tier": "core",
        "upstream": "https://github.com/emilkowalski/skills",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
    {
        "name": "video-use",
        "category": "agent-media",
        "tier": "core-specialist",
        "upstream": "https://github.com/browser-use/video-use",
        "license": "MIT",
        "mirror_policy": "fork_or_mirror",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
    {
        "name": "Diffusion Studio Editor",
        "category": "agent-media",
        "tier": "optional",
        "upstream": "https://github.com/diffusionstudio/editor",
        "license": "MPL-2.0_WITH_PROPRIETARY_BRAND_ASSETS",
        "mirror_policy": "mirror_with_copyleft_review_exclude_brand_assets",
        "verified": True,
        "mirror_eligibility": "selective",
        "dependency_policy": "review_required",
        "sync_policy": "review",
    },
    {
        "name": "OpenDesign",
        "category": "agent-design-system",
        "tier": "core-specialist",
        "upstream": "https://github.com/vustudio/opendesign",
        "license": "Apache-2.0_WITH_BUNDLED_MIT_SKILLS",
        "mirror_policy": "fork_or_mirror_preserve_notices",
        "verified": True,
        "mirror_eligibility": "legal",
        "dependency_policy": "safe_default",
        "sync_policy": "auto",
    },
]

by_name = {repo["name"]: repo for repo in repos}

added = 0
updated = 0

for candidate in additions:
    existing = by_name.get(candidate["name"])

    if existing is None:
        repos.append(candidate)
        by_name[candidate["name"]] = candidate
        added += 1
        print("ADD   ", candidate["name"])
        continue

    changed = False
    for key, value in candidate.items():
        if existing.get(key) != value:
            existing[key] = value
            changed = True

    if changed:
        updated += 1
        print("UPDATE", candidate["name"])
    else:
        print("KEEP  ", candidate["name"])

data["schema_version"] = "0.2"

policy = data.setdefault("policy", {})
policy["registry_dimensions"] = {
    "mirror_eligibility": [
        "legal",
        "selective",
        "private_only",
        "reference_only",
        "prohibited",
    ],
    "dependency_policy": [
        "safe_default",
        "review_required",
        "prohibited",
    ],
    "sync_policy": [
        "auto",
        "review",
        "manual",
        "none",
    ],
}

REPOS_PATH.write_text(json.dumps(data, indent=2) + "\n")

sources = {
    "schema_version": 1,
    "sources": [
        {
            "name": "Skillry",
            "category": "agent-skill-marketplace",
            "url": "https://skillry.dev/",
            "tier": "source",
            "ownership": "hosted_proprietary",
            "usage": "discover and evaluate individual reusable agent skills",
        },
        {
            "name": "AppKittie",
            "category": "mobile-product-intelligence",
            "url": "https://www.appkittie.com/",
            "tier": "core-optional-source",
            "ownership": "hosted_proprietary",
            "usage": "mobile market, competitor, onboarding, ads and ASO intelligence",
        },
        {
            "name": "Jiro",
            "category": "design-reference",
            "url": "https://jiro.build/",
            "tier": "source",
            "ownership": "hosted",
            "usage": "design prompts and implementation reference",
        },
        {
            "name": "Anim8",
            "category": "motion-production",
            "url": "https://tryanim8.com/",
            "tier": "situational-source",
            "ownership": "hosted_proprietary",
            "usage": "video to editable vector, SVG and Lottie workflows",
        },
        {
            "name": "Annnimate",
            "category": "motion-reference",
            "url": "https://annnimate.com/",
            "tier": "source",
            "ownership": "hosted_proprietary",
            "usage": "production motion component and GSAP reference",
        },
        {
            "name": "Raylight",
            "category": "creative-production",
            "url": "https://raylight.io/",
            "tier": "situational-source",
            "ownership": "hosted_proprietary",
            "usage": "browser motion and video production",
        },
        {
            "name": "Motion.so",
            "category": "creative-production-reference",
            "url": "https://motion.so/",
            "tier": "reference",
            "ownership": "hosted_proprietary",
            "usage": "autonomous motion-design workflow reference",
        },
    ],
}

if SOURCES_PATH.exists():
    current = json.loads(SOURCES_PATH.read_text())
    current_sources = current.setdefault("sources", [])
    existing = {item["name"]: item for item in current_sources}

    for item in sources["sources"]:
        if item["name"] in existing:
            existing[item["name"]].update(item)
        else:
            current_sources.append(item)

    sources = current

SOURCES_PATH.write_text(json.dumps(sources, indent=2) + "\n")

print()
print(f"Repositories added: {added}")
print(f"Repositories updated: {updated}")
print(f"Repository total: {len(repos)}")
print(f"Sources total: {len(sources['sources'])}")
