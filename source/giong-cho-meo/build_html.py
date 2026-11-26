#!/usr/bin/env python3
"""Build giong-cho-meo.html (1 file HTML, CSS+JS inline, dữ liệu JSON inline,
ảnh tham chiếu tương đối tới photos/) từ data/breeds.json. Phong cách Letter.
Usage: python3 build_html.py
"""
import json, pathlib

BASE = pathlib.Path("/home/hatch/workspace/giong-cho-meo")
DATA = json.loads((BASE / "data" / "breeds.json").read_text(encoding="utf-8"))
NDOG = sum(1 for x in DATA if x["loai"] == "cho")
NCAT = sum(1 for x in DATA if x["loai"] == "meo")
NPHOTO = sum((1 if x.get("anh") else 0) + len(x.get("anh_phu", [])) for x in DATA)
NVIDEO = sum(1 for x in DATA if x.get("video"))
NUNVER = sum(1 for x in DATA if x["trang_thai"] != "da-kiem-chung")

# JSON inline an toàn trong <script>: chặn chuỗi đóng script
DATA_JSON = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")

HTML = """<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Giống chó và mèo — Nuôi con nào hợp nhà mình?</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Alegreya:ital,wght@0,400;0,500;0,700;1,400&family=Caveat:wght@600;700&display=swap" rel="stylesheet">
<style>
*{box-sizing:border-box}
:root{--paper:#FAF6EF;--card:#FFFDF8;--ink:#2B2118;--muted:#7A6A58;--terra:#B85C38;--terra-d:#9A4A2B;--line:#E5DCCB;--soft:#F3EBDB;--green:#3E7A4E;--amber:#A87400;--red:#A83A2A}
body{margin:0;background:var(--paper);color:var(--ink);font-family:'Alegreya',Georgia,'Times New Roman',serif;line-height:1.55}
header{background:linear-gradient(180deg,#F3E7D3,#FAF6EF);border-bottom:3px double var(--terra);padding:34px 18px 22px;text-align:center}
header h1{font-family:'Caveat',cursive;font-size:52px;line-height:1.05;margin:0;color:var(--terra-d)}
header .sub{font-size:19px;color:var(--muted);margin:8px auto 0;max-width:760px;font-style:italic}
.stats{display:flex;gap:10px;justify-content:center;flex-wrap:wrap;margin:18px auto 0;max-width:900px}
.stat{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 18px;min-width:120px;box-shadow:0 1px 3px rgba(43,33,24,.06)}
.stat b{display:block;font-size:26px;color:var(--terra-d);line-height:1.1}
.stat span{font-size:13.5px;color:var(--muted)}
.wrap{max-width:1180px;margin:0 auto;padding:0 16px 70px}
.note{background:#FFF8E6;border:1px solid #EBD9A0;border-radius:10px;padding:12px 16px;margin:18px 0;font-size:14.5px}
.note b{color:var(--terra-d)}
.controls{position:sticky;top:0;z-index:50;background:var(--paper);padding:14px 0 10px;border-bottom:1px solid var(--line)}
.controls .row{display:flex;gap:8px;flex-wrap:wrap}
.controls input[type=search]{flex:2 1 280px;padding:11px 13px;font-size:16px;font-family:inherit;border:1.5px solid var(--line);border-radius:10px;background:#fff}
.controls select{flex:1 1 150px;padding:10px 8px;font-size:15px;font-family:inherit;border:1.5px solid var(--line);border-radius:10px;background:#fff;color:var(--ink)}
.controls button{cursor:pointer;border:0;border-radius:10px;font-size:15px;font-family:inherit;padding:10px 16px;background:var(--terra);color:#fff;font-weight:700}
.controls button.ghost{background:#fff;color:var(--terra-d);border:1.5px solid var(--terra)}
#count{font-size:15px;color:var(--muted);margin-top:9px}
#count b{color:var(--terra-d)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:20px;margin-top:20px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;overflow:hidden;box-shadow:0 2px 8px rgba(43,33,24,.07);display:flex;flex-direction:column;scroll-margin-top:170px}
.card.flash{outline:3px solid var(--terra)}
.photo{position:relative;aspect-ratio:4/3;background:var(--soft);overflow:hidden}
.photo img{width:100%;height:100%;object-fit:cover;display:block}
.photo .nophoto{width:100%;height:100%;display:flex;align-items:center;justify-content:center;flex-direction:column;color:var(--muted);font-style:italic;font-size:17px;gap:4px}
.photo .nophoto small{font-size:13px}
.badge-kind{position:absolute;top:10px;left:10px;background:rgba(43,33,24,.82);color:#FFF6E8;font-size:12.5px;font-weight:700;letter-spacing:.08em;padding:4px 10px;border-radius:20px}
.badge-fci{position:absolute;top:10px;right:10px;background:rgba(184,92,56,.92);color:#fff;font-size:12.5px;font-weight:700;padding:4px 10px;border-radius:20px}
.body{padding:16px 18px 14px;display:flex;flex-direction:column;gap:9px;flex:1}
.body h2{margin:0;font-size:21px;line-height:1.25}
.body h2 .vi{display:block;font-size:15px;color:var(--muted);font-weight:500;font-style:italic}
.tags{display:flex;gap:6px;flex-wrap:wrap}
.tag{font-size:12.5px;padding:2px 9px;border-radius:20px;background:var(--soft);color:#5C4A33;border:1px solid var(--line)}
.tag.warn{background:#FDECEA;color:var(--red);border-color:#F0C4BC}
.tag.ok{background:#EAF3EC;color:var(--green);border-color:#C4DCC9}
.desc{font-size:15px;margin:0}
.facts{font-size:14.5px;border-top:1px dashed var(--line);padding-top:9px;display:grid;grid-template-columns:1fr 1fr;gap:3px 12px}
.facts div b{color:var(--terra-d);font-weight:700}
.facts .full{grid-column:1/-1}
.traits{display:flex;gap:6px;flex-wrap:wrap}
.trait{font-size:13px;background:#F6EDE0;border:1px solid var(--line);border-radius:16px;padding:2px 10px}
.src{font-size:13px;color:var(--muted);border-top:1px dashed var(--line);padding-top:8px;margin-top:auto}
.src a{color:var(--terra-d)}
.credit{font-size:12px;color:#9A8A76}
.thumbs{display:flex;gap:6px;padding:8px 10px;background:var(--soft);overflow-x:auto}
.thumb{flex:0 0 auto;width:56px;height:42px;object-fit:cover;border-radius:6px;border:2px solid transparent;cursor:pointer;padding:0;background:none}
.thumb.active{border-color:var(--terra)}
.video{margin:0;background:#1F1710}
.video video{width:100%;display:block;max-height:320px}
.video .vcredit{font-size:12px;color:#D8C9B4;padding:6px 10px}
details.v2{border-top:1px dashed var(--line);padding-top:9px}
details.v2 summary{cursor:pointer;color:var(--terra-d);font-weight:700;font-size:15px;list-style:none}
details.v2 summary::-webkit-details-marker{display:none}
details.v2 summary::before{content:"＋ ";color:var(--terra)}
details.v2[open ] summary::before{content:"－ "}
.v2sec{margin-top:10px;font-size:14.5px}
.v2sec h3{margin:0 0 3px;font-size:15px;color:var(--terra-d)}
.v2sec p{margin:0}
.v2sec ul{margin:2px 0 0;padding-left:18px}
.v2sec li{margin-bottom:3px}
.friend{display:grid;grid-template-columns:auto 1fr;gap:2px 10px;font-size:14.5px}
.friend b{color:var(--terra-d)}
.unver-tag{display:inline-block;font-size:12px;font-weight:700;color:var(--red);background:#FDECEA;border:1px solid #F0C4BC;border-radius:12px;padding:1px 8px;margin-left:6px;vertical-align:middle}
.empty{text-align:center;padding:50px 10px;color:var(--muted);font-size:18px;font-style:italic}
footer{max-width:1180px;margin:0 auto;padding:0 16px 40px;color:var(--muted);font-size:14px}
footer a{color:var(--terra-d)}
@media(max-width:560px){header h1{font-size:38px}.grid{grid-template-columns:1fr}}
</style>
</head>
<body>
<header>
<h1>Nuôi con nào hợp nhà mình?</h1>
<p class="sub">Một chỗ tra cứu duy nhất bằng tiếng Việt: giống chó &amp; giống mèo — kích cỡ, tính cách, rụng lông, vận động, có hợp chung cư không, tuổi thọ — kèm ảnh thật từng giống. Mỗi giống có 3–5 ảnh thật, một số giống có cả video, bấm “Xem chi tiết đầy đủ” để đọc nguồn gốc, ngoại hình, tính cách chi tiết, sức khỏe và lưu ý khi nuôi ở Việt Nam.</p>
<div class="stats">
<div class="stat"><b>__TOTAL__</b><span>giống</span></div>
<div class="stat"><b>__DOGS__</b><span>giống chó (FCI)</span></div>
<div class="stat"><b>__CATS__</b><span>giống mèo</span></div>
<div class="stat"><b>__PHOTOS__</b><span>ảnh thật</span></div>
<div class="stat"><b>__VIDEOS__</b><span>giống có video</span></div>
</div>
</header>
<div class="wrap">
<div class="note"><b>Cách dùng:</b> gõ tên không dấu vào ô tìm kiếm (vd “cho phu quoc”, “meo ba tu”, “husky”), rồi lọc theo kích cỡ, tính cách, rụng lông, nhu cầu vận động và hợp chung cư. Bấm vào ảnh nhỏ dưới ảnh chính để xem các ảnh khác của giống; giống nào có video sẽ hiện trình phát ngay dưới ảnh. Số liệu lấy từ Wikipedia tiếng Anh, chuẩn FCI, AKC, CFA/TICA, PetMD/VCA. <b>__UNVER__ mục ghi rõ “chưa kiểm chứng”</b> ở trường nào chưa có số liệu công bố — trang không bịa số. Riêng mục “Lưu ý khi nuôi ở Việt Nam” của mọi giống đều là suy luận chưa có nguồn riêng, đã ghi rõ trong từng thẻ.</div>
<div class="controls">
<div class="row">
<input type="search" id="q" placeholder="Tìm giống chó, mèo… (không cần gõ dấu)" autocomplete="off">
<select id="fLoai" aria-label="Loài"><option value="">Tất cả: chó &amp; mèo</option><option value="cho">Chó</option><option value="meo">Mèo</option></select>
<select id="fSize" aria-label="Kích cỡ"><option value="">Kích cỡ: tất cả</option><option value="Nho">Nhỏ</option><option value="Vua">Vừa</option><option value="Lon">Lớn</option><option value="Khong lo">Khổng lồ</option></select>
<select id="fTrait" aria-label="Tính cách"><option value="">Tính cách: tất cả</option></select>
<select id="fShed" aria-label="Rụng lông"><option value="">Rụng lông: tất cả</option><option value="It">Ít</option><option value="Trung binh">Trung bình</option><option value="Nhieu">Nhiều</option></select>
<select id="fEx" aria-label="Vận động"><option value="">Vận động: tất cả</option><option value="Thap">Thấp</option><option value="Trung binh">Trung bình</option><option value="Cao">Cao</option></select>
<select id="fApt" aria-label="Hợp chung cư"><option value="">Chung cư: tất cả</option><option value="Co">Hợp chung cư</option><option value="Han che">Hạn chế</option><option value="Khong">Không hợp</option></select>
</div>
<div class="row" style="margin-top:8px">
<select id="fSort" aria-label="Sắp xếp"><option value="az">Sắp xếp: tên A – Z</option><option value="size">Kích cỡ: nhỏ → lớn</option><option value="shed">Ít rụng lông trước</option></select>
<button id="btnRandom" type="button">Giống ngẫu nhiên</button>
<button id="btnClear" type="button" class="ghost">Xóa lọc</button>
</div>
<div id="count"></div>
</div>
<div class="grid" id="grid"></div>
<div class="empty" id="empty" hidden>Không tìm thấy giống nào khớp bộ lọc. Thử bỏ bớt một điều kiện nhé.</div>
</div>
<footer>
<p><b>Nguồn dữ liệu:</b> Wikipedia tiếng Anh (mỗi giống có link trong thẻ), chuẩn giống FCI, AKC, CFA/TICA, PetMD/VCA. Ảnh thật và video từ Wikimedia Commons (public domain / CC), giấy phép và tác giả ghi trong từng thẻ — bấm vào tên file ảnh để xem trang gốc. Ảnh nào chưa tìm được đúng giống thì thẻ ghi rõ “chưa có ảnh”, không gắn ảnh sai. 5 giống hiện chưa có ảnh nào: Bohemian Rex, Cashmere, Exotic Longhair, Korn Ja, York Chocolate.</p>
<p><b>Lưu ý:</b> rụng lông / vận động / hợp chung cư là phân loại dựa trên mô tả lông, năng lượng và mục đích sử dụng của giống trong nguồn — không phải số đo tuyệt đối. Cân nặng, chiều cao, tuổi thọ chỉ ghi khi có số liệu công bố; không có thì ghi “chưa kiểm chứng”. Trước khi đón một bé về nhà, hãy kiểm tra lại với trại giống / bác sĩ thú y.</p>
</footer>
<script>
const DATA = __DATA_JSON__;
const SIZE_ORDER = {"Nho":0,"Vua":1,"Lon":2,"Khong lo":3};
const SHED_ORDER = {"It":0,"Trung binh":1,"Nhieu":2};
function norm(s){return (s||"").normalize("NFD").replace(/[̀-ͯ]/g,"").replace(/đ/g,"d").replace(/Đ/g,"D").toLowerCase();}
function esc(s){return String(s==null?"":s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");}
const grid=document.getElementById("grid"), countEl=document.getElementById("count"), emptyEl=document.getElementById("empty");
const qEl=document.getElementById("q");
// Tính cách: 30 trait phổ biến nhất
const traitCount={};
DATA.forEach(b=>(b.tinh_cach||[]).forEach(t=>traitCount[t]=(traitCount[t]||0)+1));
const traitSel=document.getElementById("fTrait");
Object.entries(traitCount).sort((a,b)=>b[1]-a[1]).slice(0,30).forEach(([t,n])=>{
  const o=document.createElement("option"); o.value=t; o.textContent=t+" ("+n+")"; traitSel.appendChild(o);
});
function aptLabel(v){return v==="Co"?"Hợp chung cư":v==="Han che"?"Hạn chế ở chung cư":"Không hợp chung cư";}
function aptClass(v){return v==="Co"?"ok":v==="Han che"?"":"warn";}
function friendRow(label, f){
  if(!f) return "";
  const m = f.muc || "Chưa kiểm chứng";
  const note = f.ghi_chu ? " — "+esc(f.ghi_chu) : "";
  return '<div><b>'+label+':</b></div><div>'+esc(m)+note+'</div>';
}
function v2details(b){
  const og = b.nguon_goc||{}, oh = b.ngoai_hinh||{}, vd = b.van_dong_phut_ngay||{},
    sk = b.suc_khoe||{}, hv = b.hop_voi_ai||{}, vn = b.luu_y_viet_nam||{};
  const colors = (oh.mau_pho_bien||[]).map(esc).join(", ");
  const diseases = (sk.benh_thuong_gap||[]).length
    ? '<ul>'+sk.benh_thuong_gap.map(d=>'<li><b>'+esc(d.benh)+'</b>'+(d.ghi_chu?' — '+esc(d.ghi_chu):'')+'</li>').join("")+'</ul>'
    : '<p>Chưa có bệnh nào được nguồn liệt kê — không bịa bệnh.</p>';
  const mins = vd.phut_toi_thieu!=null ? "tối thiểu <b>"+esc(vd.phut_toi_thieu)+" phút/ngày</b>" : "chưa có số phút chuẩn từ nguồn";
  const unver2 = b.ghi_chu_chua_kiem_chung_v2 ? '<div class="v2sec"><h3>Chưa kiểm chứng (v2)</h3><p>'+esc(b.ghi_chu_chua_kiem_chung_v2)+'</p></div>' : "";
  return '<details class="v2"><summary>Xem chi tiết đầy đủ</summary>'
    +'<div class="v2sec"><h3>Nguồn gốc</h3><p><b>Xuất xứ:</b> '+esc(og.xuat_xu||"Chưa kiểm chứng")+'. '+esc(og.lich_su||"")+(og.muc_dich_ban_dau?' <b>Mục đích ban đầu:</b> '+esc(og.muc_dich_ban_dau):'')+'</p></div>'
    +'<div class="v2sec"><h3>Ngoại hình</h3><p>'+esc(oh.dac_diem_nhan_dang||"")+'</p>'
    +(oh.long?'<p><b>Lông:</b> '+esc(oh.long)+'</p>':'')
    +(colors?'<p><b>Màu phổ biến:</b> '+colors+'</p>':'')
    +(oh.tai?'<p><b>Tai:</b> '+esc(oh.tai)+'</p>':'')
    +(oh.duoi?'<p><b>Đuôi:</b> '+esc(oh.duoi)+'</p>':'')+'</div>'
    +'<div class="v2sec"><h3>Tính cách chi tiết</h3><p>'+esc(b.tinh_cach_chi_tiet||"Chưa kiểm chứng")+'</p></div>'
    +'<div class="v2sec"><h3>Thân thiện</h3><div class="friend">'
    +friendRow("Với trẻ em", b.than_thien_tre_em)+friendRow("Với vật khác", b.than_thien_vat_khac)+friendRow("Với người lạ", b.than_thien_nguoi_la)
    +'</div></div>'
    +'<div class="v2sec"><h3>Mức độ sủa</h3><p>'+esc((b.muc_do_sua||{}).muc||"Chưa kiểm chứng")+(b.muc_do_sua&&b.muc_do_sua.ghi_chu?' — '+esc(b.muc_do_sua.ghi_chu):'')+'</p></div>'
    +'<div class="v2sec"><h3>Huấn luyện</h3><p>'+esc(b.huan_luyen||"Chưa kiểm chứng")+'</p></div>'
    +'<div class="v2sec"><h3>Vận động</h3><p>'+mins+(vd.hoat_dong_goi_y?' — gợi ý: '+esc(vd.hoat_dong_goi_y):'')+(vd.ghi_chu?' ('+esc(vd.ghi_chu)+')':'')+'</p></div>'
    +'<div class="v2sec"><h3>Chăm sóc lông</h3><p>'+esc(b.cham_soc_long||"Chưa kiểm chứng")+'</p></div>'
    +'<div class="v2sec"><h3>Sức khỏe</h3>'+diseases+(sk.ghi_chu?'<p>'+esc(sk.ghi_chu)+'</p>':'')+'</div>'
    +'<div class="v2sec"><h3>Ăn uống</h3><p>'+esc(b.an_uong||"Chưa kiểm chứng")+'</p></div>'
    +'<div class="v2sec"><h3>Hợp với ai</h3><p><b>Phù hợp:</b> '+esc(hv.phu_hop||"Chưa kiểm chứng")+'</p><p><b>Cân nhắc kỹ:</b> '+esc(hv.can_nhac_ky||"—")+'</p></div>'
    +'<div class="v2sec"><h3>Lưu ý khi nuôi ở Việt Nam<span class="unver-tag">CHƯA KIỂM CHỨNG</span></h3><p>'+esc(vn.noi_dung||"Chưa kiểm chứng")+'</p></div>'
    +unver2
    +'</details>';
}
function card(b){
  const extras = (b.anh_phu||[]);
  const allPhotos = (b.anh?[b.anh]:[]).concat(extras);
  const main = allPhotos.length
    ? '<img class="mainimg" src="'+esc(allPhotos[0].file)+'" alt="Ảnh '+esc(b.ten_en)+'" loading="lazy">'
    : '<div class="nophoto"><span>Chưa có ảnh</span><small>chưa tìm được ảnh đúng giống này</small></div>';
  const thumbs = allPhotos.length
    ? '<div class="thumbs">'
      + allPhotos.map((p,i)=>'<img class="thumb'+(i===0?' active':'')+'" src="'+esc(p.file)+'" data-full="'+esc(p.file)+'" alt="" loading="lazy">').join("")
      + '</div>' : "";
  const video = b.video
    ? '<div class="video"><video controls preload="metadata" poster="'+esc(allPhotos.length?allPhotos[0].file:"")+'"><source src="'+esc(b.video.file)+'" type="video/webm"></video><div class="vcredit">Video: <a href="'+esc(b.video.commons_url)+'" target="_blank" rel="noopener" style="color:#E8D9BE">'+esc(b.video.file.split("/").pop())+'</a> · '+esc(b.video.license)+(b.video.tac_gia?" · "+esc(b.video.tac_gia.replace(/<[^>]*>/g,"")):"")+'</div></div>' : "";
  const fci = (b.loai==="cho"&&b.fci_group)?'<span class="badge-fci">FCI nhóm '+b.fci_group+'</span>':'';
  const unver = b.trang_thai!=="da-kiem-chung"
    ? '<span class="tag warn" title="'+esc(b.ghi_chu_chua_kiem_chung||"Một số số liệu chưa kiểm chứng")+'">Một số số liệu chưa kiểm chứng</span>' : "";
  const credit = b.anh ? '<div class="credit">Ảnh: <a href="'+esc(b.anh.commons_url)+'" target="_blank" rel="noopener">'+esc(b.anh.file.split("/").pop())+'</a> · '+esc(b.anh.license)+(b.anh.tac_gia?" · "+esc(b.anh.tac_gia.replace(/<[^>]*>/g,"")):"")+'</div>' : "";
  const extraCredit = extras.length ? '<div class="credit">Ảnh thêm: '+extras.map(p=>'<a href="'+esc(p.commons_url)+'" target="_blank" rel="noopener">'+esc(p.file.split("/").pop())+'</a> ('+esc(p.license)+')').join(" · ")+'</div>' : "";
  const srcs = (b.nguon||[]).map(u=>'<a href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(u.includes("wikipedia")?"Wikipedia":u.includes("fci.be")?"FCI":u.includes("akc.org")?"AKC":u.includes("cfa.org")?"CFA":u.includes("tica.org")?"TICA":u.includes("petmd")?"PetMD":u.includes("vcahospitals")?"VCA":"Nguồn")+'</a>').join(" · ");
  const srcs2 = (b.nguon_moi||[]).map(u=>'<a href="'+esc(u)+'" target="_blank" rel="noopener">'+esc(u.includes("wikipedia")?"Wikipedia":u.includes("fci.be")?"FCI":u.includes("akc.org")?"AKC":u.includes("cfa.org")?"CFA":u.includes("tica.org")?"TICA":u.includes("petmd")?"PetMD":u.includes("vcahospitals")?"VCA":"Nguồn")+'</a>').join(" · ");
  return '<article class="card" id="'+esc(b.id)+'" data-id="'+esc(b.id)+'">'
    +'<div class="photo">'+main+'<span class="badge-kind">'+(b.loai==="cho"?"CHÓ":"MÈO")+'</span>'+fci+'</div>'
    +thumbs+video
    +'<div class="body"><h2>'+esc(b.ten_en)+(b.ten_vi?'<span class="vi">'+esc(b.ten_vi)+'</span>':'')+'</h2>'
    +'<div class="tags"><span class="tag">Kích cỡ: '+esc({Nho:"Nhỏ",Vua:"Vừa",Lon:"Lớn","Khong lo":"Khổng lồ"}[b.kich_co]||b.kich_co)+'</span>'
    +'<span class="tag">Rụng lông: '+esc({It:"Ít","Trung binh":"Trung bình",Nhieu:"Nhiều"}[b.rung_long]||b.rung_long)+'</span>'
    +'<span class="tag">Vận động: '+esc({Thap:"Thấp","Trung binh":"Trung bình",Cao:"Cao"}[b.van_dong]||b.van_dong)+'</span>'
    +'<span class="tag '+aptClass(b.hop_chung_cu)+'">'+esc(aptLabel(b.hop_chung_cu))+'</span>'+unver+'</div>'
    +'<p class="desc">'+esc(b.mo_ta_ngan)+'</p>'
    +'<div class="facts"><div><b>Cân nặng:</b> '+esc(b.can_nang)+'</div><div><b>Chiều cao:</b> '+esc(b.chieu_cao)+'</div><div class="full"><b>Tuổi thọ:</b> '+esc(b.tuoi_tho)+'</div></div>'
    +'<div class="traits">'+(b.tinh_cach||[]).map(t=>'<span class="trait">'+esc(t)+'</span>').join("")+'</div>'
    +v2details(b)
    +'<div class="src">Nguồn: '+srcs+(srcs2?'<br>Nguồn chi tiết (v2): '+srcs2:'')+'<br>'+credit+extraCredit+'</div>'
    +'</div></article>';
}
function current(){
  const q=norm(qEl.value.trim());
  const loai=document.getElementById("fLoai").value, size=document.getElementById("fSize").value,
    trait=traitSel.value, shed=document.getElementById("fShed").value,
    ex=document.getElementById("fEx").value, apt=document.getElementById("fApt").value,
    sort=document.getElementById("fSort").value;
  let list=DATA.filter(b=>{
    if(loai&&b.loai!==loai) return false;
    if(size&&b.kich_co!==size) return false;
    if(trait&&!(b.tinh_cach||[]).includes(trait)) return false;
    if(shed&&b.rung_long!==shed) return false;
    if(ex&&b.van_dong!==ex) return false;
    if(apt&&b.hop_chung_cu!==apt) return false;
    if(q){
      const hay=norm([b.ten_en,b.ten_vi,b.mo_ta_ngan,(b.tinh_cach||[]).join(" "),
        b.tinh_cach_chi_tiet||"", (b.nguon_goc||{}).xuat_xu||"", (b.hop_voi_ai||{}).phu_hop||""].join(" "));
      if(!hay.includes(q)) return false;
    }
    return true;
  });
  if(sort==="size") list.sort((a,b)=>SIZE_ORDER[a.kich_co]-SIZE_ORDER[b.kich_co]||a.ten_en.localeCompare(b.ten_en));
  else if(sort==="shed") list.sort((a,b)=>SHED_ORDER[a.rung_long]-SHED_ORDER[b.rung_long]||a.ten_en.localeCompare(b.ten_en));
  else list.sort((a,b)=>a.ten_en.localeCompare(b.ten_en));
  return list;
}
function render(){
  const list=current();
  grid.innerHTML=list.map(card).join("");
  countEl.innerHTML="Hiển thị <b>"+list.length+"</b> / "+DATA.length+" giống";
  emptyEl.hidden=list.length>0;
}
grid.addEventListener("click",e=>{
  const t=e.target.closest(".thumb"); if(!t) return;
  const cardEl=t.closest(".card"); if(!cardEl) return;
  const main=cardEl.querySelector(".mainimg"); if(!main) return;
  main.src=t.dataset.full;
  cardEl.querySelectorAll(".thumb").forEach(x=>x.classList.remove("active"));
  t.classList.add("active");
});
["q","fLoai","fSize","fTrait","fShed","fEx","fApt","fSort"].forEach(id=>{
  document.getElementById(id).addEventListener("input",render);
  document.getElementById(id).addEventListener("change",render);
});
document.getElementById("btnClear").addEventListener("click",()=>{
  qEl.value=""; ["fLoai","fSize","fTrait","fShed","fEx","fApt"].forEach(id=>document.getElementById(id).value="");
  document.getElementById("fSort").value="az"; render();
});
document.getElementById("btnRandom").addEventListener("click",()=>{
  const list=current(); if(!list.length) return;
  const b=list[Math.floor(Math.random()*list.length)];
  const el=document.getElementById(b.id);
  if(el){ if(typeof el.scrollIntoView==="function") el.scrollIntoView({behavior:"smooth",block:"center"}); el.classList.add("flash"); setTimeout(()=>el.classList.remove("flash"),2200); }
});
render();
</script>
</body>
</html>
"""

html = (HTML
        .replace("__TOTAL__", str(len(DATA)))
        .replace("__DOGS__", str(NDOG))
        .replace("__CATS__", str(NCAT))
        .replace("__PHOTOS__", str(NPHOTO))
        .replace("__VIDEOS__", str(NVIDEO))
        .replace("__UNVER__", str(NUNVER))
        .replace("__DATA_JSON__", DATA_JSON))

out = BASE / "giong-cho-meo.html"
out.write_text(html, encoding="utf-8")
print(f"OK -> {out} ({out.stat().st_size} byte) | {len(DATA)} giong (cho {NDOG}, meo {NCAT}), anh {NPHOTO}")
