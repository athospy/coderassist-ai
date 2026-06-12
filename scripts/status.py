"""
Show the current status of all posts.

Usage:
    python scripts/status.py
    python scripts/status.py --ready   # show only posts with status=ready
"""

import os
import sys
import glob

import frontmatter

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "posts")
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")


def post_number(filename):
    """'01-stat-shock.md' -> 1"""
    return int(os.path.basename(filename).split("-")[0])


def has_image(num):
    folder = os.path.join(ASSETS_DIR, f"post-{num}")
    if not os.path.isdir(folder):
        return False
    return any(f for f in os.listdir(folder) if not f.startswith("."))


def main():
    filter_ready = "--ready" in sys.argv

    post_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    if not post_files:
        print("No post files found in posts/")
        return

    print(f"\n{'POST':<30} {'STATUS':<12} {'DAY':<12} {'IMAGE'}")
    print("-" * 62)

    shown = 0
    for path in post_files:
        post = frontmatter.load(path)
        status = post.metadata.get("status", "unknown")

        if filter_ready and status != "ready":
            continue

        num = post_number(path)
        name = os.path.basename(path).replace(".md", "")
        day = post.metadata.get("suggested_day", "—")
        image = "✓" if has_image(num) else "✗"

        print(f"{name:<30} {status:<12} {day:<12} {image}")
        shown += 1

    if shown == 0:
        print("  (no matching posts)")
    print()


if __name__ == "__main__":
    main()
