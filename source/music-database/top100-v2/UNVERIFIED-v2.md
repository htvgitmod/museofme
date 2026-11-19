# UNVERIFIED — Vòng 2 (enrich, 15/11/2026)

Tổng 380 bài. Các trường dưới đây VẪN THIẾU sau vòng 2 — để trống trung thực, không đoán.
Lý do chung, xem chi tiết từng batch trong `batches/batch-*/UNVERIFIED-batch-*.md` và `conflicts.md`:
- Deezer/iTunes không trả kết quả khớp tên + ca sĩ (đặc biệt nhạc xưa/bolero, rap underground, bài của Anh Tú Atus, bài song ca chỉ có 1 bản solo).
- Có ISRC nhưng Credits.fm trả `iswc: null` / không có writers (169 bài thiếu ISWC, phần lớn thuộc nhóm này).
- iTunes VN không trả trường ISRC — mọi ISRC đều từ Deezer; bài chỉ khớp iTunes thì không có ISRC để lookup Credits.fm.
- Năm: vòng 2 KHÔNG điền năm mới vào trường `year` (chỉ ghi `apple_release_date` làm bằng chứng đối chiếu, vì hay là ngày tái phát hành); 58 bài vẫn thiếu năm gốc.

## 1. Thiếu ISRC — 60/380
- song-039 — Ex's Hate Me (B Ray, AMEE) — confidence: medium
- song-062 — Hết Duyên (Tăng Duy Tân, NIT) — confidence: none
- song-095 — Heyyy (Soobin Hoàng Sơn) — confidence: medium
- song-098 — Anh sẽ về sớm thôi (Isaac) — confidence: none
- song-111 — Cảm giác lúc ấy sẽ ra sao (Lou Hoàng) — confidence: medium
- song-112 — Cuộc sống em ổn không (Anh Tú Atus) — confidence: none
- song-113 — Mình làm người yêu nhé em (Anh Tú Atus) — confidence: none
- song-114 — Mạnh mẽ lên cô gái (Anh Tú Atus) — confidence: none
- song-117 — Anh biết rồi (Rhyder) — confidence: medium
- song-119 — Hào quang (Rhyder) — confidence: medium
- song-122 — OK (Binz) — confidence: none
- song-123 — SoFar (Binz) — confidence: none
- song-124 — Người lạ ơi (Karik, Orange) — confidence: medium
- song-125 — Anh Không Đòi Quà (Karik, OnlyC) — confidence: medium
- song-127 — Có Lẽ Anh Chưa Từng (OnlyC, Karik) — confidence: none
- song-145 — Mẩy Thật Mẩy (BigDaddy) — confidence: none
- song-151 — Giàu Vì Bạn, Sang Vì Vợ (MCK) — confidence: medium
- song-152 — Tán Gái 101 (Low G) — confidence: none
- song-155 — Flexin Trên Circle K (Low G) — confidence: none
- song-163 — Tiểu thuyết tình yêu (Andree Right Hand, Lee7) — confidence: none
- song-164 — Ngọn nến trước gió (Andree Right Hand, LK, JustaTee, Emily) — confidence: none
- song-166 — Krazy (Binz, Andree Right Hand) — confidence: medium
- song-185 — Tám chữ có (Lê Cát Trọng Lý) — confidence: medium
- song-186 — Em đứng trên cánh đồng (Lê Cát Trọng Lý) — confidence: medium
- song-189 — World Without You (Phùng Khánh Linh) — confidence: none
- song-190 — Cô gái nhân ái (He Said She Said) (Phùng Khánh Linh) — confidence: medium
- song-198 — Không sao mà, em đây rồi (Suni Hạ Linh, Lou Hoàng) — confidence: medium
- song-208 — Vì Ai Vì Anh (Đông Nhi) — confidence: medium
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-224 — Còn Ta Với Nồng Nàn (Quang Dũng) — confidence: medium
- song-226 — Biển Tình (Quang Dũng) — confidence: none
- song-236 — Katy Katy (Lam Trường) — confidence: medium
- song-237 — Đôi Giày Vải (Lam Trường) — confidence: medium
- song-239 — Cảm Ơn Tình Yêu (Uyên Linh) — confidence: none
- song-254 — Buông (Lâm Bảo Ngọc) — confidence: medium
- song-255 — Rồi Em Sẽ Gặp Một Chàng Trai Khác (Lâm Bảo Ngọc) — confidence: medium
- song-282 — Lệ đá (Tuấn Ngọc) — confidence: none
- song-288 — Còn tuổi nào cho em (Ý Lan) — confidence: none
- song-289 — Em còn nhớ hay em đã quên (Ý Lan) — confidence: medium
- song-290 — Tình ca (Ý Lan) — confidence: medium
- song-292 — Vết thù trên lưng ngựa hoang (Elvis Phương) — confidence: medium
- song-303 — Xa rồi mùa đông (Phương Thanh) — confidence: medium
- song-304 — Chim trắng mồ côi (Cẩm Ly, Đan Trường) — confidence: medium
- song-305 — Bờ bến lạ (Cẩm Ly) — confidence: none
- song-306 — Người về cuối phố (Cẩm Ly) — confidence: none
- song-308 — Kiếp ve sầu (Đan Trường) — confidence: medium
- song-332 — Thành Phố Buồn (Đan Nguyên, Chế Linh) — confidence: none
- song-334 — Mưa Đêm Ngoại Ô (Trường Vũ) — confidence: none
- song-335 — Phút Cuối (Trường Vũ) — confidence: none
- song-339 — Còn thương rau đắng mọc sau hè (Hồ Văn Cường, Hương Lan) — confidence: none
- song-340 — Sa mưa giông (Hồ Văn Cường, Hương Lan) — confidence: none
- song-341 — Đêm Nghe Bài Vọng Cổ (Hương Lan) — confidence: medium
- song-343 — Đêm Buồn Tỉnh Lẻ (Thanh Tuyền) — confidence: medium
- song-352 — Bà Năm (Hồ Văn Cường) — confidence: medium
- song-353 — Về miền Tây (Hồ Văn Cường) — confidence: none
- song-359 — Đôi mắt Pleiku (Siu Black) — confidence: medium
- song-360 — Đôi chân trần (Siu Black) — confidence: none
- song-377 — Thời gian tôi (Phạm Anh Khoa) — confidence: medium
- song-378 — Tài sản của bố (ICD, Orange) — confidence: medium
- song-379 — Một chiếc váy (ICD) — confidence: none

