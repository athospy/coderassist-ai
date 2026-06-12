"""
Push all posts with status=ready to Buffer as scheduled Instagram updates.

Each post is scheduled for the next occurrence of its suggested_day at the
configured posting time (default 9:30 AM local time).

Image upload flow:
  1. Upload image to imgbb (free hosting) → get public URL
  2. Pass that URL to Buffer's create-update API

Usage:
    python scripts/push.py              # push all ready posts
    python scripts/push.py --dry-run    # preview without touching any API

Setup (one-time):
  1. Copy scripts/.env.example to scripts/.env and fill in credentials
  2. pip install -r scripts/requirements.txt
"""

import os
import sys
import glob
from datetime import datetime, timedelta

import frontmatter
import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

POSTS_DIR = os.path.join(os.path.dirname(__file__), "..", "posts")
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")

BUFFER_TOKEN = os.getenv("BUFFER_ACCESS_TOKEN", "")
BUFFER_PROFILE_ID = os.getenv("BUFFER_INSTAGRAM_PROFILE_ID", "")
IMGBB_KEY = os.getenv("IMGBB_API_KEY", "")
POST_HOUR = int(os.getenv("POST_HOUR", "9"))
POST_MINUTE = int(os.getenv("POST_MINUTE", "30"))

WEEKDAYS = {
    "monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3,
    "friday": 4, "saturday": 5, "sunday": 6,
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def next_occurrence(day_name):
    """Return the next future datetime for the given weekday at posting time."""
    target = WEEKDAYS.get(day_name.lower())
    if target is None:
        return None
    now = datetime.now()
    days_ahead = target - now.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    dt = now + timedelta(days=days_ahead)
    return dt.replace(hour=POST_HOUR, minute=POST_MINUTE, second=0, microsecond=0)


def post_number(filepath):
    """'posts/01-stat-shock.md' -> 1"""
    return int(os.path.basename(filepath).split("-")[0])


def find_image(num):
    """Return the first image file in assets/post-N/, or None."""
    folder = os.path.join(ASSETS_DIR, f"post-{num}")
    if not os.path.isdir(folder):
        return None
    files = [f for f in os.listdir(folder) if not f.startswith(".")]
    return os.path.join(folder, files[0]) if files else None


def extract_section(content, heading):
    """Extract the text between '## heading' and the next '## ' heading."""
    lines = content.split("\n")
    inside = False
    result = []
    for line in lines:
        if line.strip() == f"## {heading}":
            inside = True
            continue
        if inside:
            if line.startswith("## "):
                break
            result.append(line)
    return "\n".join(result).strip()


# ---------------------------------------------------------------------------
# API calls
# ---------------------------------------------------------------------------

def upload_image(image_path):
    """Upload a local image to imgbb and return the public URL."""
    with open(image_path, "rb") as f:
        resp = requests.post(
            "https://api.imgbb.com/1/upload",
            params={"key": IMGBB_KEY},
            files={"image": f},
            timeout=30,
        )
    resp.raise_for_status()
    return resp.json()["data"]["url"]


def create_buffer_update(caption, image_url, scheduled_at):
    """Schedule an Instagram update in Buffer."""
    resp = requests.post(
        "https://api.bufferapp.com/1/updates/create.json",
        data={
            "access_token": BUFFER_TOKEN,
            "profile_ids[]": BUFFER_PROFILE_ID,
            "text": caption,
            "media[photo]": image_url,
            "scheduled_at": int(scheduled_at.timestamp()),
            "now": "false",
        },
        timeout=15,
    )
    resp.raise_for_status()
    return resp.json()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def check_credentials(dry_run):
    if dry_run:
        return
    missing = []
    if not BUFFER_TOKEN:
        missing.append("BUFFER_ACCESS_TOKEN")
    if not BUFFER_PROFILE_ID:
        missing.append("BUFFER_INSTAGRAM_PROFILE_ID")
    if not IMGBB_KEY:
        missing.append("IMGBB_API_KEY")
    if missing:
        print("Error: missing credentials in scripts/.env:")
        for m in missing:
            print(f"  {m}")
        print("\nCopy scripts/.env.example to scripts/.env and fill in the values.")
        sys.exit(1)


def main():
    dry_run = "--dry-run" in sys.argv
    check_credentials(dry_run)

    post_files = sorted(glob.glob(os.path.join(POSTS_DIR, "*.md")))
    ready = [
        (path, frontmatter.load(path))
        for path in post_files
        if frontmatter.load(path).metadata.get("status") == "ready"
    ]

    if not ready:
        print("No posts with status 'ready'.")
        print("Mark a post ready first:")
        print("  python scripts/mark.py <slug> ready")
        return

    mode = "(DRY RUN — no APIs called)" if dry_run else ""
    print(f"\nPushing {len(ready)} ready post(s) to Buffer {mode}\n")

    for path, post in ready:
        num = post_number(path)
        slug = os.path.basename(path).replace(".md", "")
        day = post.metadata.get("suggested_day", "")
        caption = extract_section(post.content, "Caption")
        image_path = find_image(num)
        scheduled_at = next_occurrence(day)

        print(f"  {slug}")

        if not image_path:
            print(f"    SKIP — no image in assets/post-{num}/  (generate it in ChatGPT first)")
            print()
            continue

        if not scheduled_at:
            print(f"    SKIP — unrecognized suggested_day: '{day}'")
            print()
            continue

        print(f"    Image:     {os.path.basename(image_path)}")
        print(f"    Scheduled: {scheduled_at.strftime('%A %Y-%m-%d at %H:%M')}")
        print(f"    Caption:   {caption[:80]}{'...' if len(caption) > 80 else ''}")

        if dry_run:
            print()
            continue

        try:
            print("    Uploading image to imgbb...", end=" ", flush=True)
            image_url = upload_image(image_path)
            print("done")

            print("    Scheduling in Buffer...", end=" ", flush=True)
            create_buffer_update(caption, image_url, scheduled_at)
            print("queued")

        except requests.HTTPError as e:
            print(f"\n    ERROR {e.response.status_code}: {e.response.text[:200]}")
        except Exception as e:
            print(f"\n    ERROR: {e}")

        print()


if __name__ == "__main__":
    main()
