# DGAP — Ghi chú lấp khoảng trống (gap-fill), 25/11/2026

## 1. Đối chiếu: FCI chính thức có bao nhiêu giống, thiếu bao nhiêu

- **Nguồn đối chiếu A — FCI chính thức (fci.be, tải trực tiếp 10 trang nhóm 25/11): 344 chuẩn giống**
  (nhóm 1: 43, 2: 53, 3: 34, 4: 1, 5: 46, 6: 70, 7: 36, 8: 22, 9: 26, 10: 13).
  Lưu ý: 344 là số *chuẩn* FCI; FCI hay được trích dẫn là "~360 giống" vì một số chuẩn có nhiều biến thể
  (vd Belgian Shepherd 4 biến thể, Dachshund 9 biến thể) — dự án này đếm 1 mục / 1 bài Wikipedia như các batch khác.
- **Nguồn đối chiếu B — Wikipedia EN "List of dog breeds" (extant): 557 mục** (gồm cả giống không thuộc FCI,
  giống lai/designer, type) — chỉ dùng để kiểm tra sự tồn tại của bài viết, không dùng làm danh sách FCI.
- **Đã có trước DGAP: 356 mục** (D1–D4: 239 mục JSON + D5/D6 list: 117 tên; tổng số này khớp 357 trang
  Category:FCI breeds trừ 1 trang list "List of Hungarian dog breeds" mà D4 đã loại đúng).

### Phương pháp đối chiếu
1. Trích tên + số chuẩn từ 10 trang nhóm FCI → đối chiếu với 356 mục đã có bằng chuẩn hóa tên
   (gỡ dấu tiếng Việt/Pháp/Đức kiểu NFKD, gạch nối → khoảng trắng, bỏ "(dog breed)"/"dog" cuối).
2. 81 tên FCI không khớp trực tiếp → phân giải qua Wikipedia API (redirects) + tra cứu từng tên:
   đa số là **khác tên gọi** (tên FCI tiếng Anh vs tên bài Wikipedia): vd Beauce Sheepdog = Beauceron,
   Collie Rough = Rough Collie, Mastiff = English Mastiff, Shiba = Shiba Inu, Kai = Kai Ken,
   French Pointing Dog (Gascogne/Pyrenean) = Braque Français, v.v.
3. Với 81 tên này, đã **kiểm chứng từng tên bằng số chuẩn FCI trong infobox bài Wikipedia** (`fcistd`):
   73/81 khớp số chuẩn (vd Beauceron = 044, Rough Collie = 156); các trường hợp đặc biệt xem mục 3.

### Kết quả: FCI thiếu thật sự: 7 giống → đã bổ sung đủ 7 trong DGAP.json
| # | Giống | FCI | Nhóm | Vì sao thiếu trong danh sách gốc |
|---|-------|-----|------|----------------------------------|
| 1 | Dachshund | 148 | 4 | Bài Wikipedia không nằm trong Category:FCI breeds → cả nhóm 4 vắng mặt |
| 2 | Cardigan Welsh Corgi | 38 | 1 | Không nằm trong Category:FCI breeds |
| 3 | Austrian Pinscher | 64 | 2 | Không nằm trong Category:FCI breeds |
| 4 | Dutch Smoushond | 308 | 2 | Không nằm trong Category:FCI breeds |
| 5 | Hokkaido | 261 | 5 | Không nằm trong Category:FCI breeds (bài là "Hokkaido (dog breed)") |
| 6 | Taiwan Dog | 348 | 5 | Không nằm trong Category:FCI breeds |
| 7 | Deutsch Stichelhaar | 232 | 7 | Không có bài Wikipedia EN, cũng không có trong "List of dog breeds" |

### KHÔNG bổ sung (đã có, chỉ khác tên) — ghi rõ để coordinator khỏi rà lại
- **American Akita (FCI 344)**: Wikipedia EN redirect về bài "Akita (dog breed)" — đã có mục `cho-akita` (D1).
  Cùng tiền lệ với Braque Français (2 chuẩn 133/134 = 1 mục), Pyrenean Sheepdog (2 chuẩn 138/141 = 1 mục),
  Belgian Shepherd (4 biến thể = 1 mục).
- **Griffon Belge (FCI 81) và Petit Brabançon (FCI 82)**: Wikipedia EN redirect về bài "Griffon Bruxellois"
  — đã có mục `cho-griffon-bruxellois`. Không tách riêng, đúng tiền lệ trên.
  (Lưu ý: infobox bài Griffon Bruxellois ghi chuẩn 080; nếu sau này muốn tách 3 giống thì cần dữ liệu từ PDF chuẩn FCI 081/082 — PDF đã tải sẵn trong `dgap_work/`.)
- Braque Français chuẩn 134, Pyrenean Sheepdog chuẩn 141: cùng bài với chuẩn 133/138 — đã có, không tách.