## 2. Thiếu ISWC — 169/380
Gồm cả bài không có ISRC để lookup và bài có ISRC nhưng Credits.fm trả iswc null.
- song-002 — Lạc Trôi (Sơn Tùng M-TP) — confidence: high
- song-004 — Nơi Này Có Anh (Sơn Tùng M-TP) — confidence: high
- song-016 — Nấu Ăn Cho Em (Đen, PiaLinh) — confidence: high
- song-021 — Lạ Lùng (Vũ.) — confidence: high
- song-023 — Bước Qua Mùa Cô Đơn (Vũ.) — confidence: high
- song-024 — Mùa Mưa Ngâu Nằm Cạnh (Vũ.) — confidence: high
- song-025 — Gái Độc Thân (tlinh) — confidence: high
- song-026 — Nếu Lúc Đó (tlinh, 2pillz) — confidence: high
- song-027 — Thích Quá Rùi Nà (tlinh, Trung Trần) — confidence: high
- song-028 — vaicaunoicokhiennguoithaydoi (Grey D, tlinh) — confidence: high
- song-035 — Dù Cho Tận Thế (Erik) — confidence: high
- song-037 — Anh Nhà Ở Đâu Thế (AMEE, B Ray) — confidence: high
- song-038 — Sao Anh Chưa Về Nhà (AMEE, Ricky Star) — confidence: high
- song-039 — Ex's Hate Me (B Ray, AMEE) — confidence: medium
- song-041 — Waiting for You (MONO) — confidence: medium
- song-042 — Quên Anh Đi (MONO) — confidence: medium
- song-044 — Anh Không Thể (MONO) — confidence: medium
- song-055 — Exit Sign (HIEUTHUHAI, Marzuz) — confidence: high
- song-059 — Chỉ Còn Một Đêm (Last Dark) (Quang Hùng MasterD, F.HERO) — confidence: medium
- song-060 — Thủy Triều (Quang Hùng MasterD) — confidence: high
- song-061 — Ánh Mắt Biết Cười (Quang Hùng MasterD, Tăng Duy Tân) — confidence: medium
- song-062 — Hết Duyên (Tăng Duy Tân, NIT) — confidence: none
- song-064 — Dạ Vũ (Tăng Duy Tân) — confidence: high
- song-067 — Hồng Nhan (Jack) — confidence: medium
- song-068 — Bạc Phận (Jack) — confidence: high
- song-069 — Sóng Gió (Jack) — confidence: high
- song-074 — Nước Mắt Em Lau Bằng Tình Yêu Mới (Da LAB, Tóc Tiên) — confidence: high
- song-075 — 906090 (Tóc Tiên, Mew Amazing) — confidence: high
- song-079 — Đại Minh Tinh (Văn Mai Hương) — confidence: high
- song-084 — Y.Ê.U (Min) — confidence: high
- song-089 — Trái tim em cũng biết đau (Bảo Anh) — confidence: medium
- song-095 — Heyyy (Soobin Hoàng Sơn) — confidence: medium
- song-096 — Yêu không nghỉ phép (Isaac, Only C) — confidence: medium
- song-097 — Mr. Right (Khi anh yêu em) (Isaac) — confidence: medium
- song-098 — Anh sẽ về sớm thôi (Isaac) — confidence: none
- song-100 — Từ hôm nay (Feel Like Ooh) (Chi Pu) — confidence: medium
- song-103 — Cung đàn vỡ đôi (Chi Pu) — confidence: medium
- song-111 — Cảm giác lúc ấy sẽ ra sao (Lou Hoàng) — confidence: medium
- song-112 — Cuộc sống em ổn không (Anh Tú Atus) — confidence: none
- song-113 — Mình làm người yêu nhé em (Anh Tú Atus) — confidence: none
- song-114 — Mạnh mẽ lên cô gái (Anh Tú Atus) — confidence: none
- song-116 — Chịu cách mình nói thua (Rhyder, Ban, CoolKid) — confidence: high
- song-117 — Anh biết rồi (Rhyder) — confidence: medium
- song-118 — Dân chơi sao phải khóc (Andree Right Hand, Rhyder, Wokeup) — confidence: high
- song-119 — Hào quang (Rhyder) — confidence: medium
- song-120 — Bigcityboi (Binz) — confidence: high
- song-122 — OK (Binz) — confidence: none
- song-123 — SoFar (Binz) — confidence: none
- song-124 — Người lạ ơi (Karik, Orange) — confidence: medium
- song-125 — Anh Không Đòi Quà (Karik, OnlyC) — confidence: medium
- song-126 — Bạn Đời (Karik, GDucky) — confidence: high
- song-127 — Có Lẽ Anh Chưa Từng (OnlyC, Karik) — confidence: none
- song-128 — N-Sao? (Suboi) — confidence: high
- song-129 — Cho Không (Suboi) — confidence: high
- song-131 — Sickerrr (Suboi) — confidence: high
- song-133 — Chạy (Wowy) — confidence: high
- song-137 — Nến Và Hoa (Rhymastic) — confidence: high
- song-138 — Cứ Chill Thôi (Chillies, SUNI Hạ Linh, Rhymastic) — confidence: high
- song-142 — Bâng Khuâng (JustaTee) — confidence: high
- song-143 — Forever Alone (JustaTee) — confidence: high
- song-145 — Mẩy Thật Mẩy (BigDaddy) — confidence: none
- song-147 — Yêu Nắm (BigDaddy, Emily) — confidence: high
- song-148 — Chìm Sâu (MCK, Trung Trần) — confidence: high
- song-149 — Anh Đã Ổn Hơn (MCK) — confidence: high
- song-151 — Giàu Vì Bạn, Sang Vì Vợ (MCK) — confidence: medium
- song-152 — Tán Gái 101 (Low G) — confidence: none
- song-153 — Tán Gái 606 (Low G) — confidence: high
- song-154 — An Thần (Low G, Thắng) — confidence: high
- song-155 — Flexin Trên Circle K (Low G) — confidence: none
- song-157 — Lost (Obito) — confidence: high
- song-158 — Buồn Hay Vui (VSOUL, Boyzed, Obito, MCK, Ronboogz) — confidence: high
- song-159 — Hà Nội (Obito, Shiki, VSTRA) — confidence: high
- song-160 — Slow Down (Seachains) — confidence: medium
- song-161 — Anh 17 (Seachains) — confidence: medium
- song-163 — Tiểu thuyết tình yêu (Andree Right Hand, Lee7) — confidence: none
- song-164 — Ngọn nến trước gió (Andree Right Hand, LK, JustaTee, Emily) — confidence: none
- song-165 — Nhạc anh (Andree Right Hand, Wxrdie) — confidence: high
- song-166 — Krazy (Binz, Andree Right Hand) — confidence: medium
- song-168 — Còn Thở Còn Gỡ (Lil Wuyn) — confidence: medium
- song-169 — Mở Mắt (Lil Wuyn, Đen) — confidence: high
- song-170 — Như Vậy Nhé (Lil Wuyn, Wxrdie) — confidence: medium
- song-175 — Yếu đuối (Hoàng Dũng) — confidence: medium
- song-178 — Đôi lời tình ca (Hoàng Dũng) — confidence: medium
- song-179 — Một đêm say (X) (Thịnh Suy) — confidence: high
- song-180 — Thắc mắc? (Thịnh Suy) — confidence: high
- song-181 — Chuyện rằng (Thịnh Suy) — confidence: high
- song-182 — Tiny Love (Thịnh Suy) — confidence: high
- song-183 — Nghe em (Thịnh Suy) — confidence: high
- song-185 — Tám chữ có (Lê Cát Trọng Lý) — confidence: medium
- song-186 — Em đứng trên cánh đồng (Lê Cát Trọng Lý) — confidence: medium
- song-188 — Hôm Nay Tôi Buồn (Phùng Khánh Linh) — confidence: medium
- song-189 — World Without You (Phùng Khánh Linh) — confidence: none
- song-190 — Cô gái nhân ái (He Said She Said) (Phùng Khánh Linh) — confidence: medium
- song-191 — Sweet Summer (Phùng Khánh Linh) — confidence: medium
- song-194 — Em hát ai nghe (Orange) — confidence: medium
- song-196 — Không yêu đừng gây thương nhớ (LyLy, Karik) — confidence: medium
- song-198 — Không sao mà, em đây rồi (Suni Hạ Linh, Lou Hoàng) — confidence: medium
- song-202 — Cô Đơn Trên Sofa (Hồ Ngọc Hà) — confidence: medium
- song-203 — Chạm Khẽ Tim Anh Một Chút Thôi (Noo Phước Thịnh) — confidence: medium
- song-208 — Vì Ai Vì Anh (Đông Nhi) — confidence: medium
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-215 — Anh (Hồ Quỳnh Hương) — confidence: medium
- song-224 — Còn Ta Với Nồng Nàn (Quang Dũng) — confidence: medium
- song-226 — Biển Tình (Quang Dũng) — confidence: none
- song-231 — Bình Minh Sẽ Mang Em Đi (Đàm Vĩnh Hưng) — confidence: medium
- song-233 — Say Tình (Đàm Vĩnh Hưng) — confidence: medium
- song-234 — Tình Ơi Xin Ngủ Yên (Đàm Vĩnh Hưng) — confidence: medium
- song-235 — Tình Thôi Xót Xa (Lam Trường) — confidence: medium
- song-236 — Katy Katy (Lam Trường) — confidence: medium
- song-237 — Đôi Giày Vải (Lam Trường) — confidence: medium
- song-239 — Cảm Ơn Tình Yêu (Uyên Linh) — confidence: none
- song-240 — Bài Hát Của Em (Uyên Linh) — confidence: high
- song-246 — Dấu Mưa (Trung Quân) — confidence: medium
- song-248 — Chưa Bao Giờ (Trung Quân) — confidence: high
- song-254 — Buông (Lâm Bảo Ngọc) — confidence: medium
- song-255 — Rồi Em Sẽ Gặp Một Chàng Trai Khác (Lâm Bảo Ngọc) — confidence: medium
- song-257 — Nói Không Thành Lời (Lâm Bảo Ngọc) — confidence: high
- song-258 — Không Phải Em Đúng Không? (Dương Hoàng Yến) — confidence: high
- song-262 — Rồi Cũng Sẽ Qua (Myra Trần) — confidence: high
- song-265 — Thiên Hạ Hữu Tình Nhân (Juky San) — confidence: high
- song-266 — Người Đầu Tiên (Juky San, buitruonglinh) — confidence: high
- song-282 — Lệ đá (Tuấn Ngọc) — confidence: none
- song-288 — Còn tuổi nào cho em (Ý Lan) — confidence: none
- song-289 — Em còn nhớ hay em đã quên (Ý Lan) — confidence: medium
- song-290 — Tình ca (Ý Lan) — confidence: medium
- song-291 — Trăm nhớ ngàn thương (Ý Lan, Vũ Khanh) — confidence: medium
- song-292 — Vết thù trên lưng ngựa hoang (Elvis Phương) — confidence: medium
- song-296 — Tàn tro (Thanh Hà) — confidence: medium
- song-303 — Xa rồi mùa đông (Phương Thanh) — confidence: medium
- song-304 — Chim trắng mồ côi (Cẩm Ly, Đan Trường) — confidence: medium
- song-305 — Bờ bến lạ (Cẩm Ly) — confidence: none
- song-306 — Người về cuối phố (Cẩm Ly) — confidence: none
- song-308 — Kiếp ve sầu (Đan Trường) — confidence: medium
- song-309 — Mưa trên cuộc tình (Đan Trường) — confidence: medium
- song-311 — Tình khúc vàng (Đan Trường) — confidence: medium
- song-313 — Giấc Mơ Có Thật (Lệ Quyên) — confidence: medium
- song-315 — Ai Khổ Vì Ai (Lệ Quyên) — confidence: medium
- song-316 — Người Tình Mùa Đông (Như Quỳnh) — confidence: medium
- song-317 — Chuyện Hoa Sim (Như Quỳnh) — confidence: medium
- song-318 — Chuyện Tình Hoa Trắng (Như Quỳnh) — confidence: medium
- song-326 — Phải Lòng Con Gái Bến Tre (Phi Nhung, Quang Lê) — confidence: medium
- song-328 — Tình Đẹp Như Mơ (Mạnh Quỳnh) — confidence: medium
- song-330 — Gõ Cửa (Mạnh Quỳnh) — confidence: medium
- song-332 — Thành Phố Buồn (Đan Nguyên, Chế Linh) — confidence: none
- song-333 — Xin Làm Người Xa Lạ (Đan Nguyên, Chế Linh) — confidence: medium
- song-334 — Mưa Đêm Ngoại Ô (Trường Vũ) — confidence: none
- song-335 — Phút Cuối (Trường Vũ) — confidence: none
- song-339 — Còn thương rau đắng mọc sau hè (Hồ Văn Cường, Hương Lan) — confidence: none
- song-340 — Sa mưa giông (Hồ Văn Cường, Hương Lan) — confidence: none
- song-341 — Đêm Nghe Bài Vọng Cổ (Hương Lan) — confidence: medium
- song-343 — Đêm Buồn Tỉnh Lẻ (Thanh Tuyền) — confidence: medium
- song-346 — Đoạn Cuối Tình Yêu (Chế Linh, Thanh Tuyền) — confidence: medium
- song-347 — Mai Lỡ Mình Xa Nhau (Chế Linh) — confidence: medium
- song-349 — Vũ trụ có anh (Phương Mỹ Chi, Pháo) — confidence: high
- song-350 — Đẩy xe bò (Phương Mỹ Chi) — confidence: high
- song-351 — Bóng phù hoa (Phương Mỹ Chi) — confidence: high
- song-352 — Bà Năm (Hồ Văn Cường) — confidence: medium
- song-353 — Về miền Tây (Hồ Văn Cường) — confidence: none
- song-355 — Vầng trăng cô đơn (Ngọc Sơn) — confidence: medium
- song-356 — Lòng mẹ (Ngọc Sơn) — confidence: medium
- song-359 — Đôi mắt Pleiku (Siu Black) — confidence: medium
- song-360 — Đôi chân trần (Siu Black) — confidence: none
- song-373 — Nếu ta ngược lối (Châu Khải Phong) — confidence: high
- song-374 — Nỗi đau mình anh (Châu Khải Phong, Trịnh Đình Quang) — confidence: medium
- song-376 — Lý quạ kêu (Phạm Anh Khoa) — confidence: medium
- song-377 — Thời gian tôi (Phạm Anh Khoa) — confidence: medium
- song-378 — Tài sản của bố (ICD, Orange) — confidence: medium
- song-379 — Một chiếc váy (ICD) — confidence: none
- song-380 — Chân chạm đất (ICD) — confidence: medium

