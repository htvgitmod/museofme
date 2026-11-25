#!/usr/bin/env python3
"""Build tam-ly-thi-nghiem.html from data.json (static render + base64 images)."""
import json, base64, html, os, pathlib

ROOT = pathlib.Path(__file__).parent
data = json.load(open(ROOT / 'data.json', encoding='utf-8'))
FIELD = {
    'Tam ly xa hoi': 'Tâm lý xã hội',
    'Nhan thuc va Tri nho': 'Nhận thức & Trí nhớ',
    'Phat trien': 'Phát triển',
    'Hanh vi va Hoc tap': 'Hành vi & Học tập',
    'Cam xuc, Dong luc, Nhan cach': 'Cảm xúc, Động lực & Nhân cách',
    'Ra quyet dinh va Kinh te hanh vi': 'Ra quyết định & Kinh tế hành vi',
}
CONT_CLASS = {'Thấp': 'c-low', 'Trung bình': 'c-mid', 'Cao': 'c-high', 'Rất cao': 'c-vhigh'}
n_high = sum(1 for x in data if x['controversy'] in ('Cao', 'Rất cao'))
n_img = 0
img_b64 = {}
for x in data:
    if not x.get('image'):
        continue
    for cand in (ROOT / 'images' / (x['id'] + '.jpg'), ROOT / 'images' / (x['id'] + '.svg')):
        if cand.exists():
            mime = 'image/svg+xml' if cand.suffix == '.svg' else 'image/jpeg'
            img_b64[x['id']] = (mime, base64.b64encode(cand.read_bytes()).decode())
            n_img += 1
            break

def esc(s):
    return html.escape(str(s), quote=True)

cards = []
for i, x in enumerate(data, 1):
    img_html = ''
    if x['id'] in img_b64:
        mime, b64 = img_b64[x['id']]
        im = x['image']
        cap = esc(im.get('caption') or x['en_name'])
        lic = esc(im.get('license') or '')
        auth = esc(im.get('author') or '')
        page = esc(im.get('page') or '')
        img_html = (
            f'<figure class="fig"><img src="data:{mime};base64,{b64}" alt="{cap}" loading="lazy">'
            f'<figcaption>{cap}<br><span class="credit">Ảnh: {auth} — {lic} · '
            f'<a href="{page}" target="_blank" rel="noopener">Wikimedia Commons</a></span></figcaption></figure>'
        )
    badge = ''
    if not x.get('verified'):
        note = esc(x.get('notes') or '')
        badge = (f'<div class="unverified"><b>⚠ Chưa kiểm chứng đầy đủ.</b> {note}</div>')
    srcs = ''.join(
        f'<li><a href="{esc(s.get("url",""))}" target="_blank" rel="noopener">{esc(s.get("label") or s.get("url",""))}</a></li>'
        for s in x['sources']
    )
    cards.append(f'''
<article class="card" id="{esc(x["id"])}" data-field="{esc(x["field"])}" data-controversy="{esc(x["controversy"])}">
  <div class="card-top"><span class="num">{i:02d}</span>
    <div class="titles"><h2>{esc(x["en_name"])}</h2><p class="vi">{esc(x["vi_name"])}</p></div>
  </div>
  <div class="tags"><span class="tag field">{esc(FIELD.get(x["field"], x["field"]))}</span>
    <span class="tag {CONT_CLASS[x["controversy"]]}">Tranh cãi: {esc(x["controversy"])}</span>
    <span class="tag year">{esc(x["researcher"])} · {esc(x["year"])}</span></div>
  {badge}
  {img_html}
  <div class="sec"><h3>Cách làm</h3><p>{esc(x["method"])}</p></div>
  <div class="sec"><h3>Kết quả</h3><p>{esc(x["results"])}</p></div>
  <div class="sec"><h3>Bài học rút ra</h3><p>{esc(x["lesson"])}</p></div>
  <div class="sec debate"><h3>Đang tranh cãi</h3><p>{esc(x["controversy_text"])}</p></div>
  <div class="sec sources"><h3>Nguồn</h3><ol>{srcs}</ol></div>
</article>''')

chips = ''.join(
    f'<button type="button" class="chip" data-f="{esc(k)}">{esc(v)}</button>'
    for k, v in FIELD.items()
)

