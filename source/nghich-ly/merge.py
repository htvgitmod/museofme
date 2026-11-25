#!/usr/bin/env python3
"""Gom 5 batch -> data/nghich-ly.json + data/nghich-ly.md (dedupe, renumber)."""
import json, re, glob
from collections import Counter

DROP_E = {"crocodile dilemma", "braess's paradox", "downs\u2013thomson paradox",
          "paradox of tolerance", "sleeping beauty problem", "boy or girl paradox"}

def norm(s):
    return re.sub(r"\s+", " ", s.strip().lower())

merged = []
seen = set()
dropped = []
for f in ["batch-a.json", "batch-b.json", "batch-c.json", "batch-d.json", "batch-e.json"]:
    data = json.load(open(f"/home/hatch/workspace/nghich-ly/data/{f}"))
    for x in data:
        key = norm(x["en_name"])
        # Boy or Girl vs Boy or girl -> same key after lower()
        if key in seen:
            dropped.append((x["id"], x["en_name"], f))
            continue
        seen.add(key)
        x = dict(x)
        x["batch_id"] = x["id"]
        merged.append(x)

print(f"raw total: 115, dropped dups: {len(dropped)}")
for d in dropped:
    print("  dropped:", d)

# Normalize Mary's room name
for x in merged:
    if norm(x["en_name"]).startswith("mary's room"):
        x["en_name"] = "Mary's room"

# Renumber NL-001..NL-109
for i, x in enumerate(merged, 1):
    x["id"] = f"NL-{i:03d}"

# Validate
assert len(merged) == 109, len(merged)
cats = Counter(x["category"] for x in merged)
print("categories:", dict(cats))
print("interactive:", Counter(x["interactive"] for x in merged))
print("source_status:", Counter(x["source_status"] for x in merged))
for x in merged:
    for field in ("en_name", "vi_name", "category", "puzzle", "explanation", "source_url"):
        assert x.get(field), (x["id"], field)
    n = len([p for p in re.split(r"[.!?]\s", x["explanation"].strip()) if p.strip()])
    assert n == 3, (x["id"], "explanation sentences", n)
    if x["interactive"] == "quiz":
        assert x.get("quiz_question") and len(x.get("quiz_options", [])) == 3
        assert 0 <= x["quiz_answer"] <= 2, x["id"]

json.dump(merged, open("/home/hatch/workspace/nghich-ly/data/nghich-ly.json", "w"),
          ensure_ascii=False, indent=2)

CAT_VI = {"logic": "Logic", "xac-suat": "Xác suất", "thoi-gian": "Thời gian",
          "vo-cuc": "Vô cực", "tu-tham-chieu": "Tự tham chiếu",
          "vat-ly": "Vật lý", "quyet-dinh": "Quyết định"}
lines = ["# Nghịch lý — Câu đố làm não kẹt (dữ liệu nguồn)",
         "",
         f"Tổng: **{len(merged)} nghịch lý** (gom từ 5 batch, đã loại 6 mục trùng tên).",
         "Mỗi mục: tên Anh + tên Việt, câu đố, giải thích đúng 3 câu, phân loại, link Wikipedia EN.",
         "Tất cả 106 URL nguồn riêng biệt đã kiểm tra HTTP 200 ngày 25/11/2026; 0 mục 'chưa kiểm chứng'.",
         "",
         "## Lưu ý nguồn",
         "- Bootstrap / Predestination / Causal loop cùng trỏ bài Wikipedia `Temporal_paradox` (3 khái niệm khác nhau, cùng 1 bài).",
         "- 4 nghịch lý Zeno (Achilles, Dichotomy, Arrow, Stadium) cùng trỏ bài `Zeno's paradoxes`.",
         "- Tristram Shandy trỏ `Temporal_finitism`, Problem of future contingents trỏ `Contingency_(philosophy)`, Polchinski trỏ `Novikov_self-consistency_principle` — các bài chứa mục về nghịch lý đó, không có trang riêng.",
         "- Inspection paradox trỏ `Renewal_theory`, Meno's paradox trỏ `Meno` (bài chứa mục).",
         "- Paradox of choice trỏ trang sách `The_Paradox_of_Choice` của Barry Schwartz (mục này có trong List of paradoxes).",
         "- Mpemba effect: ghi rõ trong lời giải đây là hiệu ứng quan sát, không phải nghịch lý logic thuần túy.",
         "- 6 mục trùng đã loại khi gộp (giữ bản của batch chính A/B/D): Crocodile dilemma (E), Braess's paradox (E), Downs–Thomson paradox (E), Paradox of tolerance (E), Sleeping Beauty problem (E), Boy or Girl paradox (E).",
         "",
         "## Danh sách",
         ""]
for x in merged:
    lines.append(f"### {x['id']} — {x['vi_name']} ({x['en_name']}) [{CAT_VI[x['category']]}]")
    lines.append(f"- Câu đố: {x['puzzle']}")
    lines.append(f"- Lời giải: {x['explanation']}")
    if x["interactive"] == "quiz":
        opts = "; ".join(f"{chr(65+i)}. {o}" for i, o in enumerate(x["quiz_options"]))
        lines.append(f"- Quiz: {x['quiz_question']} — {opts} (Đáp án: {chr(65+x['quiz_answer'])})")
    elif x["interactive"] in ("monty-hall", "birthday"):
        lines.append(f"- Mô phỏng tương tác: {x['interactive']}")
    lines.append(f"- Nguồn: {x['source_url']}")
    lines.append("")
open("/home/hatch/workspace/nghich-ly/data/nghich-ly.md", "w").write("\n".join(lines))
print("wrote data/nghich-ly.json + data/nghich-ly.md, total", len(merged))