## 3. Thiếu nhạc sĩ (cả vòng 1 lẫn Credits.fm) — 17/380 (đã sửa 1: song-231, xem mục 7)
- song-035 — Dù Cho Tận Thế (Erik) — confidence: high
- song-100 — Từ hôm nay (Feel Like Ooh) (Chi Pu) — confidence: medium
- song-117 — Anh biết rồi (Rhyder) — confidence: medium
- song-119 — Hào quang (Rhyder) — confidence: medium
- song-160 — Slow Down (Seachains) — confidence: medium
- song-161 — Anh 17 (Seachains) — confidence: medium
- song-163 — Tiểu thuyết tình yêu (Andree Right Hand, Lee7) — confidence: none
- song-164 — Ngọn nến trước gió (Andree Right Hand, LK, JustaTee, Emily) — confidence: none
- song-166 — Krazy (Binz, Andree Right Hand) — confidence: medium
- song-194 — Em hát ai nghe (Orange) — confidence: medium
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-215 — Anh (Hồ Quỳnh Hương) — confidence: medium
- song-233 — Say Tình (Đàm Vĩnh Hưng) — confidence: medium
- song-234 — Tình Ơi Xin Ngủ Yên (Đàm Vĩnh Hưng) — confidence: medium
- song-296 — Tàn tro (Thanh Hà) — confidence: medium
- song-311 — Tình khúc vàng (Đan Trường) — confidence: medium
- song-313 — Giấc Mơ Có Thật (Lệ Quyên) — confidence: medium