CSS = '''
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Alegreya',Georgia,'Times New Roman',serif;margin:0;background:#F7F1E3;color:#2E2620;line-height:1.65}
a{color:#B85C38}
header.hero{background:#FBF6EC;border-bottom:3px solid #B85C38;padding:34px 20px 22px;text-align:center}
header.hero h1{font-family:'Caveat',cursive;font-size:52px;line-height:1.05;margin:0;color:#8A3B1E}
header.hero .sub{font-size:18px;color:#6B5D4F;max-width:760px;margin:10px auto 0}
.stats{display:flex;gap:12px;flex-wrap:wrap;justify-content:center;margin:20px auto 0;max-width:900px}
.stat{background:#fff;border:1px solid #E4D5BE;border-radius:12px;padding:10px 18px;min-width:130px;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.stat b{display:block;font-size:26px;color:#B85C38;line-height:1.1}
.stat span{font-size:13px;color:#6B5D4F}
.wrap{max-width:920px;margin:0 auto;padding:0 16px 70px}
.controls{position:sticky;top:0;z-index:50;background:#F7F1E3;padding:12px 0 10px;border-bottom:1px solid #E0CDB2}
.controls .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.controls input[type=search]{flex:1 1 260px;padding:11px 13px;font-size:16px;font-family:inherit;border:1px solid #C9B18F;border-radius:10px;background:#FFFDF7}
.controls select{padding:11px 8px;font-size:15px;font-family:inherit;border:1px solid #C9B18F;border-radius:10px;background:#FFFDF7}
.controls button{cursor:pointer;border:0;border-radius:10px;font-size:15px;font-family:inherit;padding:11px 16px;background:#B85C38;color:#fff}
.controls button.ghost{background:#FFFDF7;color:#8A3B1E;border:1px solid #C9B18F}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}
.chip{font-size:13px;padding:5px 11px;border-radius:20px;background:#FFFDF7;color:#6B4A2F;border:1px solid #D8C3A5;cursor:pointer;font-family:inherit}
.chip.on{background:#B85C38;color:#fff;border-color:#B85C38}
#count{font-size:14px;color:#6B5D4F;margin:8px 0 0}
.note{background:#FFF8E1;border:1px solid #EBCB7A;border-radius:10px;padding:12px 16px;margin:16px 0;font-size:15px}
.card{background:#FFFDF7;border:1px solid #E4D5BE;border-radius:14px;padding:20px 22px;margin:0 0 18px;box-shadow:0 1px 4px rgba(0,0,0,.05);scroll-margin-top:150px}
.card.flash{outline:3px solid #B85C38}
.card-top{display:flex;gap:12px;align-items:flex-start}
.num{font-family:'Caveat',cursive;font-size:30px;color:#B85C38;line-height:1;min-width:44px}
.titles h2{margin:0;font-size:24px;line-height:1.25;color:#2E2620}
.titles .vi{font-family:'Caveat',cursive;font-size:24px;color:#8A3B1E;margin:2px 0 0;line-height:1.2}
.tags{display:flex;gap:6px;flex-wrap:wrap;margin:10px 0 4px}
.tag{font-size:12.5px;padding:3px 10px;border-radius:20px;background:#F1E7D3;color:#5A4632;border:1px solid #DCC9A8}
.tag.c-low{background:#E6F0E2;color:#2F6B33;border-color:#BFD8B6}
.tag.c-mid{background:#FBF0D3;color:#7A5A00;border-color:#E8D28F}
.tag.c-high{background:#FBE3D3;color:#9A3B12;border-color:#EFB48F}
.tag.c-vhigh{background:#FADBD8;color:#8E1F16;border-color:#EFA9A2}
.tag.year{background:#fff}
.unverified{background:#FDECEA;border:1px solid #F0B8B2;border-radius:10px;padding:10px 14px;margin:10px 0;font-size:14.5px}
.fig{margin:12px 0;text-align:center}
.fig img{max-width:100%;max-height:420px;border-radius:10px;border:1px solid #E4D5BE}
.fig figcaption{font-size:13px;color:#6B5D4F;margin-top:6px}
.credit{font-size:12px}
.sec{margin:12px 0}
.sec h3{font-family:'Caveat',cursive;font-size:23px;color:#8A3B1E;margin:0 0 2px}
.sec p{margin:0;font-size:16px}
.sec.debate{background:#FBEFE6;border-left:4px solid #B85C38;border-radius:0 10px 10px 0;padding:10px 14px}
.sec.sources ol{margin:4px 0 0;padding-left:20px;font-size:14.5px}
.sec.sources li{margin:2px 0;overflow-wrap:anywhere}
footer{border-top:2px solid #E0CDB2;padding:22px 20px 40px;text-align:center;color:#6B5D4F;font-size:14px}
@media(max-width:640px){header.hero h1{font-size:40px}.titles h2{font-size:20px}.card{padding:16px}}
'''

