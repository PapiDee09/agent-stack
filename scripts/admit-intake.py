#!/usr/bin/env python3

import argparse
import json
from pathlib import Path

REGISTRY = Path("repos.json")
DEFAULT_INTAKE = Path("intake/2026-09-16-ready.json")


def normalize_upstream(url: str) -> str:
    return url.rstrip("/").removesuffix(".git").lower()


def main():
    parser = argparse.ArgumentParser(
        description="Safely admit staged intake candidates into repos.json without duplication."
    )
    parser.add_argument("--intake", default=str(DEFAULT_INTAKE))
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    registry = json.loads(REGISTRY.read_text())
    intake = json.loads(Path(args.intake).read_text())

    existing_names = {repo["name"].lower() for repo in registry["repositories"]}
    existing_upstreams = {
        normalize_upstream(repo["upstream"]) for repo in registry["repositories"]
    }

    additions = []
    skipped = []

    for candidate in intake.get("candidates", []):
        name_key = candidate["name"].lower()
        upstream_key = normalize_upstream(candidate["upstream"])

        if name_key in existing_names:
            skipped.append((candidate["name"], "name already present"))
            continue

        if upstream_key in existing_upstreams:
            skipped.append((candidate["name"], "upstream already present"))
            continue

        entry = {
            "name": candidate["name"],
            "category": candidate["category"],
            "tier": candidate["tier"],
            "upstream": candidate["upstream"],
            "license": candidate["license"],
            "mirror_policy": candidate["mirror_policy"],
            "verified": True,
            "dependency_policy": candidate.get("dependency_policy", "review_required"),
            "mirror_eligibility": candidate.get("mirror_eligibility", "legal"),
            "sync_policy": candidate.get("sync_policy", "review"),
        }
        additions.append(entry)
        existing_names.add(name_key)
        existing_upstreams.add(upstream_key)

    print(f"Registry entries before: {len(registry['repositories'])}")
    print(f"Candidates in intake:    {len(intake.get('candidates', []))}")
    print(f"New entries:             {len(additions)}")
    print(f"Duplicates skipped:      {len(skipped)}")
    print()

    for entry in additions:
        print(f"ADD   {entry['name']} — {entry['upstream']} — sync={entry['sync_policy']}")

    for name, reason in skipped:
        print(f"SKIP  {name} — {reason}")

    if not args.apply:
        print()
        print("Dry plan only. Re-run with --apply to update repos.json.")
        return

    registry["repositories"].extend(additions)
    REGISTRY.write_text(json.dumps(registry, indent=2) + "\n")

    print()
    print(f"Updated repos.json: {len(registry['repositories'])} entries total.")


if __name__ == "__main__":
    main()