## 4. Thiếu năm (trường year vòng 1) — 57/380 (đã sửa 1: song-231, xem mục 7)
Một số bài có `apple_release_date` gợi ý nhưng là ngày tái phát hành, chưa xác minh nên chưa điền.
- song-122 — OK (Binz) — confidence: none
- song-139 — Lặng (Rhymastic) — confidence: high
- song-145 — Mẩy Thật Mẩy (BigDaddy) — confidence: none
- song-152 — Tán Gái 101 (Low G) — confidence: none
- song-155 — Flexin Trên Circle K (Low G) — confidence: none
- song-169 — Mở Mắt (Lil Wuyn, Đen) — confidence: high
- song-183 — Nghe em (Thịnh Suy) — confidence: high
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-217 — Với Anh Em Vẫn Là Cô Bé (Hồ Quỳnh Hương) — confidence: high
- song-218 — Bức Thư Tình Thứ Hai (Hồ Quỳnh Hương) — confidence: high
- song-222 — Anh Nhớ Em (Tuấn Hưng) — confidence: high
- song-224 — Còn Ta Với Nồng Nàn (Quang Dũng) — confidence: medium
- song-225 — Anh Còn Nợ Em (Quang Dũng) — confidence: high
- song-226 — Biển Tình (Quang Dũng) — confidence: none
- song-227 — Trái Tim Bên Lề (Bằng Kiều) — confidence: high
- song-230 — Để Nhớ Một Thời Ta Đã Yêu (Bằng Kiều) — confidence: high
- song-233 — Say Tình (Đàm Vĩnh Hưng) — confidence: medium
- song-236 — Katy Katy (Lam Trường) — confidence: medium
- song-237 — Đôi Giày Vải (Lam Trường) — confidence: medium
- song-238 — Mưa Phi Trường (Lam Trường) — confidence: high
- song-249 — Chưa bao giờ (Thu Phương) — confidence: high
- song-275 — Giọt sương trên mí mắt (Hồng Nhung) — confidence: high
- song-279 — Dòng sông lơ đãng (Thu Phương) — confidence: high
- song-282 — Lệ đá (Tuấn Ngọc) — confidence: none
- song-283 — Mắt lệ cho người (Tuấn Ngọc) — confidence: high
- song-289 — Em còn nhớ hay em đã quên (Ý Lan) — confidence: medium
- song-290 — Tình ca (Ý Lan) — confidence: medium
- song-295 — Áo anh sứt chỉ đường tà (Elvis Phương) — confidence: high
- song-299 — Sợ bắt đầu sợ kết thúc (Thanh Hà) — confidence: high
- song-300 — Trống vắng (Phương Thanh) — confidence: high
- song-301 — Một thời đã xa (Phương Thanh) — confidence: high
- song-302 — Giã từ dĩ vãng (Phương Thanh) — confidence: high
- song-303 — Xa rồi mùa đông (Phương Thanh) — confidence: medium
- song-304 — Chim trắng mồ côi (Cẩm Ly, Đan Trường) — confidence: medium
- song-305 — Bờ bến lạ (Cẩm Ly) — confidence: none
- song-307 — Thương nhớ người dưng (Cẩm Ly) — confidence: high
- song-315 — Ai Khổ Vì Ai (Lệ Quyên) — confidence: medium
- song-318 — Chuyện Tình Hoa Trắng (Như Quỳnh) — confidence: medium
- song-319 — Đập Vỡ Cây Đàn (Quang Lê, Đan Nguyên) — confidence: high
- song-320 — Sầu Tím Thiệp Hồng (Quang Lê) — confidence: high
- song-322 — Sương Trắng Miền Quê Ngoại (Quang Lê) — confidence: high
- song-323 — Bông Điên Điển (Phi Nhung) — confidence: high
- song-324 — Chiều Lên Bản Thượng (Phi Nhung) — confidence: high
- song-325 — Áo Mới Cà Mau (Phi Nhung) — confidence: high
- song-326 — Phải Lòng Con Gái Bến Tre (Phi Nhung, Quang Lê) — confidence: medium
- song-327 — Vợ Tôi (Mạnh Quỳnh) — confidence: high
- song-328 — Tình Đẹp Như Mơ (Mạnh Quỳnh) — confidence: medium
- song-330 — Gõ Cửa (Mạnh Quỳnh) — confidence: medium
- song-335 — Phút Cuối (Trường Vũ) — confidence: none
- song-336 — Không Giờ Rồi (Trường Vũ, Như Quỳnh) — confidence: high
- song-338 — Em Đi Trên Cỏ Non (Hương Lan) — confidence: high
- song-344 — Chuyến Tàu Hoàng Hôn (Thanh Tuyền) — confidence: high
- song-345 — Đà Lạt Hoàng Hôn (Thanh Tuyền) — confidence: high
- song-347 — Mai Lỡ Mình Xa Nhau (Chế Linh) — confidence: medium
- song-358 — Ngọn lửa cao nguyên (Siu Black) — confidence: high
- song-359 — Đôi mắt Pleiku (Siu Black) — confidence: medium
- song-374 — Nỗi đau mình anh (Châu Khải Phong, Trịnh Đình Quang) — confidence: medium

