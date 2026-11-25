# D5 — Ghi chú batch (Peruvian Hairless Dog → Shar Pei, 60 giống)

- File đầu ra: `batches/D5.json` (60 mục, JSON hợp lệ, đúng schema trong `batches/README.md`).
- Ảnh: 59/60 đã tải về `photos/` (tổng ~12 MB, đều là ảnh chính từ trang Wikipedia của chính giống đó, giấy phép PD/CC, có ghi commons_url + license + tác giả từng ảnh).
- 1 giống CHƯA CÓ ẢNH: **Rafeiro do Alentejo** — ảnh chính trên Wikipedia có giấy phép "Copyrighted free use" (không phải CC/PD) nên không tải, `anh: null` + ghi rõ lý do trong mục. Không gắn ảnh sai.
- Ảnh `cho-serbian-tricolour-hound.jpg` gốc trên Commons là GIF 367×271 — đã convert sang JPEG thật (vẫn 367×271, là ảnh duy nhất của giống trên trang Wikipedia).

## Nguồn đã dùng (đều kiểm chứng được)
- Wikipedia EN: danh sách gốc Category:FCI breeds (357 giống); infobox + bài viết từng giống (cân nặng, chiều cao, tuổi thọ, tính cách, tiêu chuẩn FCI).
- AKC (akc.org): 33/60 giống khớp (31 qua slug + 2 vá tay: Great Pyrenees, Peruvian Inca Orchid) — lấy chiều cao/cân nặng/tuổi thọ + điểm rụng lông (1–5), năng lượng (1–5), sủa, dễ huấn luyện.
- FCI: link tiêu chuẩn từng giống trong trường `nguon` (mã `gXX` trong link cho biết nhóm FCI; 7 giống link .doc không ghi nhóm → gán nhóm theo phân loại FCI chuẩn, có ghi chú trong mục: Polish Greyhound 10, Pomeranian 5, Russian Toy 9, Saluki 10, Sarail Hound 10, Schillerstövare 6, Schweizerischer Niederlaufhund 6).

## Nguồn bị chặn / không dùng được
- DogTime.com: 403 (ngày 25/11/2026) — không lấy được tuổi thọ/cân nặng bổ sung cho các giống hiếm.
- FCI website (fci.be): phản hồi rất chậm, không cào được danh mục theo nhóm — dùng link tiêu chuẩn trong infobox Wikipedia thay thế.

## Chưa kiểm chứng (đã ghi rõ trong từng mục, trang_thai = chua-kiem-chung-phan)
- 17/60 mục `da-kiem-chung`, 43/60 `chua-kiem-chung-phan`.
- Tuổi thọ chưa kiểm chứng: 24/60 (chủ yếu giống hiếm: toàn bộ họ Segugio, Posavac, Schweizer Laufhund, Podenco Canario, Ratonero Valenciano, Rastreador Brasileiro, Russo-European Laika, Saarloos, Sabueso, Saint Miguel, Petit Bleu de Gascogne, Poitevin, Polish Hound, Polish Greyhound, Portuguese Water Dog, Pyrenean... — xem từng mục).
- Cân nặng chưa kiểm chứng: 14/60. Chiều cao chưa kiểm chứng: 15/60.
- Tính cách: 30/60 có mục Temperament trên Wikipedia; 30/60 còn lại suy luận từ mô tả giống + điểm AKC và đã ghi rõ "suy luận" trong ghi_chu.
- rung_long/van_dong/hop_chung_cu: theo điểm AKC khi có (33 giống); còn lại suy luận từ mô tả lông/vai trò giống, đã ghi rõ trong ghi_chu.
- Số đo gộp nhiều dòng (ghi rõ trong ghi_chu): Poodle (Toy/Miniature/Standard), Portuguese Podengo (chỉ dòng Pequeno), Peruvian Hairless Dog (3 cỡ).
- Số liệu mâu thuẫn giữa 2 nguồn, đã ghi cả hai: Pomeranian chiều cao (AKC 15–18 cm vs Wikipedia 18–30 cm); Rottweiler tuổi thọ (Wikipedia 8–10 vs AKC 9–10); Schipperke tuổi thọ (dùng AKC 12–16, bỏ số 19 trích lỗi từ Wikipedia); Pumi tuổi thọ (Wikipedia 14 vs AKC 12–13 → ghi 12–14).

## Giống đặc biệt
- Rastreador Brasileiro: không có số đo nào trong nguồn kiểm chứng được; không khẳng định tình trạng tuyệt chủng vì bài Wikipedia trích được không ghi rõ.
- Không bỏ giống nào trong danh sách 60 giống.

## File làm việc (audit trail)
- `batches/D5_list.json` — danh sách 60 giống gốc.
- `batches/D5_raw.json` — summary + ảnh + infobox thô từng giống (Wikipedia).
- `batches/D5_raw2.json` — infobox đã parse (cân nặng/chiều cao/tuổi thọ/tính cách/nhóm FCI).
- `batches/D5_full.json` — trích từ toàn văn bài Wikipedia (số đo/tính cách bổ sung).
- `batches/D5_akc.json` — dữ liệu AKC (33 giống).
- `batches/D5_merged.json` — hợp nhất các nguồn, đã chuẩn hoá kg/cm/năm.
- `batches/d5_collect.py`, `d5_enrich3.py`, `d5_fulltext.py`, `d5_akc.py`, `d5_merge.py` — script cào (log trong `d5_collect.log`, `d5_enrich*.log`, `d5_fulltext.log`, `d5_akc.log`).
- Các file `D5_part2/3/4.json` là bản nháp trung gian, đã merge xong vào `D5.json` và đã xoá.
