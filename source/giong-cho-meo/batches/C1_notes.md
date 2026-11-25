# Batch C1 — Mèo A–LaPerm: notes

- Phạm vi: 53 trang trong `data/cat_list.json` từ "Abyssinian cat" đến "LaPerm".
- Hoàn thành: **51 mục** trong `C1.json`. Ảnh: **45/51** có ảnh thật đã tải về.

## Giống LOẠI KHỎI batch (2)
- **Fitoaty** — không phải giống mèo nhà: bài Wikipedia mô tả là mèo hoang (feral cat) ở rừng mưa đông bắc Madagascar, ít được nghiên cứu. Loại theo quy tắc "chỉ giống mèo nhà thật".
- **Caucasian black cat** — không phải giống mèo nhà: bài Wikipedia mô tả là quần thể mèo hoang / mèo rừng Caucasus hoặc con lai giữa hai loài. Loại cùng lý do.

## Giống KHÔNG CÓ ẢNH (6) — đã ghi `anh: null` + "Chưa có ảnh" trong ghi_chu, KHÔNG gắn ảnh sai
- **Bohemian Rex** — trang Wikipedia không có pageimage; tìm trên Commons không ra ảnh nào xác thực là giống này.
- **Cashmere** — trang là redirect tới mục "Long-haired variant, the Cashmere Bengal" trong bài Bengal; ảnh Bengal tìm được trên Commons không xác nhận được là bản lông dài nên không dùng.
- **Exotic Longhair** — trang là redirect tới mục "Longhair Exotics" trong bài Exotic Shorthair; tìm Commons không ra ảnh xác thực.
- **Isle of Man Longhair** — redirect tới bài Manx; ảnh Manx tìm được không xác nhận được là bản lông dài có đuôi.
- **Isle of Man Shorthair** — redirect tới bài Manx; tương tự, không xác nhận được là bản lông ngắn có đuôi.
- **Korn Ja** — redirect tới mục lịch sử bài Siamese; ảnh Siamese tìm được không phải Korn Ja nên không dùng.

## Ảnh — phương pháp & giấy phép
- Ảnh lấy từ pageimage của chính trang Wikipedia của giống đó, tải về `photos/meo-<slug>.jpg` (JPEG, ~800px, PIL convert, tổng ~5,6 MB cho 45 ảnh C1).
- Chỉ nhận license tự do: CC BY / CC BY-SA / CC0 / Public domain / GFDL.
- **Birman**: ảnh `Birmanstrofe.jpg` (tác giả Kristin Kokkersvold), license "Copyrighted free use" — đây là license cho phép dùng tự do mọi mục đích trên Commons nên đã chấp nhận tải (script gốc chặn nhầm, đã tải lại tay và kiểm tra ảnh bằng mắt: đúng mèo Birman mắt xanh, lông point).
- Đã kiểm tra bằng mắt 3 ảnh mẫu: Birman, Abyssinian, Cornish Rex — đều đúng giống.

## Chưa kiểm chứng (quan trọng — đọc trước khi dùng số liệu)
- **Tất cả 51 mục đều là `chua-kiem-chung-phan`**: infobox mèo trên Wikipedia hầu như KHÔNG có trường cân nặng/chiều cao/tuổi thọ.
  - Cân nặng có nguồn: 10/51 (Abyssinian, American Curl, Asian, Bohemian Rex, Bombay, Burmilla, Chantilly-Tiffany, Chausie, Cymric, Cyprus).
  - Chiều cao có nguồn: 1/51 (Abyssinian 20–25 cm).
  - Tuổi thọ có nguồn: 7/51 (Bengal 8,5 năm; Birman 14,4 năm; Bombay 15–20 năm; British Shorthair 9,6 năm; Burmese 14,4 năm; Japanese Bobtail 9–15 năm; Kurilian Bobtail 15–20 năm). Các tuổi thọ dạng "nghiên cứu thú y Anh" là trung bình từ nghiên cứu hồ sơ thú y Anh trích trong bài Wikipedia, đã ghi rõ trong trường tuổi thọ.
  - Còn lại ghi "chưa kiểm chứng" + liệt kê trong `ghi_chu_chua_kiem_chung` từng mục.
- Các trường phân loại (kich_co, rung_long, van_dong, hop_chung_cu, tinh_cach) được suy từ mô tả lông/tính cách/hoạt động trong chính bài Wikipedia của giống đó (vd lông dày hai lớp → rung_long Nhieu; "constant motion" → van_dong Cao); trường hợp suy luận đã ghi chú trong `ghi_chu_chua_kiem_chung`.
- **Korn Ja** gần như không có dữ liệu kiểm chứng được (chỉ biết là tên giống mèo Thái cổ, redirect về bài Siamese): mọi số liệu "chưa kiểm chứng", kích cỡ Vua chỉ là tạm xếp.
- **Chantilly-Tiffany**: giống đã tuyệt chủng từ 2015 — đã ghi trong mô tả.

## Nguồn bị chặn
- Không có: Wikipedia API + Wikimedia Commons API đều truy cập được trong suốt quá trình cào (25/11/2026), không gặp 403/429.

## Tên tiếng Việt
- Chỉ ghi `ten_vi` cho 17 giống có tên thông dụng thật ở Việt Nam (vd Mèo Anh lông ngắn, Mèo Mỹ lông ngắn, Mèo Miến Điện, Mèo Nhật đuôi ngắn, Mèo Bengal, Mèo Birman, Mèo Chartreux); 34 giống còn lại để `null`, không dịch bịa.

## QA đã chạy
- `python3 -m json.tool batches/C1.json` hợp lệ; đúng 18 key/mục theo schema; không trùng id; mọi `anh.file` tồn tại trên đĩa và mở được bằng PIL (verify); mọi `nguon[0]` là link Wikipedia EN của giống.
- File: `batches/C1.json` (68 KB), dữ liệu thô: `batches/C1_raw.json`, script cào: `batches/c1_fetch.py`, script build: `batches/c1_build.py`.
