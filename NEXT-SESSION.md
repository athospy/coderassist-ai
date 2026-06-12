# Next Session — Connect Buffer + imgbb and post the first @coderassist post

## What this project is

Instagram content automation for @coderassist (developer audience, AI tools niche).
All 10 posts are written and ready in `posts/`. One image exists (`assets/post-1/`).
Python automation scripts are built in `scripts/`. We just need credentials.

## What was built last session

Three scripts in `scripts/`:

- `python scripts/status.py` — dashboard: shows all posts, status, day, image present
- `python scripts/mark.py <slug> <status>` — flip a post's frontmatter status (draft/ready/published)
- `python scripts/push.py --dry-run` — preview what would go to Buffer (safe, no API calls)
- `python scripts/push.py` — upload image to imgbb → schedule in Buffer

Dependencies: `python-frontmatter==0.5.0`, `requests`, `python-dotenv` (already installed).

## What still needs to happen (full checklist)

### Step 1 — imgbb (image hosting)
- [ ] Go to https://imgbb.com → create free account
- [ ] Go to https://api.imgbb.com → generate a free API key
- [ ] Copy the key into `scripts/.env` as `IMGBB_API_KEY=`

### Step 2 — Instagram Business account
- [ ] Confirm @coderassist is a **Creator or Business** account
  - Instagram app → Profile → Settings → Account type and tools
  - If Personal: switch to Professional → Creator or Business
- [ ] Link it to a **Facebook Page** (Meta requires this for API access)
  - Instagram → Settings → Account → Linked accounts → Facebook
  - Create a new Page if you don't have one (can be minimal)

### Step 3 — Buffer account + API token
- [ ] Go to https://buffer.com → sign up free
- [ ] Connect the Instagram account (requires Business type + Facebook Page from Step 2)
- [ ] Get **access token**: https://buffer.com/developers/api/oauth → use the "Get Access Token" flow
- [ ] Get **Instagram profile ID**: `GET https://api.bufferapp.com/1/profiles.json?access_token=YOUR_TOKEN`
  - Find the profile where `service == "instagram"` and copy its `id`
- [ ] Copy both into `scripts/.env`:
  ```
  BUFFER_ACCESS_TOKEN=
  BUFFER_INSTAGRAM_PROFILE_ID=
  ```

### Step 4 — Write the .env file
Create `scripts/.env` (copy from `scripts/.env.example`):
```
BUFFER_ACCESS_TOKEN=<from Step 3>
BUFFER_INSTAGRAM_PROFILE_ID=<from Step 3>
IMGBB_API_KEY=<from Step 1>
POST_HOUR=9
POST_MINUTE=30
```

### Step 5 — Post the first post (01-stat-shock)
```bash
# The image already exists in assets/post-1/
python scripts/mark.py 01-stat-shock ready
python scripts/push.py --dry-run    # verify caption + date look right
python scripts/push.py              # real push → imgbb upload + Buffer queue
```

### Step 6 — Queue the Week 1 schedule
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

For each: generate image in ChatGPT (upload `assets/avatar.jpg`, paste `## Image Prompt` from the post file) → save to `assets/post-N/` → mark ready → push.

## MCP Playwright note

Playwright MCP is registered (`claude mcp add playwright npx @playwright/mcp@latest`).
**It will be available in this new session** — Claude can open a browser and walk through the imgbb + Buffer setup interactively.

## Prompt to paste

> We're working on the @coderassist Instagram posting automation in `/Users/santiagomorel/site/coderassist-ai`.
> Last session we built three Python scripts (`scripts/status.py`, `scripts/mark.py`, `scripts/push.py`) that extract captions from markdown post files and push to Buffer via imgbb for image hosting.
> MCP Playwright is now registered — use it to walk me through setting up imgbb (free API key) and Buffer (free account, connect Instagram, get access token + profile ID). I'll fill in credentials as we go.
> Once `.env` is populated, run `python scripts/push.py --dry-run` then the real push for post `01-stat-shock` (image already exists in `assets/post-1/`).
> Check `NEXT-SESSION.md` in the project root for the full checklist.
