# Next Session — Connect Buffer and push the first @coderassist post

## What this project is

Instagram content automation for @coderassist (developer audience, AI tools niche).
All 10 posts are written and ready in `posts/`. One image exists (`assets/post-1/`).
Python automation scripts are built in `scripts/`. Landing page is live.

## What was done (sessions 1 + 2)

### Session 1 — Scripts
- `python scripts/status.py` — dashboard: shows all posts, status, day, image present
- `python scripts/mark.py <slug> <status>` — flip a post's frontmatter status
- `python scripts/push.py --dry-run` — preview what would go to Buffer (safe, no API calls)
- `python scripts/push.py` — upload image to imgbb → schedule in Buffer

### Session 2 — Credentials + Landing Page
- [x] imgbb account created, API key generated → saved in `scripts/.env`
- [x] Formspree account created, form `xaqzloqy` wired into `landing/index.html`
- [x] Landing page built → `landing/index.html` (Matrix rain, neon green, Orbitron font)
- [x] Landing page FTP'd to `apps.santiagomorel.dev/coderassist`
- [x] @coderassist switched to Professional/Creator Instagram account
- [x] Instagram linked to a Facebook Page

## What still needs to happen (full checklist)

### Step 1 — Instagram Business account ✓ DONE
- [x] Switched @coderassist to Professional/Creator account
- [x] Linked to a Facebook Page

### Step 2 — Buffer account + API token ← START HERE
- [ ] Go to https://buffer.com → sign up free
- [ ] Connect the Instagram account (requires Step 1 complete)
- [ ] Get **access token**: https://buffer.com/developers/api/oauth → "Get Access Token" flow
- [ ] Get **Instagram profile ID**:
  ```
  GET https://api.bufferapp.com/1/profiles.json?access_token=YOUR_TOKEN
  ```
  Find entry where `service == "instagram"` → copy its `id`
- [ ] Add both to `scripts/.env`:
  ```
  BUFFER_ACCESS_TOKEN=
  BUFFER_INSTAGRAM_PROFILE_ID=
  ```

### Step 3 — Push post 01 (01-stat-shock)
Image already exists in `assets/post-1/`
```bash
python scripts/mark.py 01-stat-shock ready
python scripts/push.py --dry-run    # verify caption + date look right
python scripts/push.py              # real push → imgbb upload + Buffer queue
```

### Step 4 — Queue the Week 1 schedule
Content calendar order (from `content-calendar.md`):
| Day | Post |
|-----|------|
| Monday | 07-90-percent-engineers |
| Tuesday | 04-prompt-engineering |
| Wednesday | 03-tool-comparison |
| Thursday | 01-stat-shock |
| Friday | 02-vibe-coding |
| Saturday | 05-junior-vs-senior |
| Sunday | 10-engagement |

For each: generate image in ChatGPT (upload `assets/avatar.jpg`, paste `## Image Prompt`)
→ save to `assets/post-N/` → mark ready → push.

## Current state of scripts/.env

```
IMGBB_API_KEY=7a4ca576c9a6619165c204cc516f9657   ✓ done
BUFFER_ACCESS_TOKEN=                              ← needed
BUFFER_INSTAGRAM_PROFILE_ID=                     ← needed
POST_HOUR=9
POST_MINUTE=30
```

## MCP Playwright note

Playwright MCP is registered (`claude mcp add playwright npx @playwright/mcp@latest`).
Available in every new session — Claude can open a browser for the Buffer setup walkthrough.

## Prompt to paste

> We're working on the @coderassist Instagram posting automation in `/Users/santiagomorel/site/coderassist-ai`.
>
> **Done so far:**
> - 10 posts written in `posts/`, scripts built in `scripts/`
> - `scripts/.env` has `IMGBB_API_KEY` filled in
> - Landing page live at `apps.santiagomorel.dev/coderassist` (Matrix rain design)
> - Formspree newsletter wired in (endpoint `xaqzloqy`, → santi.morel@gmail.com)
> - @coderassist switched to Professional/Creator + linked to a Facebook Page ✓
>
> **Next steps (in order):**
> 1. Sign up for Buffer (buffer.com free), connect the @coderassist Instagram account, get the access token + Instagram profile ID, add both to `scripts/.env`
> 2. Run `python scripts/push.py --dry-run` then the real push for post `01-stat-shock` (image already in `assets/post-1/`)
>
> MCP Playwright is registered — use it to walk me through Buffer setup interactively.
> Check `NEXT-SESSION.md` for the full checklist and current `.env` state.
