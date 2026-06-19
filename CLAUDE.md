# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Content management for the Instagram account [@coderassist](https://www.instagram.com/coderassist/). The account targets software developers with advice focused on AI tools and developer productivity. There is no application code — everything here is markdown content and image assets.

## Structure

- `posts/` — one markdown file per post, numbered sequentially (`01-stat-shock.md`, `02-vibe-coding.md`, etc.)
- `assets/` — source images and generated post images.
  - `assets/avatar.jpg` — the robot mascot used as a reference image in every ChatGPT image generation
  - `assets/canvas1–8.png` — existing carousel cards from an older blog-post series
  - `assets/post-N/` — generated images for each post, created after image prompt is run
- `brand/style-guide.md` — visual identity, the two image prompt templates (Standard and Featured), and the hashtag bank
- `content-calendar.md` — weekly posting schedule and backlog of future post ideas

## Post file format

Each file in `posts/` follows this structure:

```
---
status: draft | ready | published
topic: short description
suggested_day: day of week
---

## Hook         ← scroll-stopping first line for the caption
## Caption      ← full Instagram text including hashtags
## Hashtags     ← repeated for quick copy
## Image Quote  ← single sentence to render on the green card
## Image Prompt ← ready-to-paste ChatGPT prompt (includes avatar upload instruction)
## Notes        ← sources, repurpose ideas, carousel candidates
```

## Image generation workflow

1. Open ChatGPT, upload `assets/avatar.jpg` as a reference image.
2. Paste the `## Image Prompt` from the post file.
3. Save the output to `assets/post-N/` where N matches the post number.

The generated image for post 01 (`assets/post-1/`) is the visual reference for what the brand looks like in practice.

## Brand essentials

- Background: solid dark forest green `#2d7021`
- Text: white serif (Georgia-style), large, left-aligned
- Handle: `@coderassist` centered at bottom
- Robot mascot: bottom-right corner (Standard layout) or right half (Featured layout for engagement posts)
- One sentence per image card — the caption carries the full content

## Adding new posts

Number sequentially from the last existing post. Use `brand/style-guide.md` as the source of truth for the image prompt template — paste it, insert the `## Image Quote` text, and the prompt is ready.

## Publishing workflow

Posts are scheduled via the **Buffer MCP server** (`https://mcp.buffer.com/mcp`), called directly from Claude Code. Do not use `scripts/push.py` — it targets Buffer's legacy API which no longer accepts new apps.

Full details in `internal-docs/publishing-workflow.md`. Short version:

1. Generate image in ChatGPT (upload `assets/avatar.jpg`, paste `## Image Prompt`) → save to `assets/post-N/`
2. Copy image to `/tmp/postN.png` (avoids spaces in filename), upload to imgbb via curl
3. Call `mcp__buffer__create_post` with the imgbb URL, caption, channel ID `6a2d755d38b5579345906746`, and `dueAt` in ISO 8601 Chicago time
4. `python scripts/mark.py <slug> ready` after scheduling; `published` after it goes live

Scripts still useful:
- `python scripts/status.py` — dashboard of all posts and their status
- `python scripts/mark.py <slug> <status>` — flip a post's status field
