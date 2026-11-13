# Cơ sở dữ liệu nhạc Việt — Top 100 ca sĩ Việt Nam

> **Ngày chốt danh sách:** 13/11/2026 (Batch 1)
> **Phạm vi batch này:** Chỉ chốt danh sách 100 ca sĩ + tiêu chí chọn. KHÔNG crawl bài hát, KHÔNG làm giao diện.

## 1. Tiêu chí chọn

1. **Ca sĩ Việt, ưu tiên đang hoạt động / có ảnh hưởng lớn.** Người nghe Việt Nam vẫn nghe nhiều trên streaming, YouTube, radio, sân khấu — không chọn ca sĩ chỉ nổi tiếng về mặt lịch sử mà không còn bản ghi được nghe nhiều.
2. **Có catalogue đủ để crawl sau này:** mỗi ca sĩ sau này cần 3–5 bài nổi tiếng nhất (mục tiêu chung của dự án: 100 ca sĩ → 300–500 bài).
3. **Cân bằng nhiều chiều:**
   - Nam / nữ.
   - Nhiều thế hệ: từ thế hệ hải ngoại / trữ tình (Khánh Ly, Tuấn Ngọc, Chế Linh…) qua thế hệ 2000s (Mỹ Tâm, Hồ Ngọc Hà, Noo Phước Thịnh…) đến Gen Z (MONO, tlinh, HIEUTHUHAI, Grey D…).
   - Nhiều thể loại: Pop, Ballad, R&B, Rap/Hip-hop, Indie, Bolero/trữ tình, Rock, EDM.
4. **Chỉ ca sĩ solo.** Không đưa nhóm nhạc / ban nhạc / duo vào danh sách này (xem mục 4 — trường hợp phân vân).
5. **Không bịa số liệu:** file này KHÔNG ghi lượt nghe, lượt xem hay thứ hạng cụ thể nếu không kiểm chứng được từ nguồn công khai. Lý do chọn mỗi người chỉ 1 dòng ngắn, dựa trên sự nghiệp / album / bài hit / giải thưởng đã biết chung, không ghi số không có nguồn.

## 2. Phương pháp chọn

Kết hợp nhiều tín hiệu, **không dựa vào một bảng xếp hạng duy nhất**:

- Spotify / Apple Music (monthly listeners, độ dày discography, độ phủ playlist).
- Wikipedia / Wikidata — các danh sách ca sĩ Việt Nam.
- Chart Zing MP3 / Billboard Vietnam (khi có dữ liệu công khai).
- Lượt xem MV official trên YouTube (mức độ phổ biến chung, không lấy con số cụ thể vào file này).
- Độ nhận biết chung trong công chúng Việt Nam qua nhiều năm (đặc biệt với thế hệ trước streaming).

> **⚠️ Cảnh báo quan trọng — "Top" ở đây là ước lượng tổng hợp từ các nguồn trên, KHÔNG phải bảng xếp hạng chính thức duy nhất.**
> Thứ tự 1–100 trong danh sách dưới đây là cách sắp xếp theo nhóm (demo trước, rồi theo dòng nhạc / thế hệ) để tiện theo dõi và crawl, **không phải thứ hạng 1 là hay nhất / nghe nhiều nhất**. Không dùng thứ tự này để khẳng định "ca sĩ A hơn ca sĩ B".

## 3. Quy ước trong danh sách

- Mỗi dòng: `số thứ tự. Nghệ danh [demo nếu có] — Tên thật (nếu chắc chắn) | Thể loại chính | Lý do chọn (1 dòng)`.
- Tên thật chỉ ghi khi chắc chắn; nếu không chắc chắn thì ghi `—` (không đoán).
- Nghệ danh viết theo cách viết chuẩn, phổ biến nhất (ví dụ: `Vũ.` có dấu chấm, `tlinh` viết thường).
- **10 ca sĩ demo bắt buộc** được đánh dấu `[demo]` — đó là 10 ca sĩ của bản demo graph đã có: Sơn Tùng M-TP, Mỹ Tâm, Hà Anh Tuấn, Đen, Hoàng Thùy Linh, Vũ., tlinh, Bích Phương, Erik, AMEE.