## 5. Thiếu Apple Music URL — 37/380
- song-062 — Hết Duyên (Tăng Duy Tân, NIT) — confidence: none
- song-072 — Ngày Mai (Vũ Điệu Cồng Chiêng) (Tóc Tiên) — confidence: high
- song-084 — Y.Ê.U (Min) — confidence: high
- song-097 — Mr. Right (Khi anh yêu em) (Isaac) — confidence: medium
- song-098 — Anh sẽ về sớm thôi (Isaac) — confidence: none
- song-112 — Cuộc sống em ổn không (Anh Tú Atus) — confidence: none
- song-113 — Mình làm người yêu nhé em (Anh Tú Atus) — confidence: none
- song-114 — Mạnh mẽ lên cô gái (Anh Tú Atus) — confidence: none
- song-120 — Bigcityboi (Binz) — confidence: high
- song-122 — OK (Binz) — confidence: none
- song-131 — Sickerrr (Suboi) — confidence: high
- song-145 — Mẩy Thật Mẩy (BigDaddy) — confidence: none
- song-152 — Tán Gái 101 (Low G) — confidence: none
- song-155 — Flexin Trên Circle K (Low G) — confidence: none
- song-163 — Tiểu thuyết tình yêu (Andree Right Hand, Lee7) — confidence: none
- song-164 — Ngọn nến trước gió (Andree Right Hand, LK, JustaTee, Emily) — confidence: none
- song-189 — World Without You (Phùng Khánh Linh) — confidence: none
- song-193 — Khi em lớn (Orange, Hoàng Dũng) — confidence: high
- song-195 — 24h (LyLy, Magazine) — confidence: high
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-212 — Bay (Thu Minh) — confidence: high
- song-226 — Biển Tình (Quang Dũng) — confidence: none
- song-239 — Cảm Ơn Tình Yêu (Uyên Linh) — confidence: none
- song-282 — Lệ đá (Tuấn Ngọc) — confidence: none
- song-288 — Còn tuổi nào cho em (Ý Lan) — confidence: none
- song-305 — Bờ bến lạ (Cẩm Ly) — confidence: none
- song-306 — Người về cuối phố (Cẩm Ly) — confidence: none
- song-330 — Gõ Cửa (Mạnh Quỳnh) — confidence: medium
- song-332 — Thành Phố Buồn (Đan Nguyên, Chế Linh) — confidence: none
- song-334 — Mưa Đêm Ngoại Ô (Trường Vũ) — confidence: none
- song-335 — Phút Cuối (Trường Vũ) — confidence: none
- song-339 — Còn thương rau đắng mọc sau hè (Hồ Văn Cường, Hương Lan) — confidence: none
- song-340 — Sa mưa giông (Hồ Văn Cường, Hương Lan) — confidence: none
- song-353 — Về miền Tây (Hồ Văn Cường) — confidence: none
- song-360 — Đôi chân trần (Siu Black) — confidence: none
- song-379 — Một chiếc váy (ICD) — confidence: none
- song-380 — Chân chạm đất (ICD) — confidence: medium

