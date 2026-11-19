#!/usr/bin/env python3
"""Merge 10 enriched batches into top100-v2/songs-enriched.json/.csv.
- Dedupe: song-115/song-118 appear identically in batch-03 and batch-05;
  keep first occurrence, log the duplicate.
- song-086 'Ghen' was missed by batch-03; enriched manually by coordinator
  15/11 via Deezer + iTunes + Credits.fm (see MERGE_NOTES in README-v2.md).
- Never overwrites v1 fields: enriched records already preserve them.
Run: python3 merge.py  (from ~/workspace/music-database/top100-v2/)
"""
import json, glob, csv, collections, pathlib

BASE = pathlib.Path(__file__).parent
V1 = pathlib.Path.home() / "workspace/music-database/top100/songs.json"
BATCHES = sorted(glob.glob(str(BASE / "batches/batch-*/songs-enriched.json")))

v1 = {s["id"]: s for s in json.load(open(V1))}
merged = {}
dups = []
for f in BATCHES:
    for s in json.load(open(f)):
        if s["id"] in merged:
            dups.append((s["id"], f))
        else:
            merged[s["id"]] = s

# song-086, enriched manually by coordinator (Deezer/iTunes/Credits.fm, 15/11)
song086 = dict(v1["song-086"])
song086.update({
    "isrc": "SGUM72400059",
    "iswc": "T-301049471-6",
    "deezer_id": 2612287792,
    "deezer_url": "https://www.deezer.com/track/2612287792",
    "deezer_album": "Ghen",
    "apple_music_url": "https://music.apple.com/vn/album/ghen/1724722202?i=1724722213&uo=4",
    "apple_release_date": "2017-05-23",
    "duration_seconds": 247,
    "credits_songwriters": [{"name": "HUNG KHAC", "ipi": "00690117845", "role": "ComposerLyricist"}],
    "credits_source": "credits.fm /v1/isrc/SGUM72400059 (MLC GA0QE5)",
    "credits_mlc_code": "GA0QE5",
    "credits_upc": "00602465094626",
    "isrc_source": "deezer",
    "iswc_source": "credits.fm",
    "enrichment_confidence": "high",
    "conflicts": [],
})
merged["song-086"] = song086

missing = sorted(set(v1) - set(merged))
extra = sorted(set(merged) - set(v1))
assert not missing, f"missing: {missing}"
assert not extra, f"extra: {extra}"
assert len(merged) == 380, len(merged)

songs = [merged[k] for k in sorted(merged, key=lambda i: int(i.split("-")[1]))]

def cnt(fn):
    return sum(1 for s in songs if fn(s))

def v1cnt(field):
    return sum(1 for s in v1.values() if s.get(field))

stats = {
    "total": len(songs),
    "isrc_before": v1cnt("isrc"), "isrc_after": cnt(lambda s: bool(s.get("isrc"))),
    "iswc_before": v1cnt("iswc"), "iswc_after": cnt(lambda s: bool(s.get("iswc"))),
    "apple_before": v1cnt("apple_music_url"), "apple_after": cnt(lambda s: bool(s.get("apple_music_url"))),
    "deezer_after": cnt(lambda s: bool(s.get("deezer_url"))),
    "duration_before": v1cnt("duration_seconds"), "duration_after": cnt(lambda s: bool(s.get("duration_seconds"))),
    "composers_v1": cnt(lambda s: bool(s.get("composers"))),
    "composers_with_credits": cnt(lambda s: bool(s.get("composers")) or bool(s.get("credits_songwriters"))),
    "year_v1": cnt(lambda s: bool(s.get("year"))),
    "youtube_official_v1": v1cnt("youtube_official_url"),
    "confidence": dict(collections.Counter(s.get("enrichment_confidence") or "none" for s in songs)),
    "duplicates_removed": dups,
    "per_batch": {},
}
for f in BATCHES:
    b = json.load(open(f))
    name = pathlib.Path(f).parent.name
    stats["per_batch"][name] = {
        "n": len(b),
        "isrc": sum(1 for s in b if s.get("isrc")),
        "iswc": sum(1 for s in b if s.get("iswc")),
        "apple": sum(1 for s in b if s.get("apple_music_url")),
    }

json.dump(songs, open(BASE / "songs-enriched.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)
json.dump(stats, open(BASE / "merge-stats.json", "w", encoding="utf-8"),
          ensure_ascii=False, indent=2)

# CSV: flatten list fields
fields = ["id", "title", "singers", "composers", "credits_songwriters", "year",
          "apple_release_date", "album", "deezer_album", "duration_seconds",
          "isrc", "iswc", "deezer_url", "apple_music_url", "youtube_official_url",
          "spotify_url", "isrc_source", "iswc_source", "enrichment_confidence",
          "conflicts_count", "title_version"]
def flat(v):
    if isinstance(v, list):
        return "; ".join(str(x.get("name", x)) if isinstance(x, dict) else str(x) for x in v)
    return "" if v is None else v
with open(BASE / "songs-enriched.csv", "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=fields)
    w.writeheader()
    for s in songs:
        row = {k: flat(s.get(k)) for k in fields}
        row["conflicts_count"] = len(s.get("conflicts") or [])
        row["credits_songwriters"] = "; ".join(
            f"{c.get('name')} ({c.get('role','')}, IPI {c.get('ipi','')})".strip()
            for c in (s.get("credits_songwriters") or []))
        w.writerow(row)

print(json.dumps(stats, ensure_ascii=False, indent=2))
print("missing:", missing, "extra:", extra)