## 4. Các trường hợp phân vân — đã xử lý như sau

1. **Nhóm nhạc / ban nhạc:** LOẠI khỏi danh sách này. Chỉ lấy ca sĩ solo để mỗi node trong graph là 1 người, tránh trùng người (ví dụ một ca sĩ vừa solo vừa trong nhóm sẽ bị tính 2 lần). Các nhóm nổi tiếng như Chillies, Ngọt, Da LAB, Bức Tường, 365… nếu cần sẽ làm danh sách riêng ở batch sau, không trộn vào Top 100 solo này.
2. **Ca sĩ hải ngoại (Paris By Night / trung tâm hải ngoại):** GIỮ, nếu repertoire tiếng Việt của họ vẫn được nghe nhiều tại Việt Nam trên YouTube/streaming (ví dụ: Như Quỳnh, Quang Lê, Đan Nguyên, Trường Vũ, Tuấn Ngọc, Khánh Ly, Ý Lan, Elvis Phương, Thanh Hà). Tiêu chí là "được nghe nhiều", không phải "đang sống ở Việt Nam".
3. **Ca sĩ đã mất:** CHỈ GIỮ nếu catalogue của họ vẫn được nghe/stream nhiều tới nay. Trong danh sách này chỉ có **Phi Nhung** thuộc trường hợp đó (mất 2021, các bản bolero/trữ tình vẫn được nghe rất nhiều). Không đưa ca sĩ chỉ nổi tiếng lịch sử mà không còn bản ghi streaming phổ biến (ví dụ: không đưa Trịnh Công Sơn — ông chủ yếu là nhạc sĩ, không phải ca sĩ thu âm chính; không đưa các danh ca tiền chiến không còn bản ghi phổ biến).
4. **Một người, hai nghệ danh / tên dễ nhầm:** KHÔNG liệt kê cùng 1 người dưới 2 nghệ danh. Ví dụ đã tránh: chỉ lấy 1 "Trung Quân" (Trung Quân Idol) và không lấy thêm một mục "Nguyễn Trần Trung Quân" riêng; chỉ lấy 1 "Anh Tú" là Anh Tú Atus (Bùi Anh Tú), không lấy thêm Anh Tú khác. Các batch sau khi crawl cần kiểm tra lại bằng tên thật / ISRC / Spotify artist ID để không tách đôi một người.
5. **Ca sĩ gây tranh cãi / vướng scandal nhưng vẫn được nghe nhiều:** GIỮ theo tiêu chí "được nghe nhiều", không đánh giá đạo đức trong file này. Việc có đưa bài hát cụ thể nào của họ vào database hay không sẽ do batch crawl + John quyết định sau, dựa trên nguồn chính thức.
6. **Rapper vs ca sĩ:** GIỮ rapper có sản phẩm âm nhạc phát hành chính thức, được nghe rộng rãi (Binz, Karik, Đen, HIEUTHUHAI, MCK…), vì họ là một phần lớn của nhạc Việt đương đại. Không đưa battle rapper / underground chỉ nổi trong cộng đồng hẹp mà không có sản phẩm streaming phổ biến.
7. **Ca sĩ kiêm nhạc sĩ / producer:** GIỮ nếu họ nổi tiếng trước hết với vai trò ca sĩ trình diễn (ví dụ: Phan Mạnh Quỳnh, Vũ Cát Tường, Tăng Duy Tân). Không đưa producer thuần túy không hát chính (ví dụ: không đưa K-ICM).
8. **Chi Pu:** GIỮ — dù xuất phát là diễn viên/hot girl, cô đã phát hành nhiều sản phẩm âm nhạc chính thức, có hit và lượng nghe lớn, nên đủ tiêu chí "ca sĩ đang hoạt động".

## 5. Danh sách Top 100

### Nhóm demo (1–10) — 10 ca sĩ bắt buộc từ bản demo

