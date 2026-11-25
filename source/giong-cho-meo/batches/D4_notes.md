# D4 — Ghi chú batch (Istrian Shorthaired Hound → Pembroke Welsh Corgi)

Ngày làm: 25/11/2026. Nguồn danh sách: Category:FCI breeds (Wikipedia EN), file `D4_list.json`.

## Kết quả
- **59/60 mục hoàn thành** (59 giống chó thật, 0 trùng id, 0 trùng tên_en).
- **59/59 ảnh thật đã tải** về `photos/cho-*.jpg`, tổng 12.365.974 byte, tất cả đều là JPEG hợp lệ (kiểm tra magic bytes). 3 ảnh kiểm tra trực quan: Manchester Terrier, Komondor, Istrian Shorthaired Hound — đều đúng giống.
- **44 mục `da-kiem-chung` / 15 mục `chua-kiem-chung-phan`.**
- `ten_vi`: chỉ 11 giống có tên tiếng Việt thông dụng thật (Labrador, Corgi, Bắc Kinh, Chó Nhật, Maltese, Lhasa Apso, Jindo, Spitz Nhật, Pinscher mini, Schnauzer mini, King Charles); còn lại null — không dịch bịa.

## Mục loại khỏi danh sách (1)
- `List of Hungarian dog breeds` — trang danh sách, không phải một giống chó. Không có mục JSON cho trang này.

## Nguồn số liệu
- Chính: infobox + nội dung bài Wikipedia EN của từng giống (cân nặng, chiều cao lấy từ infobox; tuổi thọ lấy từ câu "life expectancy/lifespan" trong bài).
- Bổ sung: **AKC (akc.org)** cho 44/59 giống — chỉ điền các trường Wikipedia không có, và chỉ ghi vào `nguon` khi trang AKC tồn tại. Nhờ AKC, số mục đầy đủ tăng từ 10 lên 44.
- Mọi mục đều có link chuẩn FCI trong `nguon` (59/59, trích từ `fcistd` trong infobox).
- Không có nguồn nào bị chặn (không gặp 403/429 ở Wikipedia API lẫn AKC).

## Nhóm FCI — 3 giống không có trong infobox, đã kiểm chứng riêng
- Lapponian Herder → **nhóm 5** (FCI Nomenclature, Section 3 Nordic Watchdogs and Herders; chuẩn số 284).
- Magyar Agár → **nhóm 10** (Sighthounds; chuẩn số 240).
- Montenegrin Mountain Hound → **nhóm 6** (Scent hounds; chuẩn số 279).
- 56 giống còn lại lấy nhóm FCI trực tiếp từ link chuẩn `fcistd` trong infobox.

## Ảnh — trường hợp đặc biệt (1)
- **Manchester Terrier**: ảnh chính trên trang Wikipedia (`Mancherster_Terrier.jpg`) mang giấy phép **GPL** — script chỉ chấp nhận PD/CC nên không tải. Đã thay bằng ảnh khác trên Wikimedia Commons: `Anchor, the Manchester Terrier0.jpg`, **CC BY 2.0, tác giả Roger Ahlbrand** — đã kiểm tra trực quan, đúng giống (đen-vàng, lông mượt, tai gập).

## Chưa kiểm chứng (15 mục — ghi rõ trong từng `ghi_chu_chua_kiem_chung`)
Nguyên nhân chung: các giống FCI-only này **không có trang AKC** (404 đã kiểm chứng) và bài Wikipedia EN không ghi số liệu.
- Istrian Shorthaired Hound: thiếu chiều cao, tuổi thọ
- Jämthund: thiếu cân nặng, tuổi thọ
- Kangal Shepherd Dog: thiếu tuổi thọ
- Karst Shepherd: thiếu cân nặng, chiều cao, tuổi thọ
- Kazakh Tazy: thiếu tuổi thọ
- Kintamani: thiếu tuổi thọ
- Kishu: thiếu tuổi thọ
- Komondor: thiếu chiều cao
- Korean Jindo: thiếu tuổi thọ
- Landseer: thiếu tuổi thọ
- Macedonian Shepherd Dog: thiếu tuổi thọ
- Magyar Agár: thiếu cân nặng
- Maremmano-Abruzzese Sheepdog: thiếu tuổi thọ
- Montenegrin Mountain Hound: thiếu cân nặng, chiều cao, tuổi thọ
- Old Danish Pointer: thiếu cân nặng, chiều cao, tuổi thọ

## Lưu ý về các trường suy luận
- `tinh_cach` / `rung_long` / `van_dong` / `hop_chung_cu`: **suy luận từ mô tả bộ lông, năng lượng và mục đích sử dụng trong bài Wikipedia EN**, không phải số liệu trực tiếp từ FCI/AKC — đã ghi rõ trong `ghi_chu_chua_kiem_chung` của mọi mục.
- `kich_co`: tính từ điểm giữa khoảng cân nặng theo ngưỡng Nho <10 / Vua 10–25 / Lon 25–45 / Khổng lồ >45 kg; khi cân nặng chưa kiểm chứng thì suy ra từ chiều cao/loại giống và cũng ghi rõ trong ghi chú.
- `tuoi_tho` dạng "khoảng 12 năm" = bài nguồn chỉ ghi một con số duy nhất (life expectancy of 12 years), không phải khoảng.

## File liên quan
- `batches/D4.json` — đầu ra chính (59 mục, đúng schema).
- `batches/D4_raw.json` — dữ liệu thô Wikipedia (summary + infobox wikitext + metadata ảnh).
- `batches/scrape_d4.py`, `batches/build_d4.py` — script cào và build (có thể chạy lại).
- `/tmp/d4_fields2.json`, `/tmp/d4_full.json`, `/tmp/d4_akc.json` — dữ liệu trung gian (infobox đã parse, full-text, AKC).

## QA cuối
- `python3 -m json.tool batches/D4.json` — hợp lệ.
- Schema: đủ 18 key/mục, enum đúng (kich_co/rung_long/van_dong/hop_chung_cu), tinh_cach 2–4 từ, fci_group 1–10, id duy nhất.
- Ảnh: 59/59 file tồn tại, đúng JPEG, license + tác giả + commons_url đầy đủ.
- Phân bố: kích cỡ Nho 20 / Vừa 22 / Lớn 10 / Khổng lồ 7; hợp chung cư: Có 14 / Hạn chế 25 / Không 20.
