# Read X Posts Without Login (FxTwitter / vxTwitter / oEmbed)

Source: Skill Card No.001, @ojigineko_tips — "Xポスト読み取りスキル". Saved 2026-11-15 at John's request. Verified live 2026-11-15 against https://x.com/ojigineko_tips/status/2120622660833173617 (FxTwitter returned HTTP 200 with full text, author, counts and media).

## When to use this skill

- The user gives a specific X (formerly Twitter) post URL and asks what it says.
- x.com itself cannot be read directly because of the login wall or domain restrictions.
- Only for a single public post whose URL is already known. To *find* a post by topic or keyword, use the `grok_x_search` skill first to get the URL, then read it with this skill ("search = Grok Build, read = FxTwitter").

## Rules — read-only, always

- Read-only only. Never like, follow, reply, post, or log in.
- Only public posts can be read. If a post is non-public or deleted, say honestly that it cannot be read — do not guess its content.
- FxTwitter and vxTwitter are unofficial services run by volunteers, so they can stop at any time. If they stop, fall back to method 3 (official oEmbed).
- If one method fails, do not repeat the same method — move on to the next method.

## Methods — use in order 1 → 2 → 3

### 1. FxTwitter (primary — most information)

```
https://api.fxtwitter.com/<user>/status/<post_id>
```

- Take the username and post ID from the post URL.
- The returned JSON contains: text (`text`), author info, likes, reposts, replies, views, and attached media URLs.
- Quoted post: the `quote` field contains the full text of the quoted post — read that too.
- Video: the `media` field contains the mp4 direct URL and the thumbnail URL.

### 2. vxTwitter (backup — when FxTwitter does not work)

```
https://api.vxtwitter.com/<user>/status/<post_id>
```

- Content is almost the same JSON, but field names differ slightly (`text` / `user_name` / `likes`, and the quote is `qrt`), and view count (`views`) is not included.
- Numbers may be old (measured at about 1/4 of FxTwitter's). Confirm accurate numbers with FxTwitter.
- Quoted post: the `qrt` field contains the full text of the quoted post (verified by measurement).

### 3. Official oEmbed (last resort — least likely to stop)

```
https://publish.twitter.com/oembed?url=<encoded_post_url>
```

- `<encoded_post_url>` is the post URL, URL-encoded.
- Only the text and the author can be retrieved. Like counts and other numbers do not come out.
- A direct image URL cannot be retrieved (only the `pic.twitter.com` link inside the HTML).
- Fetch with `curl -sL` (a 301 redirect is returned, so `-L` is required. Text fetch from a browser may fail because of domain restrictions).

### 4. Account info (when you want to know the person, not the post)

```
https://api.fxtwitter.com/<user>
```

- Returns follower count, bio, post count, and registration period.

## Tips

- Photo URL: append `?name=orig` to the end to get the original size.
- Video: first check the thumbnail image to judge the content, then download the mp4 only if needed.
- A trailing `https://t.co/...` at the end of the text is a link to media, not part of the text — do not treat it as text.
- Report numbers as the value at the time of fetching (they increase a little each time the post is read).
- If one method fails, do not repeat it — move to the next method.

## What to report for a post

Text (full, not truncated), author (name + @handle), likes / reposts / replies / views / bookmarks / quotes as fetched, and the content of attached images or video (check the thumbnail / image itself, do not guess from the text alone).