## 6. Confidence none — không enrich được gì mới — 29/380
- song-062 — Hết Duyên (Tăng Duy Tân, NIT) — confidence: none
- song-098 — Anh sẽ về sớm thôi (Isaac) — confidence: none
- song-112 — Cuộc sống em ổn không (Anh Tú Atus) — confidence: none
- song-113 — Mình làm người yêu nhé em (Anh Tú Atus) — confidence: none
- song-114 — Mạnh mẽ lên cô gái (Anh Tú Atus) — confidence: none
- song-122 — OK (Binz) — confidence: none
- song-123 — SoFar (Binz) — confidence: none
- song-127 — Có Lẽ Anh Chưa Từng (OnlyC, Karik) — confidence: none
- song-145 — Mẩy Thật Mẩy (BigDaddy) — confidence: none
- song-152 — Tán Gái 101 (Low G) — confidence: none
- song-155 — Flexin Trên Circle K (Low G) — confidence: none
- song-163 — Tiểu thuyết tình yêu (Andree Right Hand, Lee7) — confidence: none
- song-164 — Ngọn nến trước gió (Andree Right Hand, LK, JustaTee, Emily) — confidence: none
- song-189 — World Without You (Phùng Khánh Linh) — confidence: none
- song-210 — Trốn Tìm (Đông Nhi) — confidence: none
- song-226 — Biển Tình (Quang Dũng) — confidence: none
- song-239 — Cảm Ơn Tình Yêu (Uyên Linh) — confidence: none
- song-282 — Lệ đá (Tuấn Ngọc) — confidence: none
- song-288 — Còn tuổi nào cho em (Ý Lan) — confidence: none
- song-305 — Bờ bến lạ (Cẩm Ly) — confidence: none
- song-306 — Người về cuối phố (Cẩm Ly) — confidence: none
- song-332 — Thành Phố Buồn (Đan Nguyên, Chế Linh) — confidence: none
- song-334 — Mưa Đêm Ngoại Ô (Trường Vũ) — confidence: none
- song-335 — Phút Cuối (Trường Vũ) — confidence: none
- song-339 — Còn thương rau đắng mọc sau hè (Hồ Văn Cường, Hương Lan) — confidence: none
- song-340 — Sa mưa giông (Hồ Văn Cường, Hương Lan) — confidence: none
- song-353 — Về miền Tây (Hồ Văn Cường) — confidence: none
- song-360 — Đôi chân trần (Siu Black) — confidence: none
- song-379 — Một chiếc váy (ICD) — confidence: none

