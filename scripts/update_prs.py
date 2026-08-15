#!/usr/bin/env python3
"""Refresh the recent-contributions block in README.md from the GitHub API."""

import json
import os
import re
import urllib.request

USER = "pdd23001"
START = "<!-- RECENT:START -->"
END = "<!-- RECENT:END -->"
LIMIT = 5
# One-off hackathon submissions with placeholder titles; not worth surfacing.
EXCLUDE_REPOS = {
    "ShaiVerma/Algorand_Hack",
    "Hackers-of-Tomorrow/5-idiots-MIT",
}
QUERY = (
    f"https://api.github.com/search/issues"
    f"?q=author:{USER}+type:pr+is:merged&sort=updated&order=desc&per_page=30"
)


def fetch():
    req = urllib.request.Request(QUERY, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)["items"]


def render(items):
    lines = ["| Pull request | Repository | Merged |", "| :-- | :-- | :-- |"]
    shown = 0
    for item in items:
        repo = item["repository_url"].split("/repos/")[1]
        if repo in EXCLUDE_REPOS or shown >= LIMIT:
            continue
        title = item["title"].replace("|", "\\|")
        merged = (item.get("closed_at") or "")[:10]
        lines.append(f"| [{title}]({item['html_url']}) | `{repo}` | {merged} |")
        shown += 1
    return "\n".join(lines)


def main():
    with open("README.md", encoding="utf-8") as fh:
        readme = fh.read()

    block = f"{START}\n{render(fetch())}\n{END}"
    pattern = re.escape(START) + ".*?" + re.escape(END)
    updated = re.sub(pattern, lambda _: block, readme, flags=re.S)

    if updated != readme:
        with open("README.md", "w", encoding="utf-8") as fh:
            fh.write(updated)
        print("README.md updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
