---
status: draft
topic: How to write better AI prompts
suggested_day: Tuesday
---

## Hook

Your AI writes bad code because your prompts are bad. Here's how to fix that.

## Caption

Most developers prompt AI the way they text a friend.

"write a login function"
"fix this bug"
"make it faster"

Then they wonder why the output is generic, wrong, or misses the architecture entirely.

Senior developers prompt differently. Here is what changes:

1. Context first.
   "I'm building a Node.js REST API with Express and Prisma. The auth layer uses JWTs stored in httpOnly cookies."

2. State the constraints.
   "Must handle concurrent requests. No third-party auth libraries."

3. Specify the output format.
   "Return TypeScript. Add JSDoc. No inline comments in the body."

4. Tell it what not to do.
   "Do not refactor anything outside the auth module."

5. Ask for reasoning.
   "Explain the trade-offs of your approach before writing the code."

Better prompts do not just produce better code.
They reveal whether you actually understand the problem.

Save this 🔖 and use it on your next AI-assisted feature.

#promptengineering #aitools #coderassist #developer #chatgpt #claudeai #softwaredeveloper #codinglife

## Image Quote

> Better prompts do not just produce better code. They reveal whether you understand the problem.

## Image Prompt

Upload `assets/avatar.jpg` as a reference image in ChatGPT, then use this prompt:

Square 1:1 image. Solid dark forest green background, hex #2d7021.
White serif text (Georgia or similar), large font, left-aligned with
generous padding (~10% from left and top edges). Text reads:
"Better prompts do not just produce better code. They reveal whether you understand the problem."
At the bottom center, smaller white serif text: "@coderassist".
In the bottom-right corner, place the robot character from the reference image —
small (roughly 20% of image width), full body, friendly pose, slightly floating.
No other elements — no borders, no gradients, no extra illustrations.
Clean and minimal.

## Notes

Evergreen content. Works well paired with a carousel showing a before/after prompt example. Can be repurposed from blog content later.
