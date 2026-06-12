---
status: draft
topic: What to always review in AI-generated code
suggested_day: Thursday
---

## Hook

AI will write confidently broken code in these five areas. Review them every time.

## Caption

AI coding tools generate plausible-looking code that fails in very specific ways.

These are the five areas where it fails most dangerously:

Authentication and authorization logic. One incorrect condition can make every resource publicly accessible. AI does not fully understand your permission model — it approximates it.

Database queries. AI defaults to the simplest query, not the correct one. N+1 patterns, missing indexes, and queries that will not survive real load are all common.

Error handling. AI wraps blocks in try/catch and considers the job done. What it rarely does is think about recovery paths, meaningful error messages, or what happens downstream when something fails silently.

Payment and billing flows. Any code that touches money deserves a second set of human eyes, every time, no exceptions.

System boundaries and API contracts. AI writes to the interface you showed it. It does not consider what breaks when that interface changes, or what systems depend on the response shape.

A useful rule of thumb: the higher the impact of a bug in a given area, the more carefully you review the AI's contribution to it.

Save this as a checklist for your next AI-assisted PR 🔖

#coderassist #aitools #codereviews #softwaredeveloper #programming #aicoding #devtips #webdev

## Image Quote

> The higher the impact of a bug, the more carefully you review what AI wrote.

## Image Prompt

Upload `assets/avatar.jpg` as a reference image in ChatGPT, then use this prompt:

Square 1:1 image. Solid dark forest green background, hex #2d7021.
White serif text (Georgia or similar), large font, left-aligned with
generous padding (~10% from left and top edges). Text reads:
"The higher the impact of a bug, the more carefully you review what AI wrote."
At the bottom center, smaller white serif text: "@coderassist".
In the bottom-right corner, place the robot character from the reference image —
small (roughly 20% of image width), full body, friendly pose, slightly floating.
No other elements — no borders, no gradients, no extra illustrations.
Clean and minimal.

## Notes

Practical safety checklist. Very saveable/shareable. Could become a carousel (one card per area) — strong candidate for a multi-slide post.