## 7. Mâu thuẫn — ĐÃ CHỐT HẾT ngày 16/11/2026 (kiểm chứng lại bằng API + Wikipedia)

Tất cả 7 mâu thuẫn dưới đây đã được rà lại và sửa vào `songs-enriched.json` /
`songs-enriched.csv` (và `singers.json`/`singers.csv` cho LyLy). Không còn mục nào
chờ John chốt. Chi tiết từng bài nằm trong trường `conflicts[]` của bài đó.

- song-001 Chạy Ngay Đi + song-003 Muộn Rồi Mà Sao Còn — CHỐT: giữ nhạc sĩ Sơn Tùng M-TP.
  Credits.fm/MLC ghi nhất quán DUY DUC NGUYEN (IPI 01068595419) cho cả 2 bài, nhưng không
  có nguồn kiểm chứng nào nối tên đó với Sơn Tùng M-TP — tên thật của anh là Nguyễn Thanh
  Tùng (Wikipedia vi/en + chính anh xác nhận, kiểm chứng 16/11). Nhạc sĩ giữ theo mô tả MV
  chính thức (COMPOSER: SON TUNG M-TP) + Wikipedia; tên đăng ký Credits.fm vẫn lưu trong
  `credits_songwriters`, không lấy làm nhạc sĩ chính.
