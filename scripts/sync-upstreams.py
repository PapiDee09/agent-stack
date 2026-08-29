#!/usr/bin/env python3

import argparse
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

REGISTRY = Path("repos.json")
SAFE_POLICIES = {"fork_or_mirror"}


def run(cmd, timeout=60):
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
    code, out, err = run(["gh", *args], timeout=30)
    if code != 0:
        return None, err or out

    try:
        return json.loads(out), None
    except json.JSONDecodeError:
        return None, "invalid JSON returned by GitHub CLI"


def slug(url):
    parsed = urlparse(url)
    return parsed.path.strip("/").removesuffix(".git")


def inspect(repo, owner):
    name = repo["name"]
    upstream = slug(repo["upstream"])
    target_repo = upstream.split("/")[-1]
    target = f"{owner}/{target_repo}"

    target_data, err = gh_json(["api", f"repos/{target}"])
    if err:
        return {
            "name": name,
            "target": target,
            "state": "BROKEN",
            "detail": err,
        }

    if not target_data.get("fork"):
        return {
            "name": name,
            "target": target,
            "state": "BLOCKED",
            "detail": "target is not a fork",
        }

    parent = (target_data.get("parent") or {}).get("full_name")

    if not parent or parent.lower() != upstream.lower():
        return {
            "name": name,
            "target": target,
            "state": "BLOCKED",
            "detail": f"parent={parent}",
        }

    fork_branch = target_data.get("default_branch")

    upstream_data, err = gh_json(["api", f"repos/{upstream}"])
    if err:
        return {
            "name": name,
            "target": target,
            "state": "BROKEN",
            "detail": err,
        }

    upstream_branch = upstream_data.get("default_branch")

    if not fork_branch or not upstream_branch:
        return {
            "name": name,
            "target": target,
            "state": "BROKEN",
            "detail": "missing default branch",
        }

    endpoint = (
        f"repos/{upstream}/compare/"
        f"{upstream_branch}...{owner}:{fork_branch}"
    )

    comparison, err = gh_json(["api", endpoint])
    if err:
        return {
            "name": name,
            "target": target,
            "state": "BROKEN",
            "detail": err,
        }

    ahead = int(comparison.get("ahead_by", 0))
    behind = int(comparison.get("behind_by", 0))

    if ahead == 0 and behind == 0:
        state = "CURRENT"
    elif ahead == 0 and behind > 0:
        state = "SYNC_READY"
    else:
        state = "DIVERGED"

    return {
        "name": name,
        "target": target,
        "branch": fork_branch,
        "state": state,
        "ahead": ahead,
        "behind": behind,
        "detail": f"ahead={ahead} behind={behind}",
    }


def sync(item):
    code, out, err = run([
        "gh",
        "repo",
        "sync",
        item["target"],
        "-b",
        item["branch"],
    ])

    if code == 0:
        return True, out or "synced"

    return False, err or out or "sync failed"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", default="PapiDee09")
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Actually synchronize safe behind-only forks",
    )
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text())

    repos = [
        repo
        for repo in data["repositories"]
        if repo.get("verified")
        and repo.get("mirror_policy") in SAFE_POLICIES
    ]

    print(
        f"{'SYNCING' if args.apply else 'PLANNING'} "
        f"{len(repos)} safe-policy repositories..."
    )
    print()

    results = []

    for repo in repos:
        item = inspect(repo, args.owner)
        results.append(item)

        if item["state"] != "CURRENT":
            print(
                f"{item['state']:<12} "
                f"{item['name']:<30} "
                f"{item['detail']}"
            )

    ready = [r for r in results if r["state"] == "SYNC_READY"]
    diverged = [r for r in results if r["state"] == "DIVERGED"]
    broken = [
        r for r in results
        if r["state"] in {"BROKEN", "BLOCKED"}
    ]

    print()
    print("PLAN SUMMARY")
    print("=" * 56)
    print(f"CURRENT          {sum(r['state'] == 'CURRENT' for r in results)}")
    print(f"SYNC_READY       {len(ready)}")
    print(f"DIVERGED         {len(diverged)}")
    print(f"BROKEN/BLOCKED   {len(broken)}")

    if diverged or broken:
        print()
        print("Refusing sync: unsafe repository state detected.")
        sys.exit(2)

    if not args.apply:
        print()
        print("Dry plan only. Re-run with --apply to synchronize.")
        return

    if not ready:
        print()
        print("Everything is already current.")
        return

    print()
    print("SYNC")
    print("=" * 56)

    failures = 0

    for item in ready:
        ok, detail = sync(item)

        if ok:
            print(
                f"SYNCED       {item['name']:<30} "
                f"+{item['behind']} upstream commit(s)"
            )
        else:
            failures += 1
            print(
                f"FAILED       {item['name']:<30} "
                f"{detail}"
            )

    print()

    if failures:
        print(f"Completed with {failures} failure(s).")
        sys.exit(3)

    print(f"Successfully synchronized {len(ready)} repositories.")


if __name__ == "__main__":
    main()
