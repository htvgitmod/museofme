# Batch D2 — Notes (Braque Saint-Germain → English Setter, 60 giống)

## Kết quả
- **60/60 mục** trong `batches/D2.json`, đủ schema, JSON hợp lệ, id và tên_en duy nhất.
- **60/60 ảnh thật** trong `photos/cho-*.jpg` (11,8 MB), đều là JPEG hợp lệ (kiểm bằng PIL),
  đều lấy từ ảnh chính của trang Wikipedia của chính giống đó (pageimage) hoặc — riêng
  Colombian Fino Hound — file Commons cùng tên giống (`File:Colombian Fino Hound.jpg`,
  CC BY-SA 4.0, tác giả D1090, mô tả "Colombian Fino Hound"). 3 ảnh đã kiểm tra trực quan
  (Bulldog, Colombian Fino Hound, Drever) đều đúng giống.
- **33 mục `da-kiem-chung`, 27 mục `chua-kiem-chung-phan`** (xem dưới).
- Không giống nào bị bỏ; không trùng tên; không nguồn nào bị chặn 403/429 trong đợt này
  (Wikipedia API, AKC, FCI đều trả 200).

## Nguồn số liệu (theo thứ tự ưu tiên)
1. **Tiêu chuẩn FCI (PDF)** — chiều cao/cân nặng/tính cách/nhóm, tải qua `pdftotext`.
   Nhóm FCI suy ra từ số tiêu chuẩn (vd 115g07 → nhóm 7) và kiểm chứng lại bằng PDF.
2. **AKC** — PageMap (cao/nặng/tuổi thọ) + thang điểm trait 1-5 (shedding, energy, bark...).
   Áp dụng cho 35/60 giống (AKC chỉ công nhận một phần giống FCI).
3. **Wikipedia EN** — infobox + toàn văn bài (tuổi thọ từ các nghiên cứu UK/Ý 2024,
   mục Temperament). Infobox của Wikipedia rất thưa (life_span 0/60, temperament 0/60)
   nên không dùng làm nguồn chính cho 2 trường này.

## Trường "chưa kiểm chứng" — chi tiết
- **Tuổi thọ thiếu ở 27 mục** (ghi rõ từng mục trong `ghi_chu_chua_kiem_chung`):
  đa số là giống FCI hiếm (3 Braque, Briquet Griffon Vendéen, Burgos Pointer, Bucovina,
  Campeiro Bulldog, Carpathian, Castro Laboreiro, Central Asian, Chien Français ×3,
  Colombian Fino Hound, Continental Bulldog, Croatian Sheepdog, Czechoslovakian Wolfdog,
  Cão de Gado Transmontano, Drever, Dunker, East Siberian Laika, Drentse Patrijshond…).
  AKC/FCI/Wikipedia đều không công bố tuổi thọ cho các giống này — KHÔNG bịa số.
- **Cân nặng thiếu ở 15 mục** (Braque ×3, Briquet Griffon Vendéen, Burgos Pointer,
  Carpathian, Castro Laboreiro, Catalan Sheepdog, Chien Français ×3, Croatian Sheepdog,
  Drever, East Siberian Laika): tiêu chuẩn FCI chỉ ghi chiều cao.
- **Chiều cao thiếu ở 1 mục** (Castro Laboreiro Dog): tiêu chuẩn FCI số 170 và bài
  Wikipedia đều không ghi số đo; kích cỡ "Lớn" là ước theo mô tả giống chó chăn gia súc
  lớn, đã ghi rõ trong `ghi_chu`.
- **Nhóm FCI sửa tay sau kiểm chứng** (parser ban đầu bỏ sót do URL dạng -es/-fr hoặc
  fcistd không phải PDF): Ca de Bestiar → 1 (321g01), Canaan Dog → 5 (273g05),
  Chien Français Blanc et Noir → 6 (220g06), Cimarrón Uruguayo → 2 (tiêu chuẩn 353,
  bài Wikipedia), Dunker → 6 (tiêu chuẩn 203), Drever → 6 (tiêu chuẩn 130).

