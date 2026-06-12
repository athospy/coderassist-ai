# CoderAssist Instagram — Brand Style Guide

## Visual Identity

All post images follow a single consistent format derived from the existing canvas posts.

| Property        | Value                                      |
|-----------------|--------------------------------------------|
| Format          | Square 1:1 (1080×1080 px recommended)      |
| Background      | Solid dark forest green — hex `#2d7021`    |
| Text color      | White                                      |
| Font style      | Serif (Georgia or similar), large size     |
| Text alignment  | Left-aligned, generous padding (~10%)      |
| Handle          | `@coderassist` — centered, bottom          |
| Decorations     | None — no icons, borders, gradients        |

## Avatar / Mascot

File: `assets/avatar.jpg`

The robot character is the face of the account. Key traits:
- Teal/light blue rectangular head with rounded corners
- Large eyes with amber/yellow rims and dark pupils
- White feathered wings at the shoulders
- Amber/yellow body with a small glowing chest window
- Friendly, curious expression — 3D painted figurine style

**Always upload `assets/avatar.jpg` as a reference image in ChatGPT before generating.** This anchors the character so it stays consistent across posts.

## Image Card — ChatGPT Base Prompt

Two layout modes. Use **Standard** for most posts, **Featured** for engagement/milestone posts.

### Standard layout (robot as signature in corner)

Upload `avatar.jpg` as reference, then use this prompt. Replace `[QUOTE]` with the card text.

```
Square 1:1 image. Solid dark forest green background, hex #2d7021.
White serif text (Georgia or similar), large font, left-aligned with
generous padding (~10% from left and top edges). Text reads: "[QUOTE]"
At the bottom center, smaller white serif text: "@coderassist".
In the bottom-right corner, place the robot character from the reference image —
small (roughly 20% of image width), full body, friendly pose, slightly floating.
No other elements — no borders, no gradients, no extra illustrations.
Clean and minimal.
```

### Featured layout (robot as co-star, for polls and milestone posts)

Upload `avatar.jpg` as reference, then use this prompt.

```
Square 1:1 image. Solid dark forest green background, hex #2d7021.
Right half: the robot character from the reference image, centered vertically,
full body, friendly and expressive pose — roughly 40% of image width.
Left half: white serif text (Georgia or similar), left-aligned with generous padding.
Text reads: "[QUOTE]"
At the bottom center, smaller white serif text: "@coderassist".
No borders, no gradients, no extra illustrations. Clean and minimal.
```

## Voice & Tone

- Thoughtful, direct, slightly opinionated.
- Complete sentences. No clickbait.
- The image carries one insight; the caption delivers the full value.
- Audience: software developers from junior to senior, interested in AI tools.

## Avatar

File: `assets/avatar.jpg` — teal/yellow robot with wings. Used for profile picture.

## Content Mix (target per month)

| Type                        | Frequency |
|-----------------------------|-----------|
| AI tool tips / comparisons  | 40%       |
| Developer career / mindset  | 25%       |
| Quotes from blog posts      | 20%       |
| Engagement / polls          | 15%       |

## Hashtag Banks

**AI tools:** `#aitools #aicoding #claudeai #cursor #githubcopilot #claudecode #aicodingtools`

**Developer life:** `#softwaredeveloper #developerlife #programmer #codinglife #programminglife`

**Career:** `#developercareer #techcareer #juniordev #seniordev #softwareengineering`

**Engagement:** `#coderassist #webdev #tech #coding`