## 2. Bonus ngoài FCI: Phu Quoc Ridgeback (1 mục)
- Có bài Wikipedia EN riêng ("Phu Quoc Ridgeback"), được Hiệp hội Chó giống Việt Nam (VKA) công nhận,
  KHÔNG thuộc FCI (bài Wikipedia ghi rõ). Đã thêm với `fci_group: null` + ghi rõ không thuộc FCI trong mô tả
  và ghi chú. Tên tiếng Việt "Chó Phú Quốc" là tên gọi thông dụng thật.

## 3. Những gì "chưa kiểm chứng" (6/8 mục `chua-kiem-chung-phan`)
- **Austrian Pinscher**: cân nặng + tuổi thọ (không có trong bài Wikipedia lẫn chuẩn FCI).
- **Dutch Smoushond**: tuổi thọ (không có trong bài Wikipedia lẫn chuẩn FCI).
- **Hokkaido**: tuổi thọ (không có trong bài Wikipedia lẫn chuẩn FCI); cân nặng chỉ "khoảng 20 kg" theo bài viết.
- **Taiwan Dog**: tuổi thọ (không có trong bài Wikipedia lẫn chuẩn FCI).
- **Deutsch Stichelhaar**: cân nặng + tuổi thọ (chuẩn FCI không công bố; không có bài Wikipedia).
- **Phu Quoc Ridgeback**: tuổi thọ (không có trong bài Wikipedia).
- Dachshund + Cardigan: `da-kiem-chung` (tuổi thọ theo nghiên cứu Anh 2024: Dachshund 13,2 / miniature 14;
  Cardigan 13,1; nghiên cứu Ý 2024 cho Dachshund 11,5 — đã ghi trong từng mục).
- Rụng lông / vận động / hợp chung cư ở mọi mục đều là phân loại suy ra từ mô tả lông, năng lượng và mục đích
  giống trong bài Wikipedia / chuẩn FCI — đã ghi rõ câu này trong `ghi_chu_chua_kiem_chung` từng mục.
- Không nguồn nào bị chặn 403/429 trong đợt này. Có 1 lần Commons Search API trả `cirrussearch-too-busy-error`
  (tạm thời quá tải) — đã tránh bằng cách dùng imageinfo trực tiếp với tên file đã biết, không retry dồn dập.

## 4. Ảnh (8/8 giống có ảnh thật, đã kiểm tra bằng mắt 3 ảnh rủi ro nhất)
- Dachshund (CC BY-SA 4.0, Katemil94) — ảnh lông ngắn đỏ, đúng giống, đã xem trực tiếp ✓
- Cardigan Welsh Corgi (CC BY-SA 3.0, FatFairfax) — file gốc là PNG, đã convert sang JPEG thật (960×631).
- Austrian Pinscher (CC BY-SA 2.5, Przykuta), Dutch Smoushond (CC BY 2.0, ZeppWeb — ảnh nhỏ 308×231, ảnh gốc
  trên Commons chỉ có cỡ này), Hokkaido (CC BY-SA 3.0, しでん — ảnh nhỏ 311×300, ảnh gốc chỉ có cỡ này),
  Taiwan Dog (CC BY 3.0, Cho Hsun Lu), Phu Quoc Ridgeback (Public domain, Phó Nháy).
- Deutsch Stichelhaar (CC BY-SA 3.0, Alephalpha) — file "03030288 Deutsch Stichelhaa.jpg", mô tả Commons
  "The german pointing dog Deutsch Stichelhaar", đã xem trực tiếp: chó săn lông cứng, đúng giống ✓
- Không dùng ảnh minh họa/tranh vẽ; không có giống nào "chưa có ảnh" trong batch này.

## 5. Phụ: thay ảnh Akita trong D1.json (theo ghi chú REVIEW của coordinator)
- Cũ: collage "Akita Collage.png" 395×363 (CC BY 3.0, 4 tác giả) — file gốc đã backup tại
  `batches/dgap_work/akita-collage-old.png`.
- Thử lần 1: "Brindle Moku Akita Inu - Long Fur - In Snow.jpg" (đã xem trực tiếp) — KHÔNG dùng:
  chó lông dài xoắn (đột biến moku), mặt quay đi, nhìn không nhận ra Akita.
- Chốt: "Akita hiking in Shpella e Pëllumbasit.JPG" (CC BY-SA 4.0, Mr. Bunker, 960×720) — đã xem trực tiếp:
  Akita Inu đỏ-trắng điển hình, tai dựng, đuôi cuộn, nhận ra ngay. Đã cập nhật `anh.*` trong D1.json
  (D1.json vẫn hợp lệ, đủ 60 mục sau khi sửa).

## 6. File làm việc
- `batches/DGAP.json` (8 mục), `batches/DGAP_notes.md` (file này), `batches/build_dgap.py` (script build lại được),
  `batches/dgap_raw_*.json` (dữ liệu thô Wikipedia từng giống), `batches/dgap_work/` (9 PDF chuẩn FCI,
  8 bài Wikipedia đầy đủ, ảnh Akita cũ backup).
- Nguồn FCI đã lưu: `batches/dgap_work/fci_group1..10.html`, `fci_breeds_raw.json` (344 chuẩn),
  `fci_final_gaps.json` (7 gap cuối cùng).
