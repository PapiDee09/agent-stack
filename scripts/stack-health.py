#!/usr/bin/env python3

import hashlib
import json
import subprocess
from pathlib import Path
from urllib.parse import urlparse

REGISTRY = Path("repos.json")
STATE = Path("stack-state.json")

LICENSE_FILES = (
    "LICENSE",
    "LICENSE.md",
    "LICENSE.txt",
    "COPYING",
    "COPYING.md",
    "NOTICE",
    "ENTERPRISE-LICENSE.md",
)


def run(cmd, timeout=30):
    try:
        p = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return p.returncode, p.stdout.strip(), p.stderr.strip()
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def gh_json(args):
    code, out, err = run(["gh", *args])
    if code != 0:
        return None

    try:
        return json.loads(out)
    except json.JSONDecodeError:
        return None


def slug(url):
    return urlparse(url).path.strip("/").removesuffix(".git")


def file_hash(repo_slug, path):
    data = gh_json([
        "api",
        f"repos/{repo_slug}/contents/{path}",
        "-H",
        "Accept: application/vnd.github.raw+json",
    ])

    if data is None:
        return None

    if isinstance(data, str):
        content = data
    else:
        content = json.dumps(data, sort_keys=True)

    return hashlib.sha256(content.encode()).hexdigest()


def main():
    registry = json.loads(REGISTRY.read_text())
    previous = {}

    if STATE.exists():
        previous = json.loads(STATE.read_text()).get("repositories", {})

    current = {}
    drift = []

    for repo in registry["repositories"]:
        upstream = slug(repo["upstream"])

        info = gh_json([
            "api",
            f"repos/{upstream}",
        ])

        if not info:
            old = previous.get(repo["name"])

            if old:
                current[repo["name"]] = old
                print(
                    f"STALE        {repo['name']:<30} "
                    "GitHub request failed; preserved previous state"
                )
            else:
                print(
                    f"BROKEN       {repo['name']:<30} "
                    "GitHub request failed; no previous state"
                )

            continue

        branch = info.get("default_branch")

        commit = gh_json([
            "api",
            f"repos/{upstream}/commits/{branch}",
        ]) if branch else None

        sha = commit.get("sha") if commit else None

        hashes = {}

        for filename in LICENSE_FILES:
            h = file_hash(upstream, filename)
            if h:
                hashes[filename] = h

        old = previous.get(repo["name"], {})
        old_hashes = old.get("license_hashes", {})

        changed = sorted(
            name
            for name, digest in hashes.items()
            if name in old_hashes
            and old_hashes[name] != digest
        )

        added = sorted(
            name
            for name in hashes
            if name not in old_hashes
            and old_hashes
        )

        removed = sorted(
            name
            for name in old_hashes
            if name not in hashes
        )

        if changed or added or removed:
            drift.append({
                "name": repo["name"],
                "changed": changed,
                "added": added,
                "removed": removed,
            })

        current[repo["name"]] = {
            "upstream": upstream,
            "tier": repo.get("tier"),
            "license": repo.get("license"),
            "mirror_policy": repo.get("mirror_policy"),
            "upstream_commit": sha,
            "license_hashes": hashes,
        }

        print(
            f"OK           {repo['name']:<30} "
            f"{sha[:10] if sha else 'unknown'}"
        )

    state = {
        "schema_version": 1,
        "repositories": current,
    }

    STATE.write_text(json.dumps(state, indent=2) + "\n")

    print()
    print("STACK HEALTH")
    print("=" * 60)
    print(f"Registry entries      {len(registry['repositories'])}")
    print(f"State entries         {len(current)}")
    print(f"License drift         {len(drift)}")

    if drift:
        print()
        print("LICENSE REVIEW REQUIRED")

        for item in drift:
            details = []

            if item["changed"]:
                details.append(
                    "changed=" + ",".join(item["changed"])
                )
            if item["added"]:
                details.append(
                    "added=" + ",".join(item["added"])
                )
            if item["removed"]:
                details.append(
                    "removed=" + ",".join(item["removed"])
                )

            print(
                f"REVIEW       {item['name']:<30} "
                + " ".join(details)
            )
    elif previous:
        print("License state         CLEAN")
    else:
        print("License state         BASELINE CREATED")


if __name__ == "__main__":
    main()
