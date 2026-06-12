"""
Update the status field in a post's frontmatter.

Usage:
    python scripts/mark.py <slug> <status>

Arguments:
    slug    Partial or full post name, e.g. "01-stat-shock" or "stat-shock"
    status  One of: draft | ready | published

Examples:
    python scripts/mark.py 01-stat-shock ready
    python scripts/mark.py stat-shock published
"""

import os
import re
import sys
import glob

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "posts")
VALID_STATUSES = {"draft", "ready", "published"}


def find_post(slug):
    exact = os.path.join(POSTS_DIR, f"{slug}.md")
    if os.path.isfile(exact):
        return exact

    all_posts = glob.glob(os.path.join(POSTS_DIR, "*.md"))
    matches = [p for p in all_posts if slug in os.path.basename(p)]

    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        names = [os.path.basename(p) for p in matches]
        print(f"Ambiguous slug '{slug}' — matches: {names}")
        sys.exit(1)
    return None


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    slug, new_status = sys.argv[1], sys.argv[2].lower()

    if new_status not in VALID_STATUSES:
        print(f"Invalid status '{new_status}'. Must be one of: {', '.join(sorted(VALID_STATUSES))}")
        sys.exit(1)

    path = find_post(slug)
    if not path:
        print(f"No post found matching '{slug}'")
        sys.exit(1)

    with open(path, "r") as f:
        content = f.read()

    # Extract old status before replacing (for the confirmation message)
    match = re.search(r"^status:\s*(\S+)", content, re.MULTILINE)
    old_status = match.group(1) if match else "unknown"

    # Replace only the status line inside the frontmatter block
    updated = re.sub(r"^(status:\s*)\S+", rf"\g<1>{new_status}", content, flags=re.MULTILINE)

    if updated == content:
        print(f"Status is already '{new_status}' — no change made.")
        return

    with open(path, "w") as f:
        f.write(updated)

    name = os.path.basename(path)
    print(f"{name}: {old_status} → {new_status}")


if __name__ == "__main__":
    main()
