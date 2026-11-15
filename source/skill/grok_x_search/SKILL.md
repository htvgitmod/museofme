# Search X with Grok Build (xAI CLI)

Source: Skill Card No.001, @ojigineko_tips — "Xポスト読み取りスキル", 5th method. Saved 2026-11-15 at John's request. Login / install is NOT done yet — it is deferred until the user can do it on their own device (see below).

## When to use this skill

- The four methods in `fxtwitter_post_reader` read a post whose URL is already known. When the user wants to search by topic or keyword and does not have a URL yet, use this skill.
- Division of labour: search = Grok Build, read = FxTwitter. Search to identify the URL first, then read the original with FxTwitter — that is the reliable flow.
- Optional only. Only for people who have a Grok paid plan. People without one should skip this skill entirely.

## Install and login (deferred — user does it on their own device)

- If there is no CLI, install `grok` with the official x.ai installer (destination `~/.grok/bin/grok`. Check the contents and confirm it only writes under the home directory before executing).
- Check login status with `grok models`. If "You are logged in with grok.com" is shown, that is OK.
- If not logged in, run `grok login --device-code`, and hand the URL and code to the user so they approve it on their own device. Never receive passwords etc. in chat, and never read `~/.grok/auth.json`.

## How to search

- Execution form:

```
grok --no-subagents --max-turns 6 --reasoning-effort low -p "<instruction>"
```

- The instruction must always include: use only `x_search` / topic, name and period specific / narrow the number of results / return date, account, summary and URL / if nothing is found, answer "not found".
- Search consumes the user's Grok subscription quota. Narrow the scope and use it at low frequency.

## After searching

- Take the post URL returned by the search and re-read it with the `fxtwitter_post_reader` skill (FxTwitter) to confirm the original text, author, counts and media — do not report the search summary as if it were the original post.
