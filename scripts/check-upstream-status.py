#!/usr/bin/env python3

import argparse
import concurrent.futures
import json
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

REGISTRY = Path("repos.json")
SAFE_AUTO_POLICIES = {"fork_or_mirror"}
MAX_WORKERS = 8


def run(cmd, timeout=20):
    try:
        result = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except subprocess.TimeoutExpired:
        return 124, "", "timeout"


def gh_json(args):
    code, out, err = run(["gh", *args])

    if code != 0:
        return None, err or out

    try:
        return json.loads(out), None
    except json.JSONDecodeError:
        return None, f"invalid JSON: {out[:120]}"


def upstream_slug(url):
    parsed = urlparse(url)
    return parsed.path.strip("/").removesuffix(".git")


def repo_name_from_slug(slug):
    return slug.split("/")[-1]


def status_for(repo, owner):
    name = repo["name"]
    policy = repo.get("mirror_policy", "")
    upstream = upstream_slug(repo["upstream"])
    target_name = repo_name_from_slug(upstream)
    target = f"{owner}/{target_name}"

    if policy not in SAFE_AUTO_POLICIES:
        return {
            "name": name,
            "status": "REVIEW_REQUIRED",
            "detail": policy,
        }

    target_data, error = gh_json(["api", f"repos/{target}"])
    if error:
        return {
            "name": name,
            "status": "BROKEN",
            "detail": f"target unavailable: {error}",
        }

    if not target_data.get("fork"):
        return {
            "name": name,
            "status": "BROKEN",
            "detail": "target is not a fork",
        }

    parent = (target_data.get("parent") or {}).get("full_name")
    if not parent:
        return {
            "name": name,
            "status": "BROKEN",
            "detail": "fork parent unavailable",
        }

    if parent.lower() != upstream.lower():
        return {
            "name": name,
            "status": "BROKEN",
            "detail": f"parent mismatch: {parent}",
        }

    fork_branch = target_data.get("default_branch")
    parent_data, error = gh_json(["api", f"repos/{upstream}"])

    if error:
        return {
            "name": name,
            "status": "BROKEN",
            "detail": f"upstream unavailable: {error}",
        }

    upstream_branch = parent_data.get("default_branch")

    if not fork_branch or not upstream_branch:
        return {
            "name": name,
            "status": "BROKEN",
            "detail": "missing default branch",
        }

    compare = (
        f"repos/{upstream}/compare/"
        f"{upstream_branch}...{owner}:{fork_branch}"
    )

    comparison, error = gh_json(["api", compare])

    if error:
        return {
            "name": name,
            "status": "BROKEN",
            "detail": f"compare failed: {error}",
        }

    ahead = int(comparison.get("ahead_by", 0))
    behind = int(comparison.get("behind_by", 0))

    if ahead == 0 and behind == 0:
        status = "CURRENT"
    elif ahead == 0 and behind > 0:
        status = "BEHIND"
    else:
        status = "DIVERGED"

    return {
        "name": name,
        "status": status,
        "detail": f"ahead={ahead} behind={behind}",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", default="PapiDee09")
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    data = json.loads(REGISTRY.read_text())

    repos = [
        repo
        for repo in data["repositories"]
        if repo.get("verified")
        and (
            args.all
            or repo.get("mirror_policy") in SAFE_AUTO_POLICIES
        )
    ]

    print(f"Checking {len(repos)} repositories...")
    print()

    results = []

    with concurrent.futures.ThreadPoolExecutor(
        max_workers=MAX_WORKERS
    ) as executor:

        futures = {
            executor.submit(status_for, repo, args.owner): repo
            for repo in repos
        }

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            results.append(result)

            print(
                f"{result['status']:<12} "
                f"{result['name']:<32} "
                f"{result['detail']}"
            )

    counts = {}

    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1

    print()
    print("SUMMARY")
    print("=" * 50)

    for status in (
        "CURRENT",
        "BEHIND",
        "DIVERGED",
        "BROKEN",
        "REVIEW_REQUIRED",
    ):
        print(f"{status:<16} {counts.get(status, 0)}")

    if counts.get("DIVERGED", 0) or counts.get("BROKEN", 0):
        sys.exit(2)


if __name__ == "__main__":
    main()