1. Sơn Tùng M-TP [demo] — Nguyễn Thanh Tùng | Pop | Ca sĩ pop nam có sức ảnh hưởng lớn nhất Gen Z, chuỗi hit "Chạy Ngay Đi", "Lạc Trôi", "Muộn Rồi Mà Sao Còn".
2. Mỹ Tâm [demo] — Phan Thị Mỹ Tâm | Pop / Ballad | "Họa mi tóc nâu", diva pop hàng đầu nhiều thập kỷ, album "Tâm 9" và liveshow Tri Âm.
3. Hà Anh Tuấn [demo] — Hà Anh Tuấn | Pop / Ballad | Giọng ballad nam hàng đầu, album "Truyện Ngắn", chuỗi liveshow "See Sing Share".
4. Đen [demo] — Nguyễn Đức Cường | Rap / Hip-hop | Rapper có ảnh hưởng nhất nhạc Việt đương đại, "Đưa Nhau Đi Trốn", "Hai Triệu Năm", "Mang Tiền Về Cho Mẹ".
5. Hoàng Thùy Linh [demo] — Hoàng Thùy Linh | Pop / EDM / Dân gian đương đại | "Để Mị Nói Cho Mà Nghe", "See Tình", album "Hoàng" và "LINK" pha dân gian với EDM.
6. Vũ. [demo] — Trần Anh Vũ | Indie / Pop | "Lạ Lùng", "Bước Qua Nhau", "Mùa Mưa Ngâu Nằm Cạnh Nhau", gương mặt indie-pop được nghe nhiều nhất.
7. tlinh [demo] — Nguyễn Thảo Linh | Pop / R&B / Hip-hop | Gen Z đa năng, "Gái Độc Thân", album "ái", nổi lên từ Rap Việt.
8. Bích Phương [demo] — Bùi Thị Bích Phương | Pop / Ballad | "Bùa Yêu", "Đi Đu Đưa Đi", "Chị Ngả Em Nâng", giọng pop nữ ổn định nhiều năm.
9. Erik [demo] — Lê Trung Thành | Pop / Ballad | "Sau Tất Cả", "Chạm Đáy Nỗi Đau", "Dù Cho Tận Thế", giọng ballad nam Gen Z nổi bật.
10. AMEE [demo] — Trần Huyền My | Pop | "Anh Nhà Ở Đâu Thế", "Sao Anh Chưa Về Nhà", album "dreAMEE", pop nữ Gen Z.

### Pop / Ballad Gen Z & đương đại (11–30)

