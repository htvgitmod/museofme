#!/usr/bin/env python3
"""Fetch iTunes previews for all merged genres (iTunes-first, no Deezer: Deezer links expire in ~15 min)."""
import json, urllib.request, urllib.parse, unicodedata, re, time, sys

BASE = '/home/hatch/workspace/music-glossary-3-layers/data/'
genres = json.load(open(BASE + 'merged-genres.json'))

def norm(s):
    s = unicodedata.normalize('NFKD', s or '').encode('ascii', 'ignore').decode()
    s = s.lower()
    s = re.sub(r'\(.*?(remaster|live|acoustic|version|edit|mix).*?\)', '', s)
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    return re.sub(r'\s+', ' ', s).strip()

def tokens(s):
    return set(norm(s).split())

def match_score(q_track, q_artist, r):
    rt, ra = norm(r.get('trackName', '')), norm(r.get('artistName', ''))
    qt, qa = norm(q_track), norm(q_artist)
    if not rt or not ra:
        return 0
    # exact track match
    t_ok = (rt == qt) or (qt in rt) or (rt in qt and len(rt) > 3)
    a_tok, r_tok = tokens(q_artist), set(ra.split())
    a_ok = bool(a_tok & r_tok) or (qa in ra) or (ra in qa)
    if t_ok and a_ok:
        return 3
    if t_ok:
        return 2
    if a_ok and tokens(q_track) & set(rt.split()):
        return 1
    return 0

def itunes_search(term, limit=5):
    url = 'https://itunes.apple.com/search?' + urllib.parse.urlencode(
        {'term': term, 'media': 'music', 'limit': limit})
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.load(resp).get('results', [])

out, missing = {}, []
for g in genres:
    gid, artist, track = g['id'], g['artist'], g['example_track']
    found = None
    queries = [f"{artist} {track}", track, f"{artist} {track.split('(')[0].strip()}"]
    for qi, q in enumerate(queries):
        try:
            results = itunes_search(q)
        except Exception as e:
            print(gid, 'ERR', q, e, flush=True)
            time.sleep(1)
            continue
        best, best_score = None, 0
        for r in results:
            s = match_score(track, artist, r)
            if s > best_score and r.get('previewUrl'):
                best, best_score = r, s
        if best and best_score >= 2:
            found = best
            break
        time.sleep(0.3)
    if found:
        out[gid] = {'source': 'itunes', 'preview_url': found['previewUrl'],
                    'track': found.get('trackName'), 'artist': found.get('artistName')}
        print(gid, 'OK', found.get('trackName'), '-', found.get('artistName'), flush=True)
    else:
        missing.append(gid)
        print(gid, 'MISS', artist, '-', track, flush=True)
    time.sleep(0.3)

json.dump(out, open(BASE + 'previews-itunes.json', 'w'), ensure_ascii=False, indent=1)
print('DONE total:', len(genres), 'with preview:', len(out), 'missing:', len(missing))
print('missing ids:', missing)
