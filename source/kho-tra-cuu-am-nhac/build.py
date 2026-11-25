#!/usr/bin/env python3
"""Build tu-dien-am-nhac-3-lop.html — single file, data embedded compact."""
import json, pathlib

BASE = pathlib.Path('/home/hatch/workspace/music-glossary-3-layers')
DATA = BASE / 'data'
OUT = BASE / 'tu-dien-am-nhac-3-lop.html'

genres = json.load(open(DATA / 'merged-genres.json'))
instruments = json.load(open(DATA / 'merged-instruments.json'))
theory = json.load(open(DATA / 'merged-theory.json'))
previews = json.load(open(DATA / 'previews-itunes.json'))

# sanity
assert len(genres) == 226 and len(instruments) == 75 and len(theory) == 75
assert len(previews) == 226 and set(previews) == {g['id'] for g in genres}
for v in previews.values():
    assert v['source'] == 'itunes' and 'preview_url' in v and 'exp=' not in v['preview_url']
    assert 'deezer' not in v['preview_url'].lower() and 'spotify' not in v['preview_url'].lower()

def cj(obj):
    s = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
    assert '</script' not in s.lower()
    return s

GENRES = cj(genres); INST = cj(instruments); THEORY = cj(theory); PREV = cj(previews)

HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Kho Tra Cứu Âm Nhạc — 3 lớp trong 1 chỗ</title>
<meta name="description" content="226 thể loại nhạc, 75 nhạc cụ & dàn nhạc, 75 thuật ngữ lý thuyết — tra cứu nhanh, nghe thử 30 giây qua iTunes Preview.">
<style>
:root{
  --bg:#FAF6EF; --card:#FFFFFF; --ink:#211D19; --muted:#6F6459; --faint:#9A8E80;
  --line:#E9DFD2; --line-soft:#F0E8DB;
  --accent:#B4431F; --accent-dark:#8F3415; --accent-soft:#FBE9DD; --accent-gold:#D97706;
  --amber-bg:#FFF7E8; --amber-line:#EFD9A7; --amber-ink:#7A5410;
  --green:#2F6B4F; --green-bg:#E7F2EC;
  --dark:#221A12; --dark2:#2E2318;
  --radius:16px; --shadow:0 1px 2px rgba(33,29,25,.06),0 8px 24px -12px rgba(33,29,25,.18);
  --serif:Georgia,'Times New Roman',serif;
  --sans:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,'Helvetica Neue',Arial,sans-serif;
}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
::selection{background:var(--accent);color:#fff}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
/* ---------- HERO ---------- */
.hero{background:radial-gradient(1100px 420px at 85% -10%,#4A2E1B 0%,transparent 60%),radial-gradient(800px 380px at 0% 0%,#5B3A1E 0%,transparent 55%),linear-gradient(135deg,#221A12 0%,#2E2114 55%,#1C150E 100%);color:#F7F1E6;padding:56px 0 0;overflow:hidden}
.hero-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12.5px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#E8B25C;border:1px solid rgba(232,178,92,.45);border-radius:999px;padding:7px 14px;background:rgba(232,178,92,.08)}
.hero-eyebrow .dot{width:7px;height:7px;border-radius:50%;background:#E8B25C}
.hero h1{font-family:var(--serif);font-size:clamp(34px,5.2vw,58px);line-height:1.12;font-weight:700;margin:22px 0 6px;letter-spacing:-.01em}
.hero h1 em{font-style:italic;color:#E8B25C}
.hero .sub{font-size:clamp(16px,2vw,19px);color:#D8CDBB;max-width:760px}
.hero .sub b{color:#fff}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:30px 0 26px}
.stat{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:var(--radius);padding:18px 20px}
.stat .n{font-family:var(--serif);font-size:38px;font-weight:700;line-height:1;color:#fff}
.stat .n span{color:#E8B25C;font-size:22px}
.stat .l{font-size:13.5px;color:#CFC3AF;margin-top:6px}
.stat .l b{color:#F7F1E6}
.howto{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:18px 0 26px;border-top:1px solid rgba(255,255,255,.12)}
.howto div{font-size:13.5px;color:#D8CDBB;line-height:1.55}
.howto b{display:block;color:#fff;font-size:13px;letter-spacing:.06em;text-transform:uppercase;margin-bottom:4px}
.howto b i{font-style:normal;color:#E8B25C;margin-right:6px}
/* ---------- TABS ---------- */
.tabbar{position:sticky;top:0;z-index:50;background:rgba(250,246,239,.94);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:14px 0}
.tabs{display:flex;gap:10px;flex-wrap:wrap}
.tab{flex:1;min-width:200px;text-align:left;background:var(--card);border:1.5px solid var(--line);border-radius:14px;padding:13px 16px;cursor:pointer;font-family:var(--sans);transition:.18s}
.tab:hover{border-color:var(--accent);transform:translateY(-1px)}
.tab.active{border-color:var(--accent);background:var(--accent-soft);box-shadow:var(--shadow)}
.tab .t-name{font-weight:800;font-size:16px;display:flex;justify-content:space-between;align-items:center;gap:8px}
.tab .t-count{font-family:var(--serif);font-size:20px;color:var(--accent)}
.tab .t-desc{font-size:12.5px;color:var(--muted);margin-top:2px}
.tab.active .t-desc{color:#7A4A33}
/* ---------- PANEL / TOOLBAR ---------- */
.panel{display:none;padding:28px 0 8px}
.panel.active{display:block;animation:fade .25s ease}
@keyframes fade{from{opacity:0;transform:translateY(4px)}to{opacity:1;transform:none}}
.panel-intro{font-size:15.5px;color:var(--muted);max-width:820px;margin-bottom:18px}
.panel-intro b{color:var(--ink)}
.toolbar{display:flex;gap:10px;flex-wrap:wrap;align-items:center;margin-bottom:14px}
.search{flex:1;min-width:240px;display:flex;align-items:center;gap:10px;background:#fff;border:1.5px solid var(--line);border-radius:999px;padding:11px 16px}
.search:focus-within{border-color:var(--accent);box-shadow:0 0 0 3px rgba(180,67,31,.14)}
.search svg{flex:none;color:var(--faint)}
.search input{border:0;outline:0;font:inherit;width:100%;background:transparent;color:var(--ink)}
.search input::placeholder{color:var(--faint)}
.btn{border:1.5px solid var(--line);background:#fff;color:var(--ink);border-radius:999px;padding:11px 18px;font:inherit;font-weight:700;font-size:14px;cursor:pointer;transition:.15s;white-space:nowrap}
.btn:hover{border-color:var(--accent);color:var(--accent)}
.btn.primary{background:var(--accent);border-color:var(--accent);color:#fff}
.btn.primary:hover{background:var(--accent-dark);color:#fff}
.btn.ghost{font-weight:600;color:var(--muted)}
.result-line{font-size:14px;color:var(--muted);margin:2px 0 16px}
.result-line b{color:var(--ink)}
.filters{margin-bottom:8px}
.filter-group{margin-bottom:12px}
.filter-label{font-size:12px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--faint);margin-bottom:7px}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:7px 14px;font-size:13.5px;font-weight:600;cursor:pointer;color:#4A4238;transition:.14s}
.chip:hover{border-color:var(--accent)}
.chip.on{background:var(--ink);border-color:var(--ink);color:#fff}
.chip.on.accent{background:var(--accent);border-color:var(--accent)}
.chip .c{opacity:.65;font-weight:400;margin-left:4px}
/* ---------- ORCHESTRA DIAGRAM ---------- */
.orch{border:1.5px solid var(--line);border-radius:var(--radius);background:#fff;box-shadow:var(--shadow);padding:20px;margin:4px 0 24px}
.orch h3{font-family:var(--serif);font-size:19px;margin-bottom:4px}
.orch p{font-size:13.5px;color:var(--muted);margin-bottom:16px}
.orch-stage{display:flex;flex-direction:column;gap:8px}
.orch-row{display:grid;gap:8px}
.orch-row.r1{grid-template-columns:1.4fr 1fr 1fr}
.orch-row.r2{grid-template-columns:1fr 1fr 1fr}
.orch-row.r3{grid-template-columns:1.2fr 1fr}
.orch-row.r4{grid-template-columns:1fr 1fr 1fr}
.orch-cell{border-radius:12px;padding:12px 14px;font-size:13px;line-height:1.45}
.orch-cell b{display:block;font-size:14px;margin-bottom:2px}
.orch-cell.strings{background:#FDF0E4;border:1px solid #F0D3B3}
.orch-cell.wood{background:#EAF3EC;border:1px solid #C4DCCB}
.orch-cell.brass{background:#FFF6DB;border:1px solid #EBD28A}
.orch-cell.perc{background:#F3EAF7;border:1px solid #DCCBE8}
.orch-cell.keys{background:#E8EEF7;border:1px solid #C3D2E8}
.orch-cell.ethnic{background:#FDECEC;border:1px solid #F2C6C6}
.orch-tag{font-size:11px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:var(--faint);margin-bottom:5px}
.conductor{text-align:center;font-size:13px;color:var(--muted);padding-top:4px}
.conductor .podium{display:inline-block;background:var(--ink);color:#fff;border-radius:999px;padding:6px 16px;font-weight:700;font-size:12.5px;letter-spacing:.05em}
/* ---------- CARDS ---------- */
.grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:var(--radius);padding:22px;box-shadow:var(--shadow);display:flex;flex-direction:column;transition:transform .15s,box-shadow .15s}
.card:hover{transform:translateY(-2px);box-shadow:0 2px 4px rgba(33,29,25,.06),0 16px 32px -12px rgba(33,29,25,.24)}
.card.flash{outline:3px solid var(--accent-gold);outline-offset:2px}
.card-top{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px}
.badge{display:inline-block;font-size:11.5px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;border-radius:999px;padding:5px 11px}
.badge.cat{background:var(--accent-soft);color:var(--accent-dark)}
.badge.level{background:#F0EAE0;color:#5C5145}
.badge.level.nang_cao{background:#F3E3E0;color:#7A2E1D}
.badge.fam{background:var(--green-bg);color:var(--green)}
.badge.id{margin-left:auto;background:transparent;color:var(--faint);font-weight:600;letter-spacing:.08em}
.card h3{font-family:var(--serif);font-size:23px;line-height:1.25;font-weight:700}
.card h3 .en{display:block;font-family:var(--sans);font-size:14px;font-weight:600;color:var(--muted);margin-top:3px;font-style:italic}
.card .desc{font-size:15px;color:#3D362E;margin-top:10px}
.meta-line{font-size:14px;color:#4A4238;margin-top:12px;border-top:1px dashed var(--line);padding-top:12px}
.meta-line b{color:var(--ink)}
.meta-row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-top:12px}
.bpm{display:inline-flex;align-items:center;gap:6px;font-size:13px;font-weight:800;color:var(--ink);background:#F4EEE3;border:1px solid var(--line);border-radius:999px;padding:5px 12px}
.bpm small{font-weight:600;color:var(--muted)}
.mood{display:inline-block;font-size:12.5px;font-weight:600;color:#5C5145;background:#FBF7F0;border:1px solid var(--line-soft);border-radius:999px;padding:5px 11px}
.usewhen{margin-top:14px;background:var(--accent-soft);border-left:4px solid var(--accent);border-radius:0 12px 12px 0;padding:12px 14px;font-size:14px}
.usewhen b{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--accent-dark);margin-bottom:3px}
.confused{margin-top:14px;background:var(--amber-bg);border:1px solid var(--amber-line);border-radius:12px;padding:12px 14px;font-size:14px}
.confused b{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--amber-ink);margin-bottom:3px}
.note-box{margin-top:14px;background:#F6F1E7;border-radius:12px;padding:12px 14px;font-size:14px}
.note-box b{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin-bottom:3px}
.pos-box{margin-top:14px;background:#EFF4F0;border:1px solid #D3E2D8;border-radius:12px;padding:12px 14px;font-size:14px}
.pos-box b{display:block;font-size:11.5px;letter-spacing:.09em;text-transform:uppercase;color:var(--green);margin-bottom:3px}
.audio-box{margin-top:16px;background:#211D19;border-radius:12px;padding:14px 16px;color:#F7F1E6}
.audio-box .a-label{font-size:12px;font-weight:800;letter-spacing:.09em;text-transform:uppercase;color:#E8B25C;margin-bottom:2px}
.audio-box .a-track{font-size:14.5px;font-weight:700}
.audio-box .a-track span{font-weight:400;color:#CFC3AF}
.audio-box audio{width:100%;margin-top:10px;height:38px;outline:none}
.audio-box .a-note{font-size:12px;color:#A99C88;margin-top:8px}
.no-audio{margin-top:16px;font-size:13px;color:var(--faint);border-top:1px dashed var(--line);padding-top:12px}
/* ---------- EMPTY / FOOTER / FAB ---------- */
.empty{display:none;text-align:center;padding:56px 20px;border:1.5px dashed var(--line);border-radius:var(--radius);background:#fff}
.empty.show{display:block}
.empty .big{font-family:var(--serif);font-size:26px;margin-bottom:8px}
.empty p{color:var(--muted);max-width:440px;margin:0 auto 16px}
footer{background:var(--dark);color:#CFC3AF;margin-top:56px;padding:40px 0 48px;font-size:14px}
footer h4{font-family:var(--serif);color:#F7F1E6;font-size:19px;margin-bottom:10px}
footer p{margin-bottom:10px;max-width:820px}
footer .src{color:#A99C88;font-size:13px}
.fab{position:fixed;right:20px;bottom:20px;z-index:60;display:flex;flex-direction:column;gap:10px}
.fab button{width:48px;height:48px;border-radius:50%;border:1px solid var(--line);background:#fff;box-shadow:var(--shadow);font-size:19px;cursor:pointer;color:var(--ink)}
.fab button:hover{border-color:var(--accent);color:var(--accent)}
.fab button.top{display:none}
.fab button.top.show{display:block}
@media(max-width:820px){
  .grid{grid-template-columns:1fr}
  .stats{grid-template-columns:1fr 1fr 1fr;gap:10px}
  .stat .n{font-size:28px}
  .howto{grid-template-columns:1fr;gap:10px}
  .tabs{flex-wrap:nowrap;overflow-x:auto;padding-bottom:4px;-webkit-overflow-scrolling:touch}
  .tab{min-width:230px;flex:none}
  .chips{flex-wrap:nowrap;overflow-x:auto;padding-bottom:6px;-webkit-overflow-scrolling:touch}
  .chip{flex:none}
  .orch-row{grid-template-columns:1fr !important}
  .card{padding:18px}
}
</style>
</head>
<body>

<header class="hero">
  <div class="wrap">
    <span class="hero-eyebrow"><span class="dot"></span> Kho tra cứu &middot; 3 lớp trong 1 chỗ</span>
    <h1>Kho Tra Cứu <em>Âm Nhạc</em><br>3 lớp trong 1 chỗ</h1>
    <p class="sub">Nghe một thể loại mà không biết gọi tên nó là gì? Muốn biết cây kèn kia ngồi ở đâu trong dàn nhạc, hay <b>tempo</b> khác <b>rhythm</b> chỗ nào? Kho này gom cả ba — <b>thể loại, nhạc cụ, lý thuyết</b> — để tra trong vài giây, nghe thử ngay 30 giây.</p>
    <div class="stats">
      <div class="stat"><div class="n">226</div><div class="l"><b>Thể loại nhạc</b> — từ Rock, Pop, Điện tử tới nhạc Việt &amp; World</div></div>
      <div class="stat"><div class="n">75</div><div class="l"><b>Nhạc cụ &amp; dàn nhạc</b> — 7 họ nhạc cụ, kèm vị trí ngồi</div></div>
      <div class="stat"><div class="n">75</div><div class="l"><b>Thuật ngữ lý thuyết</b> — định nghĩa, ví dụ &amp; cặp dễ nhầm</div></div>
    </div>
    <div class="howto">
      <div><b><i>1</i> Chọn lớp</b>Thể loại để tìm nhạc nghe / làm nền, Nhạc cụ để hiểu âm sắc, Lý thuyết để hiểu bài nhạc đang làm gì.</div>
      <div><b><i>2</i> Gõ &amp; lọc</b>Tìm không dấu — gõ “lofi”, “nhac cu”, “tempo” đều ra. Lọc thêm theo nhóm, tâm trạng, trình độ.</div>
      <div><b><i>3</i> Nghe &amp; dùng</b>Mỗi thể loại có bản nghe thử 30 giây thật qua iTunes. Hộp “Dùng khi nào” gợi ý đúng lúc dùng nó.</div>
    </div>
  </div>
</header>

<div class="tabbar">
  <div class="wrap">
    <div class="tabs" role="tablist">
      <button class="tab active" data-tab="genres" role="tab" aria-selected="true">
        <span class="t-name">Thể loại <span class="t-count">226</span></span>
        <span class="t-desc">Tìm nhạc theo thể loại — nghe thử 30 giây</span>
      </button>
      <button class="tab" data-tab="instruments" role="tab" aria-selected="false">
        <span class="t-name">Nhạc cụ &amp; Dàn nhạc <span class="t-count">75</span></span>
        <span class="t-desc">7 họ nhạc cụ &amp; vị trí ngồi trong dàn nhạc</span>
      </button>
      <button class="tab" data-tab="theory" role="tab" aria-selected="false">
        <span class="t-name">Lý thuyết <span class="t-count">75</span></span>
        <span class="t-desc">Thuật ngữ, định nghĩa &amp; cặp dễ nhầm</span>
      </button>
    </div>
  </div>
</div>

<main class="wrap">

  <!-- ============ GENRES ============ -->
  <section class="panel active" id="panel-genres">
    <p class="panel-intro"><b>226 thể loại</b> trong 15 nhóm lớn — từ Rock (63) và Điện tử (34) tới nhạc Việt, Latin, Jazz và các trào lưu 2024–2026. Mỗi thẻ có mô tả ngắn, nghệ sĩ đại diện, BPM, tâm trạng và một bản nghe thử 30 giây thật.</p>
    <div class="toolbar">
      <label class="search">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input id="q-genres" type="search" placeholder="Tìm thể loại… thử “lofi”, “rock”, “nhac viet”, “chill”" autocomplete="off">
      </label>
      <button class="btn primary" data-random="genres">Ngẫu nhiên</button>
      <button class="btn ghost" data-reset="genres">Xóa lọc</button>
    </div>
    <div class="filters" id="filters-genres"></div>
    <p class="result-line" id="count-genres"></p>
    <div class="grid" id="grid-genres"></div>
    <div class="empty" id="empty-genres">
      <div class="big">Không tìm thấy thể loại nào</div>
      <p>Thử một từ khác — ví dụ “rock”, “lofi”, “latin” — hoặc bỏ bớt bộ lọc đang chọn.</p>
      <button class="btn primary" data-reset="genres">Xóa hết bộ lọc</button>
    </div>
  </section>

  <!-- ============ INSTRUMENTS ============ -->
  <section class="panel" id="panel-instruments">
    <p class="panel-intro"><b>75 nhạc cụ</b> thuộc 7 họ — Dây, Gỗ, Đồng, Gõ, Phím, Điện tử, Dân tộc. Mỗi thẻ ghi rõ <b>vị trí ngồi trong dàn nhạc giao hưởng</b>, âm sắc và bản nhạc ví dụ để nghe ra tiếng của nó.</p>
    <div class="orch">
      <h3>Sơ đồ dàn nhạc giao hưởng — nhìn từ khán giả</h3>
      <p>Nhạc trưởng đứng trước, quay lưng về phía khán giả. Dây ngồi trước nhất, gần khán giả nhất; càng về sau âm thanh càng vang, càng mạnh.</p>
      <div class="orch-stage">
        <div class="orch-tag">Hàng trước — gần khán giả nhất</div>
        <div class="orch-row r1">
          <div class="orch-cell strings"><b>Dây — bên trái</b>Violin 1, Violin 2 — giọng chính, ngồi hàng đầu bên trái nhạc trưởng.</div>
          <div class="orch-cell strings"><b>Dây — giữa</b>Viola, Cello — đệm hòa âm, ngồi trung tâm, trước kèn gỗ.</div>
          <div class="orch-cell strings"><b>Dây — bên phải</b>Double Bass — nền trầm, đứng/ngồi ngoài cùng bên phải.</div>
        </div>
        <div class="orch-tag">Hàng giữa</div>
        <div class="orch-row r2">
          <div class="orch-cell wood"><b>Gỗ — Woodwind</b>Sáo, Oboe, Clarinet, Bassoon — ngồi ngay sau dàn dây, giữa sân khấu.</div>
          <div class="orch-cell keys"><b>Phím</b>Piano, Harpsichord, Organ — thường đặt lệch một bên, sau dây.</div>
          <div class="orch-cell ethnic"><b>Dân tộc</b>Đàn tranh, Sáo trúc, Đàn bầu… — vị trí linh hoạt theo dàn nhạc dân tộc / giao hưởng.</div>
        </div>
        <div class="orch-tag">Hàng sau</div>
        <div class="orch-row r3">
          <div class="orch-cell brass"><b>Đồng — Brass</b>Trumpet, Trombone, Horn, Tuba — ngồi sau kèn gỗ, âm vang, mạnh.</div>
          <div class="orch-cell perc"><b>Gõ — Percussion</b>Trống, Cymbal, Xylophone… — ngồi cuối cùng, sau lưng dàn đồng.</div>
        </div>
        <div class="orch-tag">Bên cạnh / điện tử</div>
        <div class="orch-row r4">
          <div class="orch-cell keys"><b>Điện tử</b>Synthesizer, Drum Machine — đặt bên sân khấu, nối loa.</div>
          <div class="orch-cell perc"><b>Gõ phụ</b>Timpani, Triangle… — rải dọc hàng cuối, gần trống chính.</div>
          <div class="orch-cell strings"><b>Harp</b>Ngồi lệch trái/phải hàng giữa, gần dàn dây.</div>
        </div>
        <div class="conductor"><span class="podium">Nhạc trưởng</span><br>đứng trước dàn nhạc, quay lưng về phía khán giả</div>
      </div>
    </div>
    <div class="toolbar">
      <label class="search">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input id="q-instruments" type="search" placeholder="Tìm nhạc cụ… thử “violin”, “trong”, “sao truc”" autocomplete="off">
      </label>
      <button class="btn primary" data-random="instruments">Ngẫu nhiên</button>
      <button class="btn ghost" data-reset="instruments">Xóa lọc</button>
    </div>
    <div class="filters" id="filters-instruments"></div>
    <p class="result-line" id="count-instruments"></p>
    <div class="grid" id="grid-instruments"></div>
    <div class="empty" id="empty-instruments">
      <div class="big">Không tìm thấy nhạc cụ nào</div>
      <p>Thử một từ khác — ví dụ “violin”, “trống”, “sáo” — hoặc bỏ bớt bộ lọc đang chọn.</p>
      <button class="btn primary" data-reset="instruments">Xóa hết bộ lọc</button>
    </div>
  </section>

  <!-- ============ THEORY ============ -->
  <section class="panel" id="panel-theory">
    <p class="panel-intro"><b>75 thuật ngữ lý thuyết</b> trong 7 nhóm — Hòa âm, Ký hiệu, Nhịp điệu, Giai điệu, Hình thức, Thang âm, Giọng hát. Mỗi thẻ có định nghĩa ngắn gọn, ví dụ đời thường và hộp <b>“Dễ nhầm với…”</b> để phân biệt các cặp hay lẫn.</p>
    <div class="toolbar">
      <label class="search">
        <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3"/></svg>
        <input id="q-theory" type="search" placeholder="Tìm thuật ngữ… thử “tempo”, “hop am”, “giong”" autocomplete="off">
      </label>
      <button class="btn primary" data-random="theory">Ngẫu nhiên</button>
      <button class="btn ghost" data-reset="theory">Xóa lọc</button>
    </div>
    <div class="filters" id="filters-theory"></div>
    <p class="result-line" id="count-theory"></p>
    <div class="grid" id="grid-theory"></div>
    <div class="empty" id="empty-theory">
      <div class="big">Không tìm thấy thuật ngữ nào</div>
      <p>Thử một từ khác — ví dụ “tempo”, “hợp âm”, “giọng” — hoặc bỏ bớt bộ lọc đang chọn.</p>
      <button class="btn primary" data-reset="theory">Xóa hết bộ lọc</button>
    </div>
  </section>

</main>

<footer>
  <div class="wrap">
    <h4>Kho Tra Cứu Âm Nhạc — 3 lớp trong 1 chỗ</h4>
    <p>Nội dung thể loại tham khảo Every Noise at Once, Chosic và Wikipedia; nhạc cụ và thuật ngữ được biên soạn, đối chiếu từ các nguồn tra cứu âm nhạc công khai. Bản nghe thử 30 giây được cung cấp qua iTunes Preview — bấm play là nghe trực tiếp, không cần tài khoản.</p>
    <p class="src">Ghi chú: Spotify không còn cung cấp preview cho app mới từ 27/11/2024 nên kho dùng iTunes Preview thay thế. Một số bản nghe thử là bản Acoustic / Live / Remaster hoặc có nghệ sĩ khách mời — tên bài hiển thị đúng tên bản nghe thử thực tế.</p>
    <p class="src">226 thể loại &middot; 75 nhạc cụ &middot; 75 thuật ngữ &middot; 226 bản nghe thử iTunes &middot; Mở offline được (trừ phần nghe thử cần mạng).</p>
  </div>
</footer>

<div class="fab">
  <button class="top" id="toTop" title="Cuộn lên đầu" aria-label="Cuộn lên đầu">&#8593;</button>
</div>

<script>
const GENRES=__GENRES__;
const INSTRUMENTS=__INST__;
const THEORY=__THEORY__;
const PREVIEWS=__PREV__;

/* ---------- helpers ---------- */
const $=s=>document.querySelector(s);
const norm=s=>(s||'').toString().normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase();
const esc=s=>(s||'').toString().replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const LEVEL={co_ban:'Cơ bản',trung_cap:'Trung cấp',nang_cao:'Nâng cao'};
const levelLabel=l=>LEVEL[l]||l;
/* mood merge: "vui vẻ" gộp vào "vui tươi" */
const MOOD_MAP={'vui vẻ':'vui tươi'};
const moodKey=m=>MOOD_MAP[m]||m;
const MOOD_ORDER=['sôi động','lãng mạn','thư giãn','hoài cổ','mơ màng','mạnh mẽ','vui tươi','nặng nề','dữ dội','cảm xúc','thôi miên','mộc mạc','sâu lắng','phóng khoáng','nổi loạn','bay bổng','da diết','u ám','bốc lửa'];

/* one audio at a time */
document.addEventListener('play',e=>{if(e.target.tagName==='AUDIO'){document.querySelectorAll('audio').forEach(a=>{if(a!==e.target)a.pause();});}},true);

/* ---------- state ---------- */
const state={
  genres:{q:'',cat:'',mood:'',level:''},
  instruments:{q:'',family:'',level:''},
  theory:{q:'',cat:'',level:''}
};

/* ---------- filters UI ---------- */
function chipGroup(label,items,tab,field,accent){
  const counts={};
  items.forEach(it=>counts[it.value]=(counts[it.value]||0)+1);
  return '<div class="filter-group"><div class="filter-label">'+esc(label)+'</div><div class="chips">'
    +'<button class="chip'+(state[tab][field]===''?' on':'')+'" data-tab="'+tab+'" data-field="'+field+'" data-value="">Tất cả</button>'
    +items.map(it=>'<button class="chip'+(state[tab][field]===it.value?' on'+(accent?' accent':''):'')+'" data-tab="'+tab+'" data-field="'+field+'" data-value="'+esc(it.value)+'">'+esc(it.label)+'<span class="c">'+(counts[it.value]||it.count||'')+'</span></button>').join('')
    +'</div></div>';
}
function buildFilters(){
  const gCats=[...new Set(GENRES.map(g=>g.big_category))];
  const gCatCounts={}; GENRES.forEach(g=>gCatCounts[g.big_category]=(gCatCounts[g.big_category]||0)+1);
  const gMoods=MOOD_ORDER.filter(m=>GENRES.some(g=>(g.mood||[]).some(x=>moodKey(x)===m)));
  const gMoodCounts={}; GENRES.forEach(g=>(g.mood||[]).forEach(x=>{const k=moodKey(x);gMoodCounts[k]=(gMoodCounts[k]||0)+1;}));
  $('#filters-genres').innerHTML =
    chipGroup('Nhóm thể loại',gCats.map(c=>({value:c,label:c,count:gCatCounts[c]})),'genres','cat',true)
    +chipGroup('Tâm trạng',gMoods.map(m=>({value:m,label:m,count:gMoodCounts[m]})),'genres','mood')
    +chipGroup('Trình độ',Object.keys(LEVEL).map(l=>({value:l,label:LEVEL[l],count:GENRES.filter(g=>g.level===l).length})),'genres','level');
  const fams=[...new Set(INSTRUMENTS.map(i=>i.family))];
  $('#filters-instruments').innerHTML =
    chipGroup('Họ nhạc cụ',fams.map(c=>({value:c,label:c,count:INSTRUMENTS.filter(i=>i.family===c).length})),'instruments','family',true)
    +chipGroup('Trình độ',Object.keys(LEVEL).map(l=>({value:l,label:LEVEL[l],count:INSTRUMENTS.filter(i=>i.level===l).length})),'instruments','level');
  const tCats=[...new Set(THEORY.map(t=>t.category))];
  $('#filters-theory').innerHTML =
    chipGroup('Nhóm thuật ngữ',tCats.map(c=>({value:c,label:c,count:THEORY.filter(t=>t.category===c).length})),'theory','cat',true)
    +chipGroup('Trình độ',Object.keys(LEVEL).map(l=>({value:l,label:LEVEL[l],count:THEORY.filter(t=>t.level===l).length})),'theory','level');
  document.querySelectorAll('.chip').forEach(ch=>ch.addEventListener('click',()=>{
    const tab=ch.dataset.tab,field=ch.dataset.field;
    state[tab][field]=ch.dataset.value;
    buildFilters(); renderAll();
  }));
}

/* ---------- card templates ---------- */
function genreCard(g){
  const p=PREVIEWS[g.id];
  const moods=(g.mood||[]).map(m=>'<span class="mood">'+esc(m)+'</span>').join('');
  const bpm=g.bpm?'<span class="bpm">BPM '+esc(g.bpm)+'</span>':'';
  const audio=p?'<div class="audio-box"><div class="a-label">Nghe thử 30 giây &middot; iTunes Preview</div><div class="a-track">'+esc(p.track)+' <span>— '+esc(p.artist)+'</span></div><audio controls preload="none" src="'+esc(p.preview_url)+'"></audio><div class="a-note">Bản nghe thử thực tế — có thể là bản Acoustic / Live / Remaster, tên hiển thị đúng bản đó.</div></div>':'';
  return '<article class="card" data-id="'+esc(g.id)+'">'
    +'<div class="card-top"><span class="badge cat">'+esc(g.big_category)+'</span><span class="badge level '+esc(g.level)+'">'+esc(levelLabel(g.level))+'</span><span class="badge id">'+esc(g.id)+'</span></div>'
    +'<h3>'+esc(g.name_vi)+'<span class="en">'+esc(g.name_en)+'</span></h3>'
    +'<p class="desc">'+esc(g.description)+'</p>'
    +'<p class="meta-line"><b>Nghệ sĩ đại diện:</b> '+esc(g.artist)+' &nbsp;&middot;&nbsp; <b>Bài ví dụ:</b> '+esc(g.example_track)+'</p>'
    +'<div class="meta-row">'+bpm+moods+'</div>'
    +'<div class="usewhen"><b>Dùng khi nào</b>'+esc(g.use_when)+'</div>'
    +audio+'</article>';
}
function instCard(it){
  const moods=(it.mood||[]).map(m=>'<span class="mood">'+esc(m)+'</span>').join('');
  return '<article class="card" data-id="'+esc(it.id)+'">'
    +'<div class="card-top"><span class="badge fam">'+esc(it.family)+'</span><span class="badge level '+esc(it.level)+'">'+esc(levelLabel(it.level))+'</span><span class="badge id">'+esc(it.id)+'</span></div>'
    +'<h3>'+esc(it.name_vi)+'<span class="en">'+esc(it.name_en)+'</span></h3>'
    +'<p class="desc">'+esc(it.sound)+'</p>'
    +'<div class="pos-box"><b>Vị trí trong dàn nhạc</b>'+esc(it.orchestra_position)+'</div>'
    +'<p class="meta-line"><b>Bản nhạc ví dụ:</b> '+esc(it.example_piece)+'</p>'
    +'<div class="meta-row">'+moods+'</div>'
    +'<div class="usewhen"><b>Dùng khi nào</b>'+esc(it.use_when)+'</div></article>';
}
function theoryCard(t){
  const conf=t.confused_with?'<div class="confused"><b>Dễ nhầm với…</b>'+esc(t.confused_with)+'</div>':'';
  return '<article class="card" data-id="'+esc(t.id)+'">'
    +'<div class="card-top"><span class="badge cat">'+esc(t.category)+'</span><span class="badge level '+esc(t.level)+'">'+esc(levelLabel(t.level))+'</span><span class="badge id">'+esc(t.id)+'</span></div>'
    +'<h3>'+esc(t.name_vi)+'<span class="en">'+esc(t.name_en)+'</span></h3>'
    +'<p class="desc">'+esc(t.definition)+'</p>'
    +'<div class="note-box"><b>Ví dụ</b>'+esc(t.example)+'</div>'
    +conf
    +'<div class="usewhen"><b>Khi nào dùng</b>'+esc(t.when_to_use)+'</div></article>';
}

/* ---------- filtering + render ---------- */
function haystack(...parts){return norm(parts.filter(Boolean).join(' '));}
function matchesQuery(q,hay){if(!q)return true;return norm(q).split(/\s+/).filter(Boolean).every(tok=>hay.includes(tok));}
function renderGenres(){
  const s=state.genres;
  const q=norm(s.q);
  const list=GENRES.filter(g=>{
    if(s.cat&&g.big_category!==s.cat)return false;
    if(s.mood&&!(g.mood||[]).some(m=>moodKey(m)===s.mood))return false;
    if(s.level&&g.level!==s.level)return false;
    if(!matchesQuery(s.q,haystack(g.name_vi,g.name_en,g.big_category,g.description,g.artist,g.example_track,(g.mood||[]).join(' '),g.use_when)))return false;
    return true;
  });
  $('#grid-genres').innerHTML=list.map(genreCard).join('');
  $('#count-genres').innerHTML='Đang hiển thị <b>'+list.length+' / 226</b> thể loại'+(s.q?' cho “'+esc(s.q)+'”':'')+'.';
  $('#empty-genres').classList.toggle('show',list.length===0);
  return list;
}
function renderInstruments(){
  const s=state.instruments; const q=norm(s.q);
  const list=INSTRUMENTS.filter(it=>{
    if(s.family&&it.family!==s.family)return false;
    if(s.level&&it.level!==s.level)return false;
    if(!matchesQuery(s.q,haystack(it.name_vi,it.name_en,it.family,it.sound,it.example_piece,it.orchestra_position,(it.mood||[]).join(' '),it.use_when)))return false;
    return true;
  });
  $('#grid-instruments').innerHTML=list.map(instCard).join('');
  $('#count-instruments').innerHTML='Đang hiển thị <b>'+list.length+' / 75</b> nhạc cụ'+(s.q?' cho “'+esc(s.q)+'”':'')+'.';
  $('#empty-instruments').classList.toggle('show',list.length===0);
  return list;
}
function renderTheory(){
  const s=state.theory; const q=norm(s.q);
  const list=THEORY.filter(t=>{
    if(s.cat&&t.category!==s.cat)return false;
    if(s.level&&t.level!==s.level)return false;
    if(!matchesQuery(s.q,haystack(t.name_vi,t.name_en,t.category,t.definition,t.example,t.confused_with,t.when_to_use)))return false;
    return true;
  });
  $('#grid-theory').innerHTML=list.map(theoryCard).join('');
  $('#count-theory').innerHTML='Đang hiển thị <b>'+list.length+' / 75</b> thuật ngữ'+(s.q?' cho “'+esc(s.q)+'”':'')+'.';
  $('#empty-theory').classList.toggle('show',list.length===0);
  return list;
}
function renderAll(){renderGenres();renderInstruments();renderTheory();}

/* ---------- tabs ---------- */
document.querySelectorAll('.tab').forEach(tab=>tab.addEventListener('click',()=>{
  document.querySelectorAll('.tab').forEach(t=>{t.classList.remove('active');t.setAttribute('aria-selected','false');});
  tab.classList.add('active');tab.setAttribute('aria-selected','true');
  document.querySelectorAll('.panel').forEach(p=>p.classList.remove('active'));
  $('#panel-'+tab.dataset.tab).classList.add('active');
  window.scrollTo({top:document.querySelector('.tabbar').offsetTop,behavior:'smooth'});
}));

/* ---------- search / reset / random ---------- */
[['genres','q-genres'],['instruments','q-instruments'],['theory','q-theory']].forEach(([tab,id])=>{
  document.getElementById(id).addEventListener('input',e=>{state[tab].q=e.target.value;if(tab==='genres')renderGenres();if(tab==='instruments')renderInstruments();if(tab==='theory')renderTheory();});
});
document.querySelectorAll('[data-reset]').forEach(b=>b.addEventListener('click',()=>{
  const tab=b.dataset.reset;
  state[tab]={q:'',cat:'',mood:'',level:'',family:''};
  const qEl=document.getElementById('q-'+tab); if(qEl)qEl.value='';
  buildFilters(); renderAll();
}));
document.querySelectorAll('[data-random]').forEach(b=>b.addEventListener('click',()=>{
  const tab=b.dataset.random;
  /* reset filters so the pick is from the full set, then flash the card */
  state[tab]={q:'',cat:'',mood:'',level:'',family:''};
  const qEl=document.getElementById('q-'+tab); if(qEl)qEl.value='';
  buildFilters(); renderAll();
  const list=tab==='genres'?GENRES:tab==='instruments'?INSTRUMENTS:THEORY;
  const pick=list[Math.floor(Math.random()*list.length)];
  const card=document.querySelector('#grid-'+tab+' [data-id="'+pick.id+'"]');
  if(card){card.scrollIntoView({behavior:'smooth',block:'center'});card.classList.add('flash');setTimeout(()=>card.classList.remove('flash'),2200);}
}));

/* ---------- back to top ---------- */
const toTop=$('#toTop');
window.addEventListener('scroll',()=>{toTop.classList.toggle('show',window.scrollY>600);},{passive:true});
toTop.addEventListener('click',()=>window.scrollTo({top:0,behavior:'smooth'}));

/* ---------- init ---------- */
buildFilters();
renderAll();
</script>
</body>
</html>
"""

html = HTML.replace('__GENRES__', GENRES).replace('__INST__', INST).replace('__THEORY__', THEORY).replace('__PREV__', PREV)
OUT.write_text(html, encoding='utf-8')
print('written', OUT, len(html.encode('utf-8')), 'bytes')