11. MONO — Nguyễn Việt Hoàng | Pop / R&B | "Waiting For You" gây sốt, album "22", em trai Sơn Tùng M-TP, pop Gen Z.
12. Đức Phúc — Nguyễn Đức Phúc | Pop / Ballad | Quán quân The Voice 2015, "Ánh Nắng Của Anh", "Hơn Cả Yêu".
13. Hòa Minzy — Nguyễn Thị Hòa | Pop / Ballad | "Rời Bỏ", "Không Thể Cùng Nhau Suốt Kiếp", "Thị Mầu", giọng pop nữ mạnh.
14. HIEUTHUHAI — Trần Minh Hiếu | Rap / Pop | "Ngủ Một Mình", "Không Thể Say", rapper Gen Z lấn sân pop, nổi lên từ Rap Việt và "2 Ngày 1 Đêm".
15. Grey D — Đoàn Thế Lân | Pop / R&B | "Đưa Em Về Nhà", "Dự Báo Thời Tiết Hôm Nay Mưa", cựu thành viên MONSTAR, solo pop/R&B.
16. Quang Hùng MasterD — Lê Quang Hùng | Pop / Ballad | "Thuỷ Triều", "Dễ Đến Dễ Đi", hit lớn sau thời gian hoạt động tại Thái Lan.
17. Tăng Duy Tân — Tăng Duy Tân | Pop / Ballad | "Bên Trên Tầng Lầu", "Cắt Đôi Nỗi Sầu", nhạc sĩ kiêm ca sĩ hit-maker Gen Z.
18. Jack — Trịnh Trần Phương Tuấn | Pop | "Hồng Nhan", "Sóng Gió", "Đom Đóm", hiện tượng pop Gen Z với lượng fan lớn.
19. Tóc Tiên — Nguyễn Khoa Tóc Tiên | Pop / EDM | "Ngày Mai", "Có Ai Thương Em Như Anh", "906090", pop nữ cá tính, hoạt động lâu năm.
20. Văn Mai Hương — Văn Mai Hương | Pop / Ballad | Á quân Vietnam Idol 2010, "Nếu Như Anh Đến", "Đại Minh Tinh", giọng pop nữ kỹ thuật.
21. Trúc Nhân — Nguyễn Trúc Nhân | Pop | "Thật Bất Ngờ", "Sáng Mắt Chưa", "Có Không Giữ Mất Đừng Tìm", pop nam cá tính.
22. Min — Nguyễn Minh Hằng | Pop / EDM | "Yêu", "Có Em Chờ", "Ghen", pop nữ EDM thế hệ 2010s.
23. Bảo Anh — Nguyễn Hoài Bảo Anh | Pop / Ballad | "Trái Tim Em Cũng Biết Đau", "Như Lời Đồn", "Anh Muốn Em Sống Sao".
24. Soobin Hoàng Sơn — Nguyễn Huỳnh Sơn | Pop / R&B | "Phía Sau Một Cô Gái", "Đi Để Trở Về", "Heyyy", R&B/pop nam hàng đầu.
25. Isaac — Phạm Lưu Tuấn Tài | Pop | Cựu trưởng nhóm 365, solo "Anh Sẽ Về Sớm Thôi", "Yêu Thương Không Là Trò Đùa".
26. Chi Pu — Nguyễn Thùy Chi | Pop | "Từ Hôm Nay", "Đoá Hoa Hồng", ca sĩ pop có sản phẩm chính thức và lượng nghe lớn (xem mục 4.8).
27. Quân A.P — Phạm Quốc Anh | Pop / Ballad | "Ai Là Người Thương Em", "Bông Hoa Đẹp Nhất", ballad nam Gen Z.
28. Lou Hoàng — Hoàng Kim Long | Pop / R&B | "Mình Là Gì Của Nhau", "Ngày Hôm Qua", "Cảm Giác Lúc Ấy Sẽ Ra Sao".
29. Anh Tú Atus — Bùi Anh Tú | Pop / Ballad | "Cuộc Sống Em Ổn Không", "Duyên Do Trời Định", giọng ballad nam được chú ý từ The Voice.
30. Rhyder — Nguyễn Quang Anh | Pop / R&B | Quán quân The Voice Kids 2013, "Chịu Cách Mình Nói Thua", "Anh Biết Rồi", solo Gen Z.

### Rap / Hip-hop (31–43)

31. Binz — Lê Nguyễn Trung Đan | Rap / Hip-hop | "Bigcityboi", "Cho Mình Em", "OK", rapper mainstream hàng đầu, huấn luyện viên Rap Việt.
32. Karik — Phạm Hoàng Khoa | Rap / Hip-hop | "Người Lạ Ơi", "Anh Không Đòi Quà", "Bạn Đời", rapper kỳ cựu lấn sân mainstream.
33. Suboi — Hàng Lâm Trang Anh | Rap / Hip-hop | "N-Sao?", "Cho Không", nữ rapper tiên phong của hip-hop Việt, huấn luyện viên Rap Việt.
34. Wowy — Nguyễn Minh Huy | Rap / Hip-hop | "Khu Tao Sống", "Chạy", rapper underground lên mainstream, huấn luyện viên Rap Việt.
35. Rhymastic — Vũ Đức Thiện | Rap / Hip-hop | "Yêu 5", "Cần Một Ai Đó", "Nến Và Hoa", rapper/producer kỳ cựu.
36. JustaTee — Nguyễn Thanh Tuấn | Rap / R&B | "Đã Lỡ Yêu Em Nhiều", "Thằng Điên", "Bâng Khuâng", R&B/rap melody hàng đầu.
37. BigDaddy — Trần Tất Vũ | Rap / Hip-hop | "Mượn Rượu Tỏ Tình", "Mẩy Thật Mẩy", rapper mainstream từ SpaceSpeakers.
38. MCK — Nghiêm Vũ Hoàng Long | Rap / Hip-hop | "Chìm Sâu", "Anh Đã Ổn Hơn", "Thờ Er", rapper Gen Z nổi lên từ Rap Việt.
39. Low G — Nguyễn Hoàng Long | Rap / Hip-hop | "Tán Gái 101", "An Thần", "Flexin Trên Circle K", rapper Gen Z Hà Nội.
40. Obito — Lý Quốc Phong | Rap / Hip-hop | "Simple Love", "Your Smile", "Sài Gòn Đâu Có Lạnh Đâu", rapper Gen Z melodic.
41. Seachains — Huỳnh Long Hải | Rap / Hip-hop | "Cảm Ơn Và Xin Lỗi", "Trở Về", rapper Gen Z nổi lên từ Rap Việt.
42. Andree Right Hand — Bùi Thế Anh | Rap / Hip-hop | "Nhạt", "Em Gái Mưa" (hợp tác), "Chơi Như Tụi Mỹ", rapper kỳ cựu, huấn luyện viên Rap Việt.
43. Lil Wuyn — — | Rap / Hip-hop | "Lãng Du", "Không Sao Cả", rapper Gen Z indie-rap được nghe nhiều.