- song-041 Waiting for You (MONO) — CHỐT: ISRC sửa USY6C0710009 → VNA092201159.
  ISRC vòng 1 là của ban nhạc MONO Nhật Bản. ISRC đúng đã kiểm chứng qua Deezer track
  1863033907 (16/11: đúng tên bài, ca sĩ MONO, album 22). ISWC vẫn để trống: Credits.fm
  trả ISWC T-101877319-6 cho ISRC này nhưng chính response của Credits.fm ghi song_title
  "SINCE I'VE BEEN WAITING FOR YOU" — tác phẩm của MONO Nhật, không phải bài của MONO Việt —
  nên ISWC và nhạc sĩ DUY NGUYEN HOANG từ record đó đều không lấy.
- song-246 Dấu Mưa (Trung Quân) — CHỐT: giữ ISRC VNR011016684, ISWC vẫn trống.
  ISRC đã kiểm chứng qua Deezer track 76107310 (16/11: "Dau Mua (2013 digital remaster)",
  ca sĩ Trung Quan Idol, đúng ISRC). Credits.fm vẫn map ISRC này sang "CON DO DONG SONG"
  của Ngọc Sơn, iswc null — lỗi map của Credits.fm, không lấy ISWC/nhạc sĩ từ đó.
  Nhạc sĩ Phạm Toàn Thắng đã có từ vòng 1 (Gaana + AllMusic + VTV).
- song-084 Y.Ê.U (Min) — CHỐT từ vòng 2: ISWC của bài khác đã bị loại, giữ trống.
  Credits.fm trả ISWC của "Trên tình bạn dưới tình yêu" cho ISRC này — không lấy.
  Nhạc sĩ Khắc Hưng đã khớp (HUNG KHAC, IPI 00690117845).
- song-231 Bình Minh Sẽ Mang Em Đi (Đàm Vĩnh Hưng) — CHỐT: ISRC giữ, năm + nhạc sĩ đã điền.
  ISRC VNR011002463 đã kiểm chứng qua Deezer track 3756186412 (16/11: đúng tên bài, ca sĩ
  Đàm Vĩnh Hưng). Credits.fm vẫn map sang "Một Lần Nữa Được Yêu" của Phùng Ngọc Huy và
  trả ISWC sai định dạng (T9108099350) — lỗi map của Credits.fm, không lấy. Năm điền 2001
  (album Vol. 2, Wikipedia en/fr/de/ja/th đồng thuận; ngày iTunes 2015-11-02 chỉ là tái
  phát hành). Nhạc sĩ: đây là bản lời Việt của Rednex "Hold Me for a While" — nhạc Teijo /
  Ranis, lời Việt Đàm Vĩnh Hưng (Wikipedia vi, kiểm chứng 16/11). Nhờ vậy thiếu nhạc sĩ
  18 → 17, thiếu năm 58 → 57.
- song-065 Bên Trên Tầng Lầu (Tăng Duy Tân) — CHỐT: năm sửa 2021 → 2022.
  Wikipedia vi (kiểm chứng 16/11): phát hành 10/06/2022 — khớp Deezer album release_date
  2022-06-10 và iTunes 2022-06-10. Số 2021 là năm sáng tác (giai đoạn giãn cách COVID),
  không phải năm phát hành.
- LyLy — CHỐT: tên thật sửa Nguyễn Hoàng Lan → Nguyễn Hoàng Ly.
  Wikipedia vi/en vẫn ghi "Nguyễn Hoàng Lan" nhưng kèm chú thích [a]: "Most current sources,
  including her personal Facebook profile, refer to her original name as 'Nguyễn Hoàng Ly'"
  (kiểm chứng 16/11) — và có bài báo về việc cô tiết lộ tên thật, "đến cả Wiki đều nhầm lẫn".
  Credits.fm cũng ghi NGUYEN HOANG LY ở song-197. Đã sửa trong `top100/singers.json`,
  `top100/singers.csv` và bản copy `top100-v2/singers.json`, kèm ghi chú tranh chấp.
- Lưu ý chung: nhiều mâu thuẫn nhạc sĩ khác chỉ là tên đảo thứ tự/không dấu của Credits.fm
  (vd HUNG KHAC = Khắc Hưng) — đã đối chiếu theo tập token, không tính là mâu thuẫn thật.