## Quy tắc suy luận cho 3 trường phân loại (ghi rõ trong từng mục)
- Rụng lông/vận động: nếu có điểm AKC thì theo thang AKC (shedding 1-2=Ít, 3=Trung bình,
  4-5=Nhiều; energy 1-2=Thấp, 3=Trung bình, 4-5=Cao). Nếu không có AKC thì suy luận từ
  loại lông + mục đích giống trong tiêu chuẩn FCI, ghi rõ là suy luận trong `ghi_chu`.
- Hợp chung cư (quy tắc suy luận thống nhất):
  Nho: Có (Hạn chế nếu vận động Cao + sủa nhiều); Vừa: Có nếu vận động Thấp, còn lại Hạn chế;
  Lớn: Hạn chế (Không nếu có ghi chú nguồn rõ ràng, vd Burgos Pointer 'không hợp đô thị',
  Canadian Eskimo Dog 'không nên xem là thú cưng trong nhà', English Foxhound chó săn bầy sủa nhiều);
  Khổng lồ: Hạn chế nếu vận động Thấp, còn lại Không.
- Kích cỡ: theo cân nặng khi có số (<10 Nho, 10-25 Vừa, 25-45 Lớn, >45 Khổng lồ);
  khi thiếu cân nặng thì ước theo chiều cao và ghi rõ trong `ghi_chu`.

## Các trường hợp đặc biệt
- **Bulldog**: ảnh chính license GFDL (không phải CC) — vẫn là license tự do của Commons,
  đã tải về (Whitebulldog.jpg, tác giả Av3553). Script kiểm tra license ban đầu bỏ sót GFDL,
  đã sửa tay.
- **Dobermann**: ảnh chính license "Copyrighted free use" — license tự do của Commons,
  đã tải về (Dobermann_handling.jpg, tác giả Miroslav Cacik).
- **Dogo Argentino**: tuổi thọ lấy "10-12 năm" theo bài Wikipedia; AKC ghi 9-15 năm
  (ghi trong `ghi_chu`).
- **Caucasian Shepherd Dog**: AKC ghi 10-12 năm nhưng một nghiên cứu 2024 ghi median
  chỉ 5 năm — đã ghi cảnh báo tranh cãi trong `ghi_chu`.
- **Cavalier / Dobermann / English Setter / Bull Terrier / English Cocker / Cairn Terrier**:
  tuổi thọ AKC khác với nghiên cứu 2024 trích trong bài Wikipedia — lấy số AKC, ghi số
  nghiên cứu trong `ghi_chu`.
- **Continental Toy Spaniel**: AKC và FCI coi Papillon/Phalène là một giống nên dùng
  số liệu AKC trang Papillon; tên Việt lấy "Chó Papillon" (tên thông dụng).
- **Dunker**: cân nặng 39 lb theo infobox Wikipedia (khoảng 18 kg); tiêu chuẩn FCI
  không ghi cân nặng.
- **Tên Việt null (19 mục)**: các giống hiếm, ít được nhắc tới ở Việt Nam (3 Braque,
  Briquet Griffon Vendéen, Burgos Pointer, Ca de Bestiar, Ca de Bou, Campeiro Bulldog,
  Chien Français ×3, Colombian Fino Hound, Castro Laboreiro, Cão de Gado Transmontano,
  Cimarrón Uruguayo, Danish–Swedish Farmdog, Drentse Patrijshond, Drever, Dunker) —
  không dịch bịa, để null theo quy tắc.

## File làm việc trong batch
- `D2_list.json` (danh sách gốc), `D2_raw.json` (dữ liệu thô Wikipedia + ảnh),
  `D2_parsed.json` (infobox đã parse), `D2_fulltext.json` (toàn văn bài),
  `D2_round2.json` (AKC + FCI PDF), `D2_supp.json` (7 PDF FCI bổ sung),
  `D2_merged.json`/`D2_merged.txt` (bảng duyệt), `scrape_d2.py`, `parse2.py`,
  `fulltext_d2.py`, `akc_fci_d2.py`, `merge_review.py`, `build_d2.py`, `D2.json` (final).
- Thư mục `photos/` hiện có 355 file `cho-*.jpg` vì các batch khác đang cào song song;
  60 file của D2 đã xác minh tồn tại và đọc được (xem QA trong báo cáo).