### Indie / Alternative / Nhạc sĩ kiêm ca sĩ (44–50)

44. Vũ Cát Tường — Vũ Cát Tường | Pop / R&B / Indie | "Yêu Xa", "Mơ", "Có Người", nhạc sĩ kiêm ca sĩ, phong cách unisex riêng biệt.
45. Hoàng Dũng — Nguyễn Hoàng Dũng | Pop / Ballad | "Nàng Thơ", "Yếu Đuối", "Chờ Anh Nhé", quán quân The Voice 2015, ballad nam.
46. Thịnh Suy — — | Indie | "Một Đêm Say", "Nghe Em", "Tiny Love", indie Gen Z được nghe nhiều trên streaming.
47. Lê Cát Trọng Lý — Lê Cát Trọng Lý | Indie / Folk | "Chênh Vênh", "Tám Chữ Có", "Khói Thuốc Cà Phê", folk-indie kỳ cựu.
48. Phùng Khánh Linh — Phùng Khánh Linh | Indie / Pop | "Hôm Nay Tôi Buồn", "Quý Cô Say Xỉn", album "Yesteryear", indie-pop nữ.
49. Orange — Khương Hoàn Mỹ | Pop / R&B | "Người Lạ Ơi" (hợp tác), "Chân Ái", "Khi Em Lớn", giọng R&B nữ Gen Z.
50. LyLy — Nguyễn Hoàng Ly | Pop / Ballad | "24H", "Vì Em Là Con Gái", "Không Sao Mà Em Đây Rồi", nhạc sĩ kiêm ca sĩ Gen Z.

### Pop / Ballad thế hệ 2000s–2010s (51–60)

51. Hồ Ngọc Hà — Hồ Ngọc Hà | Pop | "Xin Hãy Thứ Tha", "Cả Một Trời Thương Nhớ", "Cô Đơn Trên Sofa", diva giải trí hàng đầu.
52. Noo Phước Thịnh — Nguyễn Phước Thịnh | Pop / Ballad | "Chạm Khẽ Tim Anh Một Chút Thôi", "Thương Em Là Điều Anh Không Thể Ngờ", pop nam hàng đầu 2010s.
53. Đông Nhi — Mai Hồng Ngọc | Pop / EDM | "Bad Boy", "Xin Lỗi Anh Quá Phiền", "Trốn Tìm", pop nữ hàng đầu 2010s.
54. Thu Minh — Vũ Thu Minh | Pop / Dance | "Đường Cong", "Bay", "Yêu Mình Anh", diva dance-pop.
55. Hồ Quỳnh Hương — Hồ Quỳnh Hương | Pop / Ballad | "Anh", "Hoang Mang", "Với Anh Em Vẫn Là Cô Bé", giọng ballad nữ kỹ thuật cao.
56. Tuấn Hưng — Nguyễn Tuấn Hưng | Pop / Ballad | "Tìm Lại Bầu Trời", "Nắm Lấy Tay Anh", "Dĩ Vãng Cuộc Tình", pop-ballad nam 2000s.
57. Quang Dũng — Thái Văn Dũng | Pop / Ballad / Trữ tình | "Vì Đó Là Em", "Biển Tình", "Còn Ta Với Nồng Nàn", giọng trữ tình nam.
58. Bằng Kiều — Nguyễn Bằng Kiều | Pop / Ballad | "Trái Tim Bên Lề", "Nơi Tình Yêu Bắt Đầu", "Anh Sẽ Nhớ Mãi", giọng nam hải ngoại và trong nước.
59. Đàm Vĩnh Hưng — Huỳnh Minh Hưng | Pop / Bolero | "Bình Minh Sẽ Mang Em Đi", "Xin Lỗi Tình Yêu", "Say Tình", "ông hoàng nhạc Việt".
60. Lam Trường — Tiêu Lam Trường | Pop / Ballad | "Tình Thôi Xót Xa", "Katy Katy", "Mưa Phi Trường", pop nam thế hệ đầu Làn Sóng Xanh.