JS = '''
function norm(s){return (s||'').normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase();}
function applyFilter(){
  var q=norm(document.getElementById('q').value.trim());
  var f=document.getElementById('field').value, c=document.getElementById('controversy').value, n=0, total=0;
  document.querySelectorAll('.card').forEach(function(card){
    total++;
    var ok=true;
    if(f && card.dataset.field!==f) ok=false;
    if(c && card.dataset.controversy!==c) ok=false;
    if(q && norm(card.textContent).indexOf(q)===-1) ok=false;
    card.style.display=ok?'':'none';
    if(ok) n++;
  });
  document.getElementById('count').textContent='Hiển thị '+n+' / '+total+' thí nghiệm';
  document.querySelectorAll('.chip').forEach(function(ch){ch.classList.toggle('on', ch.dataset.f===f);});
}
document.getElementById('q').addEventListener('input',applyFilter);
document.getElementById('field').addEventListener('change',applyFilter);
document.getElementById('controversy').addEventListener('change',applyFilter);
document.querySelectorAll('.chip').forEach(function(ch){ch.addEventListener('click',function(){
  var sel=document.getElementById('field');
  sel.value=(sel.value===ch.dataset.f)?'':ch.dataset.f; applyFilter();
});});
document.getElementById('random').addEventListener('click',function(){
  var vis=[].filter.call(document.querySelectorAll('.card'),function(c){return c.style.display!=='none';});
  if(!vis.length) return;
  var pick=vis[Math.floor(Math.random()*vis.length)];
  pick.scrollIntoView({behavior:'smooth',block:'start'});
  pick.classList.add('flash'); setTimeout(function(){pick.classList.remove('flash');},2200);
});
document.getElementById('clear').addEventListener('click',function(){
  document.getElementById('q').value=''; document.getElementById('field').value=''; document.getElementById('controversy').value=''; applyFilter();
});
applyFilter();
'''

options_field = ''.join(f'<option value="{esc(k)}">{esc(v)}</option>' for k, v in FIELD.items())

html_doc = f'''<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Các thí nghiệm tâm lý nổi tiếng — 60 thí nghiệm tra cứu tiếng Việt</title>
<meta name="description" content="Một chỗ tra cứu duy nhất bằng tiếng Việt: 60 thí nghiệm tâm lý nổi tiếng — cách làm, kết quả, bài học và phần đang tranh cãi, kèm nguồn kiểm chứng.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,700;1,400&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
<header class="hero">
  <h1>Các thí nghiệm tâm lý nổi tiếng</h1>
  <p class="sub">Một chỗ tra cứu duy nhất bằng tiếng Việt: cách làm, kết quả, bài học rút ra — và cả phần đang tranh cãi — của những thí nghiệm đã định hình tâm lý học hiện đại.</p>
  <div class="stats">
    <div class="stat"><b>60</b><span>thí nghiệm</span></div>
    <div class="stat"><b>6</b><span>lĩnh vực</span></div>
    <div class="stat"><b>{n_high}</b><span>tranh cãi Cao / Rất cao</span></div>
    <div class="stat"><b>{n_img}</b><span>mục có ảnh thật</span></div>
  </div>
</header>
<div class="wrap">
  <div class="controls">
    <div class="row">
      <input type="search" id="q" placeholder="Tìm không dấu: milgram, nha tu, pavlov, tri nho…" aria-label="Tìm kiếm">
      <select id="field" aria-label="Lọc theo lĩnh vực"><option value="">Tất cả lĩnh vực</option>{options_field}</select>
      <select id="controversy" aria-label="Lọc theo mức tranh cãi"><option value="">Mọi mức tranh cãi</option><option>Thấp</option><option>Trung bình</option><option>Cao</option><option>Rất cao</option></select>
      <button type="button" id="random">🎲 Ngẫu nhiên</button>
      <button type="button" id="clear" class="ghost">Xóa lọc</button>
    </div>
    <div class="chips">{chips}</div>
    <p id="count">Hiển thị 60 / 60 thí nghiệm</p>
  </div>
  <div class="note"><b>Cách đọc:</b> mỗi mục ghi tên tiếng Anh gốc + tên tiếng Việt, nhà nghiên cứu và năm, cách làm, kết quả, bài học — và hộp <b>“Đang tranh cãi”</b> ghi rõ thí nghiệm nào đang bị nghi ngờ về đạo đức, phương pháp hay khả năng tái lập. Mục gắn huy hiệu <b>“Chưa kiểm chứng đầy đủ”</b> là mục còn số liệu hoặc nguồn chưa đối chiếu xong — xem ghi chú trong mục và trong file <code>data.md</code>.</div>
  <main id="list">
{''.join(cards)}
  </main>
</div>
<footer>
  <p>Nguồn chính: Wikipedia (tiếng Anh) + bài báo gốc / nguồn uy tín của từng thí nghiệm — xem mục “Nguồn” ở mỗi thẻ và file <code>data.json</code> / <code>data.md</code> đi kèm.</p>
  <p>Ảnh (nếu có) đều là ảnh tự do — public domain hoặc CC-BY / CC-BY-SA — từ Wikimedia Commons, có ghi giấy phép và tác giả dưới mỗi ảnh.</p>
  <p>Các thí nghiệm cũ có thể vi phạm chuẩn đạo đức nghiên cứu hiện nay; trang này trình bày để tham khảo, không cổ vũ lặp lại chúng.</p>
</footer>
<script>{JS}</script>
</body>
</html>
'''

out = ROOT / 'tam-ly-thi-nghiem.html'
out.write_text(html_doc, encoding='utf-8')
print('HTML bytes:', out.stat().st_size)
print('cards:', html_doc.count('<article class="card"'))
print('images embedded:', n_img, '| high controversy:', n_high)
