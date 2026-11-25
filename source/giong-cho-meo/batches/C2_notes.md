# Batch C2 — Mèo Lykoi → York Chocolate (25/11/2026)

## Kết quả
- Danh sách gốc: 47 trang trong data/cat_list.json từ "Lykoi" trở đi.
- Loại bỏ 2 trang (không phải giống riêng): "Pittsburgh refrigerator cat", "Malagasy forest cat" (mèo hoang).
- Loại bỏ thêm 2 redirect trùng trong quá trình làm:
  - "Thai Lilac" → redirect tới mục trong bài Korat (chỉ là biến thể màu của Korat; Korat thuộc batch C1) — không lập mục riêng.
  - "Traditional Siamese cat" → redirect tới "Thai cat" (đã có mục Thai trong batch này) — không lập mục riêng.
- **Hoàn thành: 43 mục** trong batches/C2.json (đúng schema, JSON hợp lệ, không trùng id/tên).
- **Ảnh: 42/43 giống có ảnh thật** (tổng ~5,6 MB, đều là ảnh chính từ trang Wikipedia của chính giống đó, giấy phép tự do PD/CC, đã ghi license + tác giả + commons_url từng ảnh). 3 ảnh gốc là PNG đã convert sang JPG (nền trắng): Minuet, Russian White/Black/Tabby, Turkish Van.
- **Chưa có ảnh (1): York Chocolate** — infobox Wikipedia không có ảnh; trên Commons chỉ có một ảnh mèo con ghi danh mục "York Chocolate mix cats" (mèo lai) nên KHÔNG dùng (sai ảnh còn tệ hơn không có ảnh). Ghi rõ trong mục.

## Nguồn
- Tất cả lấy từ Wikipedia EN qua API (fetch_breed.py + fulltext extracts), không bị chặn 403/429 lần nào.
- Link nguồn mỗi mục: Wikipedia EN + tối đa 2 link chuẩn giống (CFA/TICA/FIFe/WCF/GCCF) trích từ infobox khi có.
- Ảnh Oriental Longhair: giấy phép Free Art License (FAL) — giấy phép tự do, đã tải thủ công vì script chung chỉ chấp nhận CC/PD.

## Chưa kiểm chứng (ghi rõ trong từng mục, trang_thai="chua-kiem-chung-phan")
- **Chiều cao: 100% các mục ghi "chưa kiểm chứng"** — bài Wikipedia và chuẩn giống không công bố chiều cao cho mèo (chỉ có cân nặng).
- **Cân nặng có nguồn: 17/43** (trích từ toàn văn Wikipedia: Maine Coon, Manx, Mekong Bobtail, Munchkin, Nebelung, Neva Masquerade, Ocicat, Oriental Shorthair, Pixie-bob, Ragdoll, Russian Blue, Savannah, Selkirk Rex, Serengeti, Siberian, Singapura, Turkish Van). 26 mục còn lại ghi "chưa kiểm chứng".
- **Tuổi thọ có nguồn: 5/43** (Maine Coon 12-13 năm, Persian 11-14 năm, Ragdoll 10-11 năm, Siamese 11-12 năm, Sokoke 15 năm — đều từ nghiên cứu/dữ liệu bảo hiểm trích trong bài Wikipedia). 38 mục còn lại ghi "chưa kiểm chứng".
- **Các trường rung_long/van_dong/hop_chung_cu/tinh_cach** là phân loại suy ra từ mô tả lông, năng lượng và tính cách trong bài Wikipedia, KHÔNG phải số liệu trực tiếp của nguồn — đã ghi rõ câu này trong ghi_chu của mọi mục.
- Kích cỡ "Lớn" của Ragamuffin suy ra từ quan hệ họ hàng với Ragdoll (cân nặng chưa kiểm chứng) — đã ghi rõ.

## Trường hợp đặc biệt (đã ghi trong mo_ta_ngan/ghi_chu từng mục)
- Ojos Azules: giống ĐÃ TUYỆT CHỦNG chính thức (gene mắt xanh gây tác dụng phụ gây chết).
- Mexican Hairless Cat: giống gây tranh cãi ("purported breed"), ghi nhận 1902, không còn được công nhận rộng rãi.
- Minskin: nhân giống bị cấm ở một số nước (EU cấm trên thực tế). Munchkin/Minuet: gây tranh cãi, bị cấm ở một số nước.
- York Chocolate: số lượng cực ít hoặc đã tuyệt chủng tính đến 2026; chỉ WCF công nhận.
- Oriental Bicolour: chỉ GCCF (Anh) công nhận là giống riêng; các hiệp hội khác coi là biến thể màu lông của Oriental.
- Suphalak: một số nguồn coi là đồng nghĩa/biến thể màu của mèo Thái cổ, chưa được công nhận rộng rãi là giống riêng.
- Traditional Persian: không phải giống đăng ký riêng, là kiểu truyền thống của mèo Ba Tư.
- Savannah: lai serval, cần không gian + vận động nhiều; một số nơi hạn chế nuôi.

## QA cuối (25/11/2026)
- `python3 -m json.tool batches/C2.json` → hợp lệ.
- Đủ 19 key/mục, enum kich_co/rung_long/van_dong/hop_chung_cu đúng; tinh_cach 2-4 từ/mục (đã sửa Ojos Azules từ 1 lên 2).
- 42/42 file ảnh tồn tại trên đĩa, mở được bằng PIL, không file lỗi.
- Kiểm tra bằng mắt 4 ảnh: Lykoi, Peterbald, Oriental Bicolour, Turkish Van — đều đúng giống (Lykoi lông roan thưa, Peterbald không lông, Oriental Bicolour đen-trắng kiểu Oriental, Turkish Van trắng với mảng màu đầu + đuôi).