### Giọng ca vocal / Ballad đương đại (61–70)

61. Uyên Linh — Trần Nguyễn Uyên Linh | Pop / Ballad | Quán quân Vietnam Idol 2010, "Cảm Ơn Tình Yêu", "Bài Hát Của Em", "Giữa Đại Lộ Đông Tây".
62. Quốc Thiên — Trần Quốc Thiên | Pop / Ballad | Quán quân Vietnam Idol 2008, "Hơn 1000 Năm Sau", "Chia Cách Bình Yên".
63. Trung Quân — Nguyễn Trần Trung Quân | Pop / Ballad | "Trót Yêu", "Dấu Mưa", "Chưa Bao Giờ", giọng ballad nam cao vút (chỉ lấy 1 mục Trung Quân — xem mục 4.4).
64. Bùi Anh Tuấn — Bùi Anh Tuấn | Pop / Ballad | "Nơi Tình Yêu Bắt Đầu", "Hẹn Một Mai", "Thuận Theo Ý Trời", giọng ballad nam The Voice.
65. Lâm Bảo Ngọc — — | Pop / Ballad | "Đổi Thay", "Còn Lại Một Mình", giọng pop nữ The Voice, hoạt động solo ổn định.
66. Dương Hoàng Yến — Dương Hoàng Yến | Pop / Ballad | "Cầu Vồng Khuyết", "Xe Anh Đến Đâu Em Theo Đến Đó", "Không Phải Em Đúng Không".
67. Myra Trần — — | Pop / Ballad | "Mong Một Hạnh Phúc", "Tình Yêu Đến Sau", giọng nữ X-Factor, hoạt động song ngữ Việt–Mỹ.
68. Juky San — — | Pop | "Phải Chăng Em Đã Yêu", "Yêu Là Cưới", pop nữ Gen Z nổi lên từ mạng xã hội.
69. Han Sara — — | Pop | "Đếm Cừu", "Tớ Thích Cậu", "Vì Yêu Là Nhớ", pop nữ Gen Z gốc Hàn–Việt.
70. Hiền Hồ — Võ Thị Hiền Hồ | Pop / Ballad | "Rồi Người Thương Cũng Hoá Người Dưng", "Gặp Nhưng Không Ở Lại", giọng pop nữ Gen Z.

### Trữ tình / Hải ngoại / Thế hệ trước (71–80)

