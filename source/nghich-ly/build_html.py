#!/usr/bin/env python3
"""Sinh nghich-ly.html (1 file duy nhất, tự chứa) từ data/nghich-ly.json."""
import json
from collections import Counter

SRC = "/home/hatch/workspace/nghich-ly/data/nghich-ly.json"
OUT = "/home/hatch/workspace/nghich-ly/nghich-ly.html"

with open(SRC, encoding="utf-8") as f:
    DATA = json.load(f)

assert len(DATA) == 109, len(DATA)
CATS = [
    ("logic", "Logic"), ("xac-suat", "Xác suất"), ("thoi-gian", "Thời gian"),
    ("vo-cuc", "Vô cực"), ("tu-tham-chieu", "Tự tham chiếu"),
    ("vat-ly", "Vật lý"), ("quyet-dinh", "Quyết định"),
]
CAT_LABEL = dict(CATS)
counts = Counter(x["category"] for x in DATA)
n_quiz = sum(1 for x in DATA if x["interactive"] == "quiz")

chips = ['<button class="chip on" data-cat="all">Tất cả · 109</button>']
for key, label in CATS:
    chips.append(f'<button class="chip" data-cat="{key}">{label} · {counts[key]}</button>')
CHIPS_HTML = "\n".join(chips)

# JSON nhúng: escape các ký tự có thể phá thẻ <script>
DATA_JSON = (json.dumps(DATA, ensure_ascii=False)
             .replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026"))

HTML = r"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nghịch lý — Câu đố làm não kẹt (109 nghịch lý)</title>
<meta name="description" content="Một chỗ tra cứu duy nhất bằng tiếng Việt: 109 nghịch lý nổi tiếng — câu đố lên trước, lời giải tự mở, có quiz và mô phỏng tương tác.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;0,800;1,400;1,500&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:#FAF6EF;color:#2B2620;font-family:'Alegreya',Georgia,'Times New Roman',serif;line-height:1.65;
  background-image:radial-gradient(#EFE6D2 1px,transparent 1px);background-size:26px 26px}
a{color:#B85C38}
.wrap{max-width:980px;margin:0 auto;padding:0 16px 60px}
/* ---------- header ---------- */
header.hero{padding:44px 16px 26px;text-align:center}
header.hero .kicker{font-family:'Caveat',cursive;font-size:22px;color:#B85C38;letter-spacing:.5px}
header.hero h1{font-family:'Caveat',cursive;font-weight:700;font-size:clamp(44px,8vw,72px);line-height:1.05;margin:4px 0 8px;color:#33261C}
header.hero h1 .q{color:#B85C38}
header.hero p.sub{max-width:640px;margin:0 auto;font-size:18px;color:#5C5347}
.stats{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:20px 0 10px}
.stat{background:#FFFDF8;border:1px solid #E5DCC8;border-radius:12px;padding:8px 16px;box-shadow:0 1px 3px rgba(60,40,20,.08)}
.stat b{display:block;font-size:22px;color:#B85C38;line-height:1.1}
.stat span{font-size:13px;color:#7A6F60}
.srcnote{font-size:14px;color:#7A6F60;max-width:640px;margin:6px auto 0}
/* ---------- controls ---------- */
.controls{position:sticky;top:0;z-index:50;background:rgba(250,246,239,.97);border-bottom:1px solid #E5DCC8;padding:12px 0 10px;backdrop-filter:blur(2px)}
.controls .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.controls input[type=search]{flex:1 1 260px;padding:11px 14px;font-size:16px;font-family:inherit;border:1px solid #D8CDB6;border-radius:10px;background:#FFFDF8;color:#2B2620}
.controls input[type=search]:focus{outline:2px solid #B85C38;outline-offset:1px}
.chips{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
.chip{cursor:pointer;border:1px solid #D8CDB6;background:#FFFDF8;color:#5C5347;border-radius:20px;padding:5px 12px;font-size:14px;font-family:inherit}
.chip:hover{border-color:#B85C38;color:#B85C38}
.chip.on{background:#B85C38;color:#FFF6EE;border-color:#B85C38}
.btn{cursor:pointer;border:0;border-radius:10px;font-size:15px;padding:10px 16px;font-family:inherit;background:#B85C38;color:#FFF6EE}
.btn:hover{background:#9E4C2D}
.btn.ghost{background:#FFFDF8;color:#B85C38;border:1px solid #D8CDB6}
#count{font-size:14px;color:#7A6F60;margin-top:8px}
/* ---------- cards ---------- */
#cards{margin-top:22px}
.card{background:#FFFDF8;border:1px solid #E5DCC8;border-radius:14px;padding:20px 22px;margin:0 0 18px;box-shadow:0 2px 6px rgba(60,40,20,.07);scroll-margin-top:150px}
.card.flash{outline:3px solid #B85C38;outline-offset:2px}
.card .top{display:flex;justify-content:space-between;align-items:baseline;gap:10px;flex-wrap:wrap}
.card .num{font-family:'Caveat',cursive;font-size:26px;font-weight:700;color:#B85C38}
.tag{font-size:12.5px;padding:3px 10px;border-radius:20px;background:#F3E9DC;color:#8A5A33;border:1px solid #E5D0B8;white-space:nowrap}
.card h2{margin:2px 0 0;font-size:24px;line-height:1.3;color:#33261C}
.card .en{margin:2px 0 12px;font-style:italic;color:#8A7D6B;font-size:15px}
.puzzle{position:relative;border-left:3px solid #B85C38;background:#FBF6EC;border-radius:0 10px 10px 0;padding:12px 14px 12px 16px;margin:10px 0 14px}
.puzzle .qm{font-family:'Caveat',cursive;font-size:34px;line-height:0;color:#B85C38;vertical-align:-6px;margin-right:4px}
.puzzle p{margin:0;font-size:17.5px}
.sol-toggle{cursor:pointer;background:none;border:1px dashed #B85C38;color:#B85C38;border-radius:10px;padding:8px 14px;font-size:15px;font-family:inherit}
.sol-toggle:hover{background:#FBEFE6}
.solution{display:none;margin-top:14px;border-top:1px dashed #E5DCC8;padding-top:12px}
.solution.open{display:block}
.solution h3{margin:0 0 6px;font-size:16px;color:#B85C38;letter-spacing:.3px}
.solution ol{margin:0 0 10px;padding-left:20px}
.solution li{margin:0 0 6px;font-size:16.5px}
.src{font-size:14px;color:#7A6F60}
.src a{word-break:break-all}
.badge{display:inline-block;font-size:12px;background:#E9F3E6;color:#2F6B2A;border:1px solid #BCD8B4;border-radius:20px;padding:1px 9px;margin-left:6px;vertical-align:1px}
/* quiz */
.quiz{margin-top:14px;background:#F7F2E7;border:1px solid #EDE3CE;border-radius:10px;padding:12px 14px}
.quiz .qq{font-weight:700;margin:0 0 8px}
.quiz .opts{display:flex;flex-direction:column;gap:7px}
.quiz button.opt{cursor:pointer;text-align:left;background:#FFFDF8;border:1px solid #D8CDB6;border-radius:8px;padding:9px 12px;font-size:15.5px;font-family:inherit;color:#2B2620}
.quiz button.opt:hover{border-color:#B85C38}
.quiz button.opt.right{background:#E2F0DC;border-color:#5E9A52}
.quiz button.opt.wrong{background:#FBE3DC;border-color:#C65B45}
.quiz .fb{margin:8px 0 0;font-size:15px;min-height:1.2em}
.quiz .fb.good{color:#2F6B2A}.quiz .fb.bad{color:#A63E2B}
/* sims */
.sim{margin-top:14px;background:#F7F2E7;border:1px solid #EDE3CE;border-radius:10px;padding:14px}
.sim h3{margin:0 0 4px;font-size:16px;color:#B85C38}
.sim p.hint{margin:0 0 10px;font-size:14.5px;color:#5C5347}
.doors{display:flex;gap:10px;flex-wrap:wrap;margin:8px 0}
.door{cursor:pointer;flex:1 1 90px;min-height:96px;border:2px solid #B85C38;border-radius:10px;background:#FFFDF8;font-size:15px;font-family:inherit;color:#33261C;padding:8px}
.door .big{font-size:34px;display:block}
.door.picked{outline:3px solid #B85C38}
.door.opened{background:#EFE6D2;color:#7A6F60;border-color:#D8CDB6}
.door:disabled{cursor:default}
.sim .msg{margin:10px 0;font-size:16px;min-height:1.4em}
.sim .row{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0}
.sim input[type=number]{width:90px;padding:8px 10px;font-size:15px;font-family:inherit;border:1px solid #D8CDB6;border-radius:8px;background:#FFFDF8}
.bar{height:14px;background:#EDE3CE;border-radius:7px;overflow:hidden;margin:4px 0 10px}
.bar > div{height:100%;background:#B85C38;border-radius:7px}
.bdays{display:flex;gap:5px;flex-wrap:wrap;margin:10px 0}
.bday{background:#FFFDF8;border:1px solid #D8CDB6;border-radius:6px;padding:3px 8px;font-size:13.5px}
.bday.dup{background:#FBE3DC;border-color:#C65B45;font-weight:700}
footer{margin-top:36px;border-top:1px solid #E5DCC8;padding-top:18px;font-size:14.5px;color:#5C5347}
footer h2{font-family:'Caveat',cursive;font-size:28px;color:#33261C;margin:0 0 6px}
footer p{margin:6px 0}
.empty{display:none;text-align:center;padding:40px 10px;font-size:18px;color:#7A6F60}
.empty.show{display:block}
@media (max-width:640px){
  .card{padding:16px}
  .card h2{font-size:21px}
  .puzzle p{font-size:16.5px}
  .controls input[type=search]{flex-basis:100%}
}
</style>
</head>
<body>
<div class="wrap">
<header class="hero">
  <div class="kicker">✦ một chỗ tra cứu duy nhất, bằng tiếng Việt ✦</div>
  <h1>Nghịch lý <span class="q">?</span><br>Câu đố làm não kẹt</h1>
  <p class="sub">Đọc câu đố trước, tự nghĩ đáp án, rồi mới mở lời giải. Có quiz để thử tay, có mô phỏng để chạy thật — vì nhiều nghịch lý chỉ “ngấm” khi tự mình thấy nó xảy ra.</p>
  <div class="stats">
    <div class="stat"><b>109</b><span>nghịch lý</span></div>
    <div class="stat"><b>7</b><span>phân loại</span></div>
    <div class="stat"><b>__NQUIZ__</b><span>câu đố trắc nghiệm</span></div>
    <div class="stat"><b>2</b><span>mô phỏng chạy thật</span></div>
  </div>
  <p class="srcnote">Mọi mục đều có link Wikipedia tiếng Anh đã kiểm chứng (trả về HTTP 200 ngày 25/11/2026). Viết lại bằng tiếng Việt, không sao chép nguyên văn.</p>
</header>

<div class="controls">
  <div class="row">
    <input type="search" id="q" placeholder="Tìm nghịch lý… gõ không dấu cũng ra (vd: monty hall, theseus, sinh nhat)" aria-label="Tìm kiếm">
    <button class="btn ghost" id="randomBtn" type="button">🎲 Ngẫu nhiên</button>
  </div>
  <div class="chips" id="chips">
__CHIPS__
  </div>
  <div id="count">Đang hiện 109 / 109 nghịch lý</div>
</div>

<main id="cards"></main>
<div class="empty" id="empty">Không tìm thấy nghịch lý nào khớp. Thử từ khóa khác hoặc bấm “Tất cả”.</div>

<footer>
  <h2>Cách trang này được làm</h2>
  <p><b>Nguồn:</b> mỗi mục dựa trên bài Wikipedia tiếng Anh (link ở cuối mỗi lời giải) và được viết lại bằng tiếng Việt. Toàn bộ 106 đường link nguồn riêng biệt đã được kiểm tra còn truy cập được ngày 25/11/2026 — không có mục nào “chưa kiểm chứng”.</p>
  <p><b>Lưu ý nhỏ:</b> 6 mục trùng tên đã loại khi gộp dữ liệu (giữ bản của nhóm chính). Vài mục trỏ tới bài Wikipedia chứa mục về nghịch lý đó thay vì bài riêng — ví dụ 3 nghịch lý du hành thời gian cùng trỏ bài <i>Temporal paradox</i>, 4 nghịch lý Zeno cùng trỏ bài <i>Zeno’s paradoxes</i>. Nghịch lý Mpemba là hiệu ứng quan sát, không phải nghịch lý logic thuần túy — điều này đã ghi rõ trong lời giải của mục đó.</p>
  <p><b>Không dùng ảnh:</b> các nghịch lý được minh họa bằng chữ và mô phỏng tương tác, không dùng ảnh có bản quyền không rõ nguồn.</p>
  <p style="color:#8A7D6B">Nghịch lý — Câu đố làm não kẹt · 109 mục · Dữ liệu nguồn: data/nghich-ly.json</p>
</footer>
</div>

<script type="application/json" id="paradox-data">__DATA__</script>
<script>
"use strict";
var DATA = JSON.parse(document.getElementById("paradox-data").textContent);
var CAT_LABEL = {logic:"Logic","xac-suat":"Xác suất","thoi-gian":"Thời gian","vo-cuc":"Vô cực","tu-tham-chieu":"Tự tham chiếu","vat-ly":"Vật lý","quyet-dinh":"Quyết định"};
var state = {cat:"all", q:""};
function norm(s){return (s||"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").replace(/đ/g,"d").replace(/Đ/g,"D").toLowerCase();}
function el(tag, cls, text){var e=document.createElement(tag); if(cls)e.className=cls; if(text!=null)e.textContent=text; return e;}
function splitSentences(t){
  // Bảo vệ dấu chấm trong số kiểu 1.000 / 1.000.000 khỏi bị tách nhầm thành hết câu
  var tmp = t.replace(/(\d)\.(\d)/g, "$1\u0001$2");
  var m = tmp.match(/[^.!?]+[.!?]+["”)]?/g);
  if(!m || m.length===0) return [t];
  return m.map(function(s){return s.trim().replace(/\u0001/g, ".");});
}
function haystack(it){
  return norm([it.vi_name,it.en_name,it.puzzle,it.explanation,it.id,CAT_LABEL[it.category]||""].join(" "));
}

/* ---------- Monty Hall ---------- */
function buildMonty(box){
  box.appendChild(el("h3",null,"🎲 Thử ngay — chơi 1 ván Monty Hall"));
  box.appendChild(el("p","hint","Chọn 1 cửa. Người dẫn sẽ mở 1 cửa có dê, rồi bạn quyết định đổi hay giữ."));
  var doorsEl = el("div","doors"), msg = el("p","msg",""), btns = el("div","row");
  var doors=[], car, picked, revealed, phase="pick";
  function reset(){
    car = Math.floor(Math.random()*3); picked=null; revealed=null; phase="pick";
    doors.length=0;
    doorsEl.innerHTML=""; btns.innerHTML=""; msg.textContent="Chọn 1 trong 3 cửa:";
    for(var i=0;i<3;i++){
      (function(i){
        var d=el("button","door",""); d.type="button";
        d.innerHTML='<span class="big">🚪</span>Cửa '+(i+1);
        d.onclick=function(){pickDoor(i);}; doors.push(d); doorsEl.appendChild(d);
      })(i);
    }
  }
  function pickDoor(i){
    if(phase!=="pick")return;
    picked=i; phase="host";
    doors[i].classList.add("picked");
    var opts=[0,1,2].filter(function(j){return j!==picked && j!==car;});
    revealed = opts[Math.floor(Math.random()*opts.length)];
    doors[revealed].classList.add("opened"); doors[revealed].disabled=true;
    doors[revealed].innerHTML='<span class="big">🐐</span>Cửa '+(revealed+1)+' — dê!';
    msg.textContent="Người dẫn mở cửa "+(revealed+1)+" để lộ một con dê. Bạn đổi sang cửa còn lại, hay giữ cửa "+(picked+1)+"?";
    var bSwitch=el("button","btn","Đổi cửa"); bSwitch.type="button";
    var bStay=el("button","btn ghost","Giữ nguyên"); bStay.type="button";
    bSwitch.onclick=function(){finish(true);}; bStay.onclick=function(){finish(false);};
    btns.appendChild(bSwitch); btns.appendChild(bStay);
    doors.forEach(function(d){d.disabled=true;});
  }
  function finish(sw){
    phase="done";
    var finalDoor = sw ? [0,1,2].filter(function(j){return j!==picked && j!==revealed;})[0] : picked;
    var win = finalDoor===car;
    doors.forEach(function(d,j){
      d.disabled=true;
      d.innerHTML = j===car ? '<span class="big">🚗</span>Cửa '+(j+1)+' — Ô TÔ!' : '<span class="big">🐐</span>Cửa '+(j+1)+' — dê';
      if(j===finalDoor) d.classList.add("picked");
    });
    msg.textContent = (sw?"Bạn đã ĐỔI cửa. ":"Bạn đã GIỮ nguyên. ") + (win?"🎉 Trúng ô tô!":"Tiếc quá, sau cửa bạn chọn là dê.") + " (Đổi cửa thắng 2/3, giữ nguyên chỉ 1/3.)";
    btns.innerHTML="";
    var again=el("button","btn ghost","Chơi lại"); again.type="button"; again.onclick=reset; btns.appendChild(again);
  }
  function runSim(sw){
    var wins=0, N=100;
    for(var k=0;k<N;k++){
      var c=Math.floor(Math.random()*3), p=Math.floor(Math.random()*3);
      if(sw){ if(p!==c) wins++; } else { if(p===c) wins++; }
    }
    var res=el("div"); res.innerHTML="";
    var label=el("p",null,(sw?"Luôn ĐỔI cửa: ":"Luôn GIỮ nguyên: ")+wins+" / 100 ván thắng ("+wins+"%)");
    var bar=el("div","bar"); var fill=el("div"); fill.style.width=wins+"%"; bar.appendChild(fill);
    res.appendChild(label); res.appendChild(bar);
    var old=box.querySelector(".simres"); if(old) old.remove();
    res.className="simres"; box.appendChild(res);
  }
  var b1=el("button","btn","Chạy 100 lần: luôn ĐỔI"); b1.type="button"; b1.onclick=function(){runSim(true);};
  var b2=el("button","btn ghost","Chạy 100 lần: luôn GIỮ"); b2.type="button"; b2.onclick=function(){runSim(false);};
  box.appendChild(doorsEl); box.appendChild(msg); box.appendChild(btns);
  var r2=el("div","row"); r2.appendChild(b1); r2.appendChild(b2); box.appendChild(r2);
  reset();
}

/* ---------- Birthday ---------- */
function buildBirthday(box){
  box.appendChild(el("h3",null,"🎂 Thử ngay — sinh nhật trùng nhau"));
  box.appendChild(el("p","hint","Nhập số người trong phòng rồi thử: ngày sinh được bốc ngẫu nhiên, ngày trùng sẽ tô đỏ."));
  var row=el("div","row");
  var lab=el("span",null,"Số người:"); var inp=document.createElement("input");
  inp.type="number"; inp.min="2"; inp.max="100"; inp.value="23";
  var b1=el("button","btn","Thử 1 lần"); b1.type="button";
  var b2=el("button","btn ghost","Chạy 1000 lần"); b2.type="button";
  row.appendChild(lab); row.appendChild(inp); row.appendChild(b1); row.appendChild(b2);
  box.appendChild(row);
  var out=el("div"); box.appendChild(out);
  var DAYS=[31,28,31,30,31,30,31,31,30,31,30,31];
  function fmt(d){var m=0; while(d>=DAYS[m]){d-=DAYS[m]; m++;} return (d+1)+"/"+(m+1);}
  b1.onclick=function(){
    var n=Math.max(2,Math.min(100,parseInt(inp.value,10)||23)); inp.value=n;
    var seen={}, dups={}, arr=[];
    for(var i=0;i<n;i++){var d=Math.floor(Math.random()*365); arr.push(d); if(seen[d])dups[d]=1; seen[d]=1;}
    out.innerHTML="";
    var chips=el("div","bdays");
    arr.forEach(function(d){var c=el("span","bday"+(dups[d]?" dup":""),fmt(d)); chips.appendChild(c);});
    out.appendChild(chips);
    var cnt=Object.keys(dups).length;
    out.appendChild(el("p","msg",cnt>0?("🎯 Có "+cnt+" ngày sinh bị trùng trong "+n+" người này!"):"Không ai trùng sinh nhật trong lần này."));
  };
  b2.onclick=function(){
    var n=Math.max(2,Math.min(100,parseInt(inp.value,10)||23)); inp.value=n;
    var hit=0, N=1000;
    for(var k=0;k<N;k++){var s={}; var dup=false; for(var i=0;i<n;i++){var d=Math.floor(Math.random()*365); if(s[d]){dup=true;break;} s[d]=1;} if(dup)hit++;}
    out.innerHTML="";
    var pct=(hit/N*100);
    out.appendChild(el("p",null,"Với "+n+" người: "+hit+" / 1000 lần có trùng sinh nhật ("+pct.toFixed(1)+"%)."));
    var bar=el("div","bar"); var fill=el("div"); fill.style.width=pct+"%"; bar.appendChild(fill); out.appendChild(bar);
    out.appendChild(el("p","hint","Mốc tham khảo: 23 người ≈ 50,7% · 50 người ≈ 97% · 70 người ≈ 99,9%."));
  };
}

/* ---------- Cards ---------- */
var cardsEl=document.getElementById("cards");
var countEl=document.getElementById("count");
var emptyEl=document.getElementById("empty");
var cardNodes={};

function buildCard(it){
  var card=el("article","card"); card.id="card-"+it.id; card.dataset.cat=it.category;
  var top=el("div","top");
  top.appendChild(el("span","num",it.id.replace("NL-","#")));
  var tag=el("span","tag",CAT_LABEL[it.category]||it.category); top.appendChild(tag);
  card.appendChild(top);
  card.appendChild(el("h2",null,it.vi_name));
  card.appendChild(el("p","en",it.en_name));
  var pz=el("div","puzzle");
  var qm=el("span","qm","❝"); pz.appendChild(qm);
  var pp=el("p",null,it.puzzle); pz.appendChild(pp);
  card.appendChild(pz);

  if(it.interactive==="quiz"){
    var quiz=el("div","quiz");
    quiz.appendChild(el("p","qq","Thử trả lời: "+it.quiz_question));
    var opts=el("div","opts"); var fb=el("p","fb","");
    it.quiz_options.forEach(function(opt,i){
      var b=el("button","opt",String.fromCharCode(65+i)+". "+opt); b.type="button";
      b.onclick=function(){
        opts.querySelectorAll("button").forEach(function(x){x.classList.remove("right","wrong");});
        if(i===it.quiz_answer){ b.classList.add("right"); fb.textContent="✓ Đúng rồi! Mở lời giải bên dưới để xem vì sao."; fb.className="fb good"; }
        else { b.classList.add("wrong"); fb.textContent="✗ Chưa đúng — đáp án đúng là "+String.fromCharCode(65+it.quiz_answer)+". Mở lời giải để xem vì sao."; fb.className="fb bad"; }
      };
      opts.appendChild(b);
    });
    quiz.appendChild(opts); quiz.appendChild(fb); card.appendChild(quiz);
  }
  if(it.interactive==="monty-hall"){ var s1=el("div","sim"); buildMonty(s1); card.appendChild(s1); }
  if(it.interactive==="birthday"){ var s2=el("div","sim"); buildBirthday(s2); card.appendChild(s2); }

  var tog=el("button","sol-toggle","Mở lời giải ▸"); tog.type="button";
  var sol=el("div","solution");
  sol.appendChild(el("h3",null,"Lời giải — 3 ý chính"));
  var ol=el("ol");
  splitSentences(it.explanation).forEach(function(s){ ol.appendChild(el("li",null,s)); });
  sol.appendChild(ol);
  var src=el("p","src");
  var a=document.createElement("a"); a.href=it.source_url; a.target="_blank"; a.rel="noopener"; a.textContent="Wikipedia ↗";
  src.appendChild(document.createTextNode("Nguồn: ")); src.appendChild(a);
  var badge=el("span","badge","đã kiểm chứng"); src.appendChild(badge);
  sol.appendChild(src);
  tog.onclick=function(){
    var open=sol.classList.toggle("open");
    tog.textContent=open?"Đóng lời giải ▾":"Mở lời giải ▸";
  };
  card.appendChild(tog); card.appendChild(sol);
  cardNodes[it.id]=card;
  return card;
}

DATA.forEach(function(it){ cardsEl.appendChild(buildCard(it)); });

function applyFilter(){
  var q=norm(state.q), shown=0, firstVisible=null;
  DATA.forEach(function(it){
    var okCat = state.cat==="all" || it.category===state.cat;
    var okQ = !q || haystack(it).indexOf(q)!==-1;
    var show = okCat && okQ;
    cardNodes[it.id].style.display = show ? "" : "none";
    if(show){ shown++; if(!firstVisible) firstVisible=cardNodes[it.id]; }
  });
  countEl.textContent="Đang hiện "+shown+" / 109 nghịch lý";
  emptyEl.classList.toggle("show", shown===0);
  return firstVisible;
}

document.getElementById("q").addEventListener("input",function(e){ state.q=e.target.value; applyFilter(); });
document.querySelectorAll("#chips .chip").forEach(function(ch){
  ch.addEventListener("click",function(){
    document.querySelectorAll("#chips .chip").forEach(function(x){x.classList.remove("on");});
    ch.classList.add("on"); state.cat=ch.dataset.cat; applyFilter();
  });
});
document.getElementById("randomBtn").addEventListener("click",function(){
  var visible=DATA.filter(function(it){
    var c=cardNodes[it.id]; return c.style.display!=="none";
  });
  if(!visible.length) return;
  var pick=visible[Math.floor(Math.random()*visible.length)];
  var node=cardNodes[pick.id];
  node.scrollIntoView({behavior:"smooth",block:"center"});
  node.classList.remove("flash"); void node.offsetWidth; node.classList.add("flash");
  setTimeout(function(){node.classList.remove("flash");},2200);
});
applyFilter();
</script>
</body>
</html>
"""

HTML = HTML.replace("__NQUIZ__", str(n_quiz))
HTML = HTML.replace("__CHIPS__", CHIPS_HTML)
HTML = HTML.replace("__DATA__", DATA_JSON)

with open(OUT, "w", encoding="utf-8") as f:
    f.write(HTML)

print("wrote", OUT)