71. Hồng Nhung — Lê Hồng Nhung | Pop / Trữ tình | "Nhớ Về Hà Nội", "Giọt Sương Trên Mí Mắt", "Papa", diva Hà Nội.
72. Thu Phương — Nguyễn Thị Thu Phương | Pop / Trữ tình | "Chưa Bao Giờ", "Đêm Nằm Mơ Phố", "Có Phải Em Mùa Thu Hà Nội", giọng nữ hải ngoại và trong nước.
73. Tuấn Ngọc — Lữ Anh Tuấn | Trữ tình | "Riêng Một Góc Trời", "Chiều Một Mình Qua Phố", "Nỗi Nhớ Dịu Dàng", danh ca hải ngoại.
74. Khánh Ly — Nguyễn Thị Lệ Mai | Trữ tình / Nhạc Trịnh | Giọng ca gắn với nhạc Trịnh Công Sơn, "Diễm Xưa", "Hạ Trắng", "Biển Nhớ".
75. Ý Lan — Lê Thị Ý Lan | Trữ tình | "Còn Tuổi Nào Cho Em", "Em Còn Nhớ Hay Em Đã Quên", danh ca hải ngoại.
76. Elvis Phương — Phạm Ngọc Phương | Trữ tình / Rock | "Vết Thù Trên Lưng Ngựa Hoang", "Đàn Bà", "Yêu Em Dài Lâu", danh ca hải ngoại đa thể loại.
77. Thanh Hà — Trương Minh Hà | Trữ tình / Pop | "Tàn Tro", "Sợ Yêu", "Mong Manh Tình Về", giọng nữ hải ngoại được nghe nhiều tại Việt Nam.
78. Phương Thanh — Bùi Thị Phương Thanh | Pop / Rock | "Trống Vắng", "Một Thời Đã Xa", "Giã Từ Dĩ Vãng", giọng khàn đặc trưng 1990s–2000s.
79. Cẩm Ly — Trần Thị Cẩm Ly | Pop / Bolero | "Chim Trắng Mồ Côi", "Bờ Bến Lạ", "Người Về Cuối Phố", giọng nữ dân ca/bolero đương đại.
80. Đan Trường — Phạm Đan Trường | Pop | "Kiếp Ve Sầu", "Tình Khúc Vàng", "Mưa Trên Cuộc Tình", pop nam Làn Sóng Xanh.

### Bolero / Trữ tình / Dân ca (81–90)

81. Lệ Quyên — Vũ Lệ Quyên | Bolero / Trữ tình | "Nữ hoàng phòng trà", "Duyên Phận", "Giấc Mơ Có Thật", bolero đương đại hàng đầu.
82. Như Quỳnh — Lê Lâm Quỳnh Như | Bolero / Trữ tình | "Người Tình Mùa Đông", "Duyên Phận" (bản hải ngoại), "Chuyện Hoa Sim", danh ca hải ngoại.
83. Quang Lê — Lê Hữu Nghị | Bolero / Trữ tình | "Đập Vỡ Cây Đàn", "Sầu Tím Thiệp Hồng", "Về Đâu Mái Tóc Người Thương", bolero hải ngoại.
84. Phi Nhung — Phạm Phi Nhung | Bolero / Dân ca | "Bông Điên Điển", "Chiều Lên Bản Thượng", "Áo Mới Cà Mau" — ca sĩ đã mất (2021), catalogue vẫn được nghe nhiều (xem mục 4.3).
85. Mạnh Quỳnh — Nguyễn Thanh Dũng | Bolero / Trữ tình | "Vợ Tôi", "Tình Đẹp Như Mơ", "Căn Nhà Màu Tím", bolero hải ngoại, song ca nhiều với Phi Nhung.
86. Đan Nguyên — Nguyễn Đặng Đan | Bolero / Trữ tình | "Thói Đời", "Thành Phố Buồn", "Xin Làm Người Xa Lạ", bolero hải ngoại.
87. Trường Vũ — — | Bolero / Trữ tình | "Mưa Đêm Ngoại Ô", "Phút Cuối", "Không Giờ Rồi", bolero hải ngoại.
88. Hương Lan — Trần Ngọc Ánh | Bolero / Dân ca | "Em Đi Trên Cỏ Non", "Còn Thương Rau Đắng Mọc Sau Hè", "Sa Mưa Giông", danh ca dân ca/bolero.
89. Thanh Tuyền — — | Bolero / Trữ tình | "Nỗi Buồn Hoa Phượng", "Đêm Buồn Tỉnh Lẻ", "Chuyến Tàu Hoàng Hôn", danh ca bolero hải ngoại.
90. Chế Linh — Lưu Văn Linh | Bolero / Trữ tình | "Thói Đời", "Đoạn Cuối Tình Yêu", "Thành Phố Buồn", danh ca bolero hải ngoại.

### Bolero trẻ / Rock / Bổ sung đa dạng (91–100)

91. Phương Mỹ Chi — Phương Mỹ Chi | Bolero / Dân ca đương đại | "Quê Em Mùa Nước Lũ", "Vũ Trụ Cò Bay", á quân The Voice Kids, bolero Gen Z.
92. Hồ Văn Cường — Hồ Văn Cường | Bolero / Dân ca | "Bà Năm", "Cõng Mẹ Đi Chơi", quán quân Vietnam Idol Kids, bolero trẻ.
93. Ngọc Sơn — Phạm Ngọc Sơn | Bolero / Pop | "Tình Cha", "Vầng Trăng Cô Đơn", "Lòng Mẹ", "ông hoàng nhạc sến" thế hệ 1990s.
94. Siu Black — Nguyễn Thị Siu Black | Rock / Pop | "Ly Cà Phê Ban Mê", "Ngọn Lửa Cao Nguyên", "Đôi Chân Trần", "hoạ mi núi rừng", rock/pop Tây Nguyên.
95. Tùng Dương — Nguyễn Tùng Dương | Pop / Rock / Đương đại | "Chiếc Khăn Piêu", "Con Cò", "Mưa Bay Tháp Cổ", "Ôi Quê Tôi", giọng nam đương đại kỹ thuật cao.
96. Phan Mạnh Quỳnh — Phan Mạnh Quỳnh | Pop / Ballad / Indie | "Vợ Người Ta", "Khi Người Mình Yêu Khóc", "Sau Lời Từ Khước", nhạc sĩ kiêm ca sĩ.
97. Đạt G — Nguyễn Tấn Đạt | Pop / R&B | "Buồn Của Anh", "Khó Vẽ Nụ Cười", "Thêm Bao Nhiêu Lâu", pop/R&B Gen Z.
98. Châu Khải Phong — — | Pop / Ballad | "Ngắm Hoa Lệ Rơi", "Bên Nhau Thật Khó", "Đơn Phương", pop nam miền Tây được nghe nhiều trên YouTube.
99. Phạm Anh Khoa — Phạm Anh Khoa | Rock | "Ngựa Ô Thương Nhớ", "Lý Quạu", rock nam, quán quân Sao Mai Điểm Hẹn 2006.
100. ICD — — | Rap / Hip-hop | "Tài Sản Của Cha", "Sau Này", quán quân King of Rap 2020, rapper Gen Z.

---

## 6. Kiểm chứng

- [ ] Đếm bằng lệnh: đúng 100 mục đánh số 1–100, không trùng nghệ danh, không trùng người.
- [ ] 10 ca sĩ demo có mặt, đánh dấu `[demo]`: Sơn Tùng M-TP (#1), Mỹ Tâm (#2), Hà Anh Tuấn (#3), Đen (#4), Hoàng Thùy Linh (#5), Vũ. (#6), tlinh (#7), Bích Phương (#8), Erik (#9), AMEE (#10).
- [ ] Tên thật chỉ ghi khi chắc chắn; các mục ghi `—` cần batch sau xác minh lại bằng Spotify/Wikipedia trước khi crawl.
- [ ] Không ghi số lượt nghe / lượt xem cụ thể trong file này (theo tiêu chí "không bịa số liệu").

## 7. Ghi chú cho batch sau

- Thứ tự trong file KHÔNG phải thứ hạng — batch crawl cứ lấy theo số thứ tự để tiện đối chiếu, không cần crawl theo độ nổi tiếng.
- Trước khi crawl từng người, xác minh lại: (a) tên thật, (b) Spotify artist ID để tránh trùng/tách đôi 1 người, (c) 3–5 bài nổi tiếng nhất từ Spotify/YouTube/Zing, có link chính thức.
- Nếu phát hiện trùng người hoặc ca sĩ không đủ 3 bài chính thức, báo lại cho coordinator để thay thế — không tự ý đổi danh sách 100 này.
