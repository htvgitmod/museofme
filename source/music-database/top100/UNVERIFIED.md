# UNVERIFIED — File tổng Top 100 ca sĩ Việt Nam (gộp 10 batch, 13/11/2026)

> Nguyên tắc chung: trường nào chưa có nguồn kiểm chứng được thì để TRỐNG trong JSON, không đoán.
> File này gồm 2 phần: **(A)** toàn bộ UNVERIFIED.md của 10 batch, giữ nguyên nội dung từng batch;
> **(B)** các mâu thuẫn và vấn đề PHÁT HIỆN KHI GỘP (mục 2–4) — gồm các đính chính cần
> coordinator/John chốt, KHÔNG tự sửa `top100-list.md`.

## 0. Giới hạn hệ thống ảnh hưởng toàn bộ file tổng

- **Spotify Web API `not_connected` ở nhiều batch** (ghi rõ trong UNVERIFIED batch 31-40 §1,
  41-50 §1, 81-90 §1, 91-100 §1; batch 11-20 và 61-70 không có token; batch 51-60 chưa tra
  trực tiếp): vì vậy **Spotify ID ca sĩ chỉ 24/100, Spotify track URL chỉ 7/380 bài,
  ISRC chỉ 31/380 bài (8,2%)** — đây là giới hạn hệ thống, **không phải dữ liệu không tồn tại**.
  Cần một đợt bổ sung có kết nối Spotify để lấy Spotify ID + ISRC + duration + album.
- **VCPMC / Cục Bản quyền tác giả chưa tra được ở batch nào** (không có kênh tra cứu công khai
  phù hợp, không đăng nhập/bypass): ISWC = 0/380 bài; nhạc sĩ các bài bolero/trữ tình cũ chủ yếu
  mới đối chiếu qua Wikipedia/báo, chưa qua VCPMC.
- **MusicBrainz hay gặp HTTP 503** ngắt quãng trong lúc crawl (nhiều batch đã retry 1 lần rồi dừng,
  không retry dồn dập): một phần ISRC/duration/MBID trống vì lý do này, cần tra lại khi API ổn định.
- **Định nghĩa "% nhạc sĩ high" không thống nhất giữa các batch** (xem README.md mục 6): đa số batch
  báo bằng `confidence` của bài hát; batch 31-40 báo bằng "credit nhạc sĩ ghi rõ" (3/40 = 7,5%);
  batch 41-50 báo 33% (~14/42) mà cách tính không tái hiện được từ file JSON của chính batch đó.
  File tổng đếm lại theo một định nghĩa duy nhất (`composer_confidence == 'high'` → 62/380 = 16,3%),
  nhưng field này là `null` ở 300/380 bài vì 8/10 batch không ghi — xem README.md mục 4–5.

---

# (A) UNVERIFIED của từng batch (giữ nguyên nội dung batch)

---

## Batch batch-01-10

# Batch 01–10 — Chưa xác minh / chỉ 1 nguồn / mâu thuẫn

Ngày kiểm chứng: 13/11/2026. Nguyên tắc: trường nào chưa đủ bằng chứng thì để TRỐNG trong JSON, không đoán.
Nguồn chính đã dùng: Wikidata (MBID, Spotify ID, ngày sinh, ảnh Commons), MusicBrainz (ISRC, duration, ngày phát hành bản ghi),
Wikipedia vi/en (nhạc sĩ, năm, album), Apple Music, Gaana, VnExpress, Kenh14, CafeF, Thể thao & Văn hóa, VOV, Dân Việt, Znews, Eva.
Không tra được VCPMC / Cục Bản quyền tác giả (không có tra cứu công khai phù hợp, không đăng nhập) — ISWC vì vậy để trống toàn bộ.

## 1. Mâu thuẫn giữa các nguồn

| # | Mục | Mâu thuẫn | Cách xử lý trong JSON |
|---|-----|-----------|----------------------|
| 1 | Đen — nơi sinh | vi Wikipedia + VnExpress: Hạ Long, Quảng Ninh. En Wikipedia: tỉnh Đồng Nai. Wikidata P19 (Q36235) tra nhãn ra Hưng Yên (không khớp cả hai). | Ghi "Hạ Long, Quảng Ninh" (2 nguồn vi), confidence ca sĩ vẫn high nhưng ghi chú mâu thuẫn trong singers.json |
| 2 | Sơn Tùng M-TP — "Lạc Trôi" năm phát hành | MusicBrainz + en Wikipedia: 31/12/2016. Vi Wikipedia infobox: 1/1/2017 (ngày MV lên YouTube). | Ghi year 2016 (ngày phát hành bản ghi), confidence high |
| 3 | Sơn Tùng M-TP — years_active | Wikipedia vi + zh-yue: 2012–nay. Wikidata P2031 (work period start): 2009. | Ghi 2012–nay theo Wikipedia |
| 4 | Mỹ Tâm — "Họa Mi Tóc Nâu" năm/album | Vi + en Wikipedia: album Yesterday & Now, 2003. BlogAnChoi: ra mắt 2002 trong "album cùng tên (Vol.2)". | Ghi 2003 / Yesterday & Now theo Wikipedia |
| 5 | Hà Anh Tuấn — "Có Chàng Trai Viết Lên Cây" năm | Album "Truyện Ngắn" phát hành 7–8/11/2020 (Gaana, MusicBrainz). Bài hát đã được hát live từ 2018, có thể có bản single sớm hơn nhưng không tìm được nguồn chắc chắn. | Ghi year 2020 (bản album), confidence medium |
| 6 | Hà Anh Tuấn — "Xuân Thì" năm | Hát live lần đầu 23/12/2018; album "Truyện Ngắn" 2020. | Ghi year 2020 (bản album), confidence medium |
| 7 | Vũ. — "Bước Qua Nhau" năm | Wikipedia/Kenh14 gắn bài với album Một Vạn Năm (2022) và đề cử Cống hiến 2019; MusicBrainz single "Bước Qua Nhau" ghi 2021-11-11. Năm MV/single gốc chưa đối chiếu được chắc chắn (khả năng 2020). | Ghi year 2020, confidence medium |
| 8 | Vũ. — tên bài demo sai | Bản demo cũ ghi "Mùa Mưa Ngâu Nằm Cạnh Nhau". Wikipedia vi (danh sách MV) ghi "Mùa mưa ngâu nằm cạnh", MV 25/9/2016. | Đã sửa thành "Mùa Mưa Ngâu Nằm Cạnh" trong songs.json |
| 9 | tlinh — "Thích Quá Rùi Nà" feat | Bản demo/ký ức phổ biến hay nhầm với MCK. Wikipedia vi + Kworb Spotify Chart + MusicBrainz đều ghi feat. Trung Trần, phát hành 24/3/2020. | Ghi feat. Trung Trần, KHÔNG phải MCK |
| 10 | AMEE — "Sao Anh Chưa Về Nhà" duration | Wikipedia en tracklist album dreAMEE: 4:04 (244s). MusicBrainz chỉ có bản acoustic, 246s, ISRC DGA052095702. | Ghi 244s (bản album), ISRC ghi kèm chú thích "bản acoustic" trong sources |
| 11 | AMEE — "Yêu Thì Yêu Không Yêu Thì Yêu" duration/ISRC | Wikipedia en: 3:10 (190s). MusicBrainz chỉ có bản acoustic, 163s, ISRC DGA052095699. | Ghi 190s (bản album), ISRC ghi kèm chú thích "bản acoustic" |
| 12 | AMEE — "Ex's Hate Me" duration | MusicBrainz chỉ có bản phát hành lại 2023-04-15, 258s; chưa có duration bản gốc 2019. | Ghi 258s, confidence medium, chú thích bản 2023 |

## 2. Trường để trống (không có nguồn kiểm chứng được)

### Ca sĩ
- **Spotify ID / URL — 5/10 chưa có:** Mỹ Tâm, Đen, Hoàng Thùy Linh, Erik, Vũ. — Wikidata không có P1902 cho 5 người này; tìm kiếm web không trả về URL open.spotify.com/artist đã kiểm chứng. ĐÃ CÓ: Sơn Tùng M-TP, Hà Anh Tuấn, tlinh, Bích Phương, AMEE.
- **Labels — 2/10 để trống:** Hà Anh Tuấn, Đen (chưa tìm được hãng đĩa xác thực từ Wikipedia/Wikidata; không đoán).
- **Image license:** cả 10 ảnh đều chỉ ghi tên file Wikimedia Commons (Wikidata P18) + link trang file; chưa rà giấy phép từng file (CC-BY/CC-BY-SA/public domain) — cần rà trước khi hiển thị/hotlink.
- **tlinh — labels:** ghi "M Music Records" theo Shazam (đơn vị phát hành album "ái") — chỉ 1 nguồn, coi là medium, cần đối chiếu thêm.

### Bài hát — ISRC (chỉ 16/40 có, 40%)
Không có ISRC (MusicBrainz không gắn ISRC cho bản ghi đó, và không đoán ISRC):
Sơn Tùng M-TP "Chạy Ngay Đi"; Mỹ Tâm "Người Hãy Quên Em Đi", "Đừng Hỏi Em", "Đâu Chỉ Riêng Em";
Đen "Đưa Nhau Đi Trốn", "Hai Triệu Năm", "Mang Tiền Về Cho Mẹ";
Hoàng Thùy Linh "Để Mị Nói Cho Mà Nghe", "See Tình";
Vũ. "Bước Qua Nhau", "Bước Qua Mùa Cô Đơn", "Mùa Mưa Ngâu Nằm Cạnh";
tlinh cả 4 bài ("Gái Độc Thân", "Nếu Lúc Đó", "Thích Quá Rùi Nà", "vaicaunoicokhiennguoithaydoi");
Bích Phương "Bùa Yêu", "Đi Đu Đưa Đi", "Bao Giờ Lấy Chồng";
Erik cả 4 bài (MusicBrainz không tìm thấy bản ghi nào cho Erik — 0/4).
- **ISWC: 0/40** — không tra được từ nguồn công khai nào trong batch này.

### Bài hát — duration (30/40 có)
Chưa có duration: "Chạy Ngay Đi"; "Mang Tiền Về Cho Mẹ"; "Mùa Mưa Ngâu Nằm Cạnh"; "vaicaunoicokhiennguoithaydoi";
"Bùa Yêu"; "Đi Đu Đưa Đi"; Erik cả 4 bài ("Sau Tất Cả", "Chạm Đáy Nỗi Đau", "Dù Cho Tận Thế", "Có Tất Cả Nhưng Thiếu Anh").

### Bài hát — YouTube official (chỉ 1/40 có link đã kiểm chứng)
- Chỉ có "Lạc Trôi" — https://www.youtube.com/watch?v=Llw9Q6akRo4 (link embed trên trang lời bài hát, trỏ tới MV chính thức; confidence medium).
- 39 bài còn lại: MV official chắc chắn tồn tại trên kênh official của ca sĩ/hãng, nhưng batch này KHÔNG đoán video ID. Cần tra lại từng MV trên kênh official (Sơn Tùng M-TP Official, Mỹ Tâm, Hà Anh Tuấn, Đen Vâu Official, Hoàng Thùy Linh, Vũ Official, tlinh, Bích Phương, Erik, AMEE) để lấy đúng video ID.
- Lưu ý: link YouTube tìm được cho "Chạy Ngay Đi (Onionn Remix)" (https://www.youtube.com/watch?v=-vtBgNxMyZI) là bản remix, KHÔNG phải bản gốc nên không ghi vào bản gốc.

### Bài hát — Spotify/Apple Music link (chỉ 2/40 có)
- "Tháng Tư Là Lời Nói Dối Của Em" — Apple Music (link đã kiểm chứng trong search).
- "Gái Độc Thân" — Apple Music (link đã kiểm chứng trong search).
- 38 bài còn lại để trống (không có Spotify API key trong batch này; không đoán URL track).

### Bài hát — nhạc sĩ chưa xác minh
- Erik "Dù Cho Tận Thế" (2025) — composers để trống, composer_confidence low. Chỉ biết MV ra 6/2/2025, nhạc phim "Bộ tứ báo thủ" (nguồn CamAmSao). Cần tra credits MV.
- tlinh "vaicaunoicokhiennguoithaydoi" (2022) — composers để trống, composer_confidence low. Chỉ xác minh được Grey D hát chính + tlinh feat (Thể thao & Văn hóa, ELLE Man).
- "Gái Độc Thân" — composers ghi ["tlinh"] theo Gaana + Apple Music; vai trò 2pillz là producer (chưa rõ có đồng sáng tác không).

### Bài hát — hook_line (chỉ 1/40 có)
- Chỉ "Tháng Tư Là Lời Nói Dối Của Em" có câu mở đầu đã kiểm chứng trong nguồn ("Mùa xuân có em như chưa bắt đầu" — VnExpress/Thể thao & Văn hóa). 39 bài còn lại để trống, KHÔNG chép lời từ trí nhớ.

### Bài hát — lyric_url (0/40)
- Chưa ghi link trang lời cho bài nào (chưa đối chiếu trang lời có bản quyền như NhacCuaTui/Zing MP3 từng bài).

## 3. Chỉ 1 nguồn (confidence medium) — cần nguồn thứ 2
- Hà Anh Tuấn "Có Chàng Trai Viết Lên Cây", "Xuân Thì" (năm 2020 bản album — xem mục 5, 6).
- Vũ. "Bước Qua Nhau" (năm 2020 — xem mục 7), "Mùa Mưa Ngâu Nằm Cạnh" (chưa có duration/ISRC/MusicBrainz).
- tlinh "Thích Quá Rùi Nà" (duration 178s lấy từ bản phát hành lại MusicBrainz 2023, chưa chắc bằng bản gốc 2020).
- AMEE "Sao Anh Chưa Về Nhà", "Ex's Hate Me", "Yêu Thì Yêu Không Yêu Thì Yêu" (xem mục 10–12).
- Erik "Dù Cho Tận Thế" (chỉ 1 nguồn CamAmSao cho năm 2025).
- tlinh "vaicaunoicokhiennguoithaydoi" (chỉ 2 nguồn báo cho feat, chưa có nhạc sĩ/duration/ISRC).

## 4. Hạn chế kỹ thuật trong batch này
- MusicBrainz trả 503 ngắt quãng trong lúc crawl (đã retry 1 lần bằng cách chạy lại script; các bản ghi 503 lần 2 vẫn để trống, không retry dồn dập).
- MusicBrainz search theo tên dễ nhầm (Đen → Den Harrow, Erik → Erik Satie, Hà Anh Tuấn → "Anh Tuấn") — đã khắc phục bằng cách lấy MBID từ Wikidata P434 thay vì search tên.
- Không có Spotify API key / Apple Music API trong batch này nên không lấy được Spotify track URL, ISRC từ Spotify, hay monthly listeners.
- Không đăng nhập / không tra VCPMC, Cục Bản quyền tác giả (không có tra cứu công khai phù hợp) — ISWC để trống toàn bộ.

---

## Batch batch-11-20

# UNVERIFIED — Batch 11–20 (kiểm chứng ngày 13/11/2026)

> Nguyên tắc: trường nào chưa có nguồn độc lập kiểm chứng được thì để TRỐNG trong JSON, không đoán. File này liệt kê mọi trường trống / 1 nguồn / mâu thuẫn.

## 1. Toàn batch — trường trống ở hầu hết các bài

- **ISRC**: chỉ 3/40 bài có ISRC kiểm chứng qua MusicBrainz recording search:
  - “Waiting for You” (MONO) — USY6C0710009
  - “Ánh Nắng Của Anh” (Đức Phúc) — VNA0M1800964
  - “Bên Trên Tầng Lầu” (Tăng Duy Tân) — VNA0R2000662
  - 37/40 bài còn lại: MusicBrainz không trả ISRC (không có recording, hoặc recording không kèm ISRC). Cần tra tiếp qua Spotify API / Apple Music / ISRC database, không đoán.
- **ISWC**: 0/40 — chưa tra được bài nào (ISWC không có sẵn trên MusicBrainz recording công khai cho các bài này).
- **YouTube official**: chỉ 1/40 có URL kiểm chứng trực tiếp:
  - “Không Thể Say” (HIEUTHUHAI) — https://www.youtube.com/watch?v=d6pgocXnK8U (mô tả ghi Music Composer: HIEUTHUHAI)
  - 39 bài còn lại chưa mở được link MV official để xác nhận video ID — KHÔNG đoán video ID. Kênh YouTube official đã xác minh qua MusicBrainz url-rels cho: Hòa Minzy (UCjm_FW7t1gam7qLldSVOclw), HIEUTHUHAI (UCe8b9jSSD-bNabF4hkNN5PQ), Jack (UChUJa1JyBc7Lc4orkiNKKQg), Tóc Tiên (UCMwN2073L0Nyx0yN1HNhuLQ).
- **Apple Music URL**: 0/40 — chưa kiểm chứng.
- **lyric_url**: 0/40 — chưa chọn trang lời có bản quyền để dẫn (không chép lời).
- **hook_line**: 0/40 — để trống, không chép câu mở đầu khi chưa đối chiếu lời từ nguồn có bản quyền.
- **duration_seconds**: chỉ 1/40 — “Đưa Em Về Nhàa” = 240 giây (JioSaavn). Các bài còn lại chưa tra.
- **image_url**: 0/10 ca sĩ — chưa xác minh URL ảnh Wikimedia Commons/Wikipedia kèm license; không hotlink ảnh random có bản quyền.

## 2. Ca sĩ — thiếu / mâu thuẫn

| Ca sĩ | Vấn đề |
|---|---|
| Grey D | **Không có MusicBrainz ID và Spotify artist ID**: đã thử MB search “GREY D / Grey-D / Grey D” nhiều lần, không có bản ghi VN khớp. Spotify artist ID chưa tra được (chỉ có Spotify track ID của “vaicaunoicokhiennguoithaydoi”). **Mâu thuẫn ngày sinh**: Wikipedia ghi 11/12/2000, bloganchoi.com ghi 04/11/2000 — JSON lấy 11/12/2000 theo Wikipedia, cần đối chiếu thêm. Confidence ca sĩ = medium. |
| Đức Phúc, Hòa Minzy, Tóc Tiên, Văn Mai Hương | **labels[] để trống** — chưa xác minh hãng đĩa hiện tại từ 2 nguồn. |
| Tóc Tiên | **years_active “1996–nay” chỉ 1 nguồn** (it.wikipedia: “1996 – in attività”); en.wikipedia chỉ nói “began career when still a child”. Confidence ca sĩ = medium. **labels[] trống.** |
| Văn Mai Hương | **Mâu thuẫn tên thật**: Wikipedia ghi “Văn Mai Hương”, Kenh14 ghi “Nguyễn Văn Mai Hương” — JSON lấy theo Wikipedia, cần đối chiếu thêm. |
| MONO | **Mâu thuẫn ngày sinh**: Wikipedia vi/en ghi 21/1/2000, báo Thanh Niên (7/8/2022) ghi 20/1/2000 — JSON lấy 21/1/2000 (đa số nguồn), cần đối chiếu thêm. |
| Tăng Duy Tân | **labels[] = Big Arts Entertainment** (anh là CEO/điều hành sản xuất) — vai trò hãng đĩa chưa đối chiếu 2 nguồn, chỉ medium. |
| HIEUTHUHAI | **years_active “2020–nay”** suy từ King of Rap 2020, chưa có nguồn ghi rõ khoảng hoạt động. |

## 3. Bài hát — nhạc sĩ chỉ 1 nguồn (confidence = medium)

Các bài sau nhạc sĩ chỉ có 1 nguồn độc lập (thường là Wikipedia hoặc suy từ “tự sáng tác toàn bộ album”), cần đối chiếu thêm trước khi nâng lên high:

- **MONO** — “Quên Anh Đi”, “Em Là”, “Anh Không Thể”: nhạc sĩ MONO ở mức album (album 22 “8 bài do chính MONO chấp bút”), chưa đối chiếu credit từng track.
- **Đức Phúc** — “Chỉ Một Câu”: Phạm Toàn Thắng (Wikipedia).
- **Hòa Minzy** — “Thị Mầu”: Nguyễn Hoàng Phong (1 bài báo Gia đình & Xã hội + Wikipedia ghi năm 2023).
- **HIEUTHUHAI** — “Vệ Tinh”, “Ngủ Một Mình”, “Exit Sign”: nhạc sĩ HIEUTHUHAI (tự sáng tác, prod. Kewtiie) — chưa có credit từng bài từ 2 nguồn.
- **Grey D** — “vaicaunoicokhiennguoithaydoi”, “Dự Báo Thời Tiết Hôm Nay Mưa”, “Đưa Em Về Nhàa”: Grey D tự sáng tác (Wikipedia + JioSaavn cho bài thứ ba).
- **Quang Hùng MasterD** — “Ánh Mắt Biết Cười”: nhạc sĩ Quang Hùng MasterD chưa đối chiếu credit từng bài.
- **Tăng Duy Tân** — “Hết Duyên”, “Dạ Vũ”, “Cắt Đôi Nỗi Sầu”: nhạc sĩ Tăng Duy Tân (chưa đối chiếu credit từng bài từ 2 nguồn).
- **Jack** — “Hồng Nhan”, “Bạc Phận”, “Sóng Gió”: nhạc sĩ Jack (vai trò sáng tác chung, K-ICM là producer — cần phân biệt rõ composer vs producer từng bài).
- **Văn Mai Hương** — “Cầu Hôn”, “Mưa Tháng Sáu”, “Đại Minh Tinh”: nhạc sĩ Hứa Kim Tuyền — suy từ vai trò producer album Hương/Minh Tinh, **chưa đối chiếu credit nhạc sĩ từng bài** (producer ≠ composer).

## 4. Bài hát — nhạc sĩ để trống

- **Tóc Tiên — “Nước Mắt Em Lau Bằng Tình Yêu Mới” (2019)** và **“906090” (2022)**: composers[] = [] — chưa xác minh nhạc sĩ. (Bài đầu là bài của Da LAB có Tóc Tiên góp giọng.)

## 5. Mâu thuẫn năm phát hành

- **Tăng Duy Tân — “Bên Trên Tầng Lầu”**: thân bài Wikipedia vi ghi phát hành tháng 8/2021; bảng đĩa đơn Wikipedia ghi 2022; Soha/Kenh14 ghi 2022. JSON tạm lấy **2021** (theo thân bài Wikipedia) + confidence medium. Cần đối chiếu ngày phát hành chính thức (Spotify/Apple Music).

## 6. Chưa tra / chưa làm được trong batch này

- VCPMC / Cục Bản quyền tác giả: chưa tra được nhạc sĩ qua 2 nguồn này (không đăng nhập, không bypass) — nhạc sĩ hiện dựa vào Wikipedia + báo + mô tả YouTube official + JioSaavn.
- Spotify Web API: không có token trong batch này — Spotify artist ID lấy qua MusicBrainz url-rels (đã kiểm chứng chéo với kworb cho MONO: 5jTFNkoZebPnX90CbB3F2A), Spotify track ID chỉ có 3 bài qua kworb.
- Ảnh đại diện ca sĩ (Wikimedia Commons + license): chưa xác minh URL nào.
- Lượt nghe/stream cụ thể: không ghi vào JSON (trừ ghi chú evidence có nguồn, VD Exit Sign >110 triệu stream Spotify theo DatVietVAC).

---

## Batch batch-21-30

# Chưa xác minh — Batch 21-30 (Trúc Nhân, Min, Bảo Anh, Soobin Hoàng Sơn, Isaac, Chi Pu, Quân A.P, Lou Hoàng, Anh Tú Atus, Rhyder)

Ngày kiểm chứng: 13/11/2026. Quy tắc: trường nào chưa có nguồn độc lập thì để trống trong JSON, không đoán.

## 1. Ca sĩ — trường trống / độ tin cậy thấp

| Ca sĩ | Vấn đề |
|---|---|
| Isaac | Không tìm thấy Spotify artist ID (chỉ có Apple Music artist 1200463483, chưa kiểm chứng qua API) → `spotify_id`/`spotify_url` = null. |
| Anh Tú Atus | Không tìm thấy Spotify artist ID và không có MusicBrainz artist → cả hai đều null. `confidence` = medium (chỉ có Wikipedia vi + Wikidata Q111086636). |
| Rhyder | MusicBrainz ID `db9d9046-b75b-49e2-9d7a-02b73d079268` chưa xác nhận chắc chắn (MB artist "RHYDER" không ghi quốc gia; Wikidata không có MBID) → `confidence` = medium. |
| Lou Hoàng | Không có ảnh trên Wikidata/Wikimedia Commons → `image_url` = null. |
| Bảo Anh, Lou Hoàng | Hãng đĩa chưa xác định được → `labels` = []. |
| Min | Năm hoạt động: Wikipedia vi ghi 2013–nay, Wikipedia en ghi 2012–nay → dùng 2013 (vi). |
| Chi Pu, Quân A.P, Lou Hoàng, Anh Tú Atus | `genres` chỉ ở mức medium (infobox Wikipedia không liệt kê đầy đủ thể loại). |
| Tất cả 9 ảnh Commons | URL ảnh lấy từ Wikidata P18 (Special:FilePath) nhưng **giấy phép (license) từng file chưa kiểm chứng** → `image_license` = null cho tất cả. Cần rà license từng file trước khi hiển thị công khai. |

## 2. Bài hát — nhạc sĩ chưa xác minh (composers = [])

| Bài | Vấn đề |
|---|---|
| Chi Pu — "Từ hôm nay (Feel Like Ooh)" (2017) | Nhạc sĩ là các nhạc sĩ Hàn Quốc qua Krazy Sound, chưa tra được tên cụ thể → `composers` = [], `composer_confidence` = low. |
| Rhyder — "Chịu cách mình nói thua" (2023) | Không tìm thấy credit nhạc sĩ công bố (VOH chỉ ám chỉ Rhyder là tác giả, không ghi tên credit) → `composers` = [], low. |
| Rhyder — "Anh biết rồi" (2024) | Không tìm thấy credit nhạc sĩ → `composers` = [], low. |
| Rhyder — "Hào quang" (2024) | Không tìm thấy credit nhạc sĩ → `composers` = [], low. |

## 3. Bài hát — nhạc sĩ chỉ 1 nguồn (composer_confidence = medium)

| Bài | Nhạc sĩ (1 nguồn) |
|---|---|
| Bảo Anh — "Như lời đồn" | Khắc Hưng (chỉ Wikipedia vi — Bảo Anh). |
| Soobin — "Anh đã quen với cô đơn" | Soobin Hoàng Sơn (chỉ Wikipedia vi — bảng MV). |
| Soobin — "Heyyy" | SOOBIN (chỉ Wikipedia vi — bảng MV; Spotify track đã kiểm chứng nhưng không ghi nhạc sĩ). |
| Quân A.P — "Còn gì đau hơn chữ đã từng" | RIN9 (chỉ Wikipedia vi — Quân A.P). |
| Quân A.P — "Bông hoa đẹp nhất" | Vũ Hà Anh, Phan Viết Tính, Nguyễn Văn Trung (chỉ Wikipedia vi — Quân A.P). |
| Quân A.P — "Lời xin lỗi vụng về" | Vũ Hà Anh (chỉ Wikipedia vi — Quân A.P). |
| Lou Hoàng — "Mình là gì của nhau" | Lou Hoàng, Only C (chỉ Wikipedia vi — Lou Hoàng). |
| Lou Hoàng — "Đếm ngày xa em" | Nguyên Jenda (chỉ Wikipedia vi — Lou Hoàng). |
| Lou Hoàng — "Yêu một người có lẽ" | Only C, T.I.N, Lou Hoàng (chỉ Wikipedia vi — Lou Hoàng). |
| Lou Hoàng — "Cảm giác lúc ấy sẽ ra sao" | Hưng Cacao, Only C, Lou Hoàng (chỉ Wikipedia vi — Lou Hoàng). |
| Anh Tú — "Mình làm người yêu nhé em" | Vương Anh Tú (chỉ danh sách tác phẩm trên Wikipedia vi — Vương Anh Tú). |
| Isaac — "Mr. Right (Khi anh yêu em)" | Xem mục 4 — mâu thuẫn nguồn, đã hạ xuống medium. |

## 4. Mâu thuẫn giữa các nguồn (đã ghi nhận, chưa ngã ngũ)

- **Isaac — "Mr. Right (Khi anh yêu em)"**: Wikipedia vi — Only C ghi "lời của Mr. Doji" (nhạc: Only C); Gaana ghi "composed by OnlyC"; nhưng VTC News (danh sách bình chọn Bài hát yêu thích tháng 7/2015) ghi "Nhạc: Hoàng Touliver, Lời: OnlyC". Isaac Wikipedia ghi "do Hoàng Touliver sản xuất". → Giữ `composers` = [Only C], `lyricists` = [Mr. Doji] theo đa số, hạ `composer_confidence` = medium. Cần đối chiếu thêm (VCPMC / mô tả MV gốc) trước khi dùng làm dữ liệu bán hàng.
- **Isaac — "Tôi đã quên thật rồi"**: trang lời thuthuat.taimienphi.vn tự mâu thuẫn nội bộ — đoạn mở đầu ghi "sáng tác của nhạc sĩ Lou Hoàng", phần thân bài ghi "giai điệu bắt tai được nhạc sĩ Nguyễn Phúc Thiện sáng tác". Đa số (24h, Văn hóa Đời sống, Wikipedia) nói Nguyễn Phúc Thiện → giữ Nguyễn Phúc Thiện. Cùng trang này còn ghi MV quay ở Hàn Quốc ("xứ sở kim chi") trong khi 24h/Wikipedia ghi Đài Loan → tin Đài Loan.
- **Min — "Có em chờ"**: vanhoadoisong.vn liệt kê "Sáng tác: Khắc Hưng" cho bài này, mâu thuẫn với Wikipedia vi ("Sáng tác: Kai Đinh, Sản xuất: Khắc Hưng"), mô tả YouTube (Orchestra Version: "Composer: Kai Đinh") và phỏng vấn Znews của Min → giữ Kai Đinh; Khắc Hưng là nhà sản xuất, không phải nhạc sĩ.
- **Isaac — "Yêu không nghỉ phép"**: Wikipedia vi — Only C liệt kê bài này trong danh sách sáng tác của Only C, mâu thuẫn với Dân Việt, Kenh14, Văn hóa Đời sống và bảng Hòa âm Ánh sáng (đều ghi Nguyễn Phúc Thiện, em ruột Only C) → giữ Nguyễn Phúc Thiện.
- **Bảo Anh — "Sống xa anh chẳng dễ dàng"**: Wikipedia vi — Mr. Siro ghi "(Bảo Anh ft. Mr. Siro)"; trang lời thuthuat có đoạn lời ghi "[Mr.Siro:]" → có thể Mr. Siro có góp giọng, nhưng bài hát trong batch vẫn chỉ ghi `singers` = [Bảo Anh] vì Wikipedia vi — Bảo Anh không ghi feat. Cần kiểm chứng MV gốc trước khi thêm Mr. Siro vào `singers`.
- **Chi Pu — "Đóa hoa hồng (Queen)"**: tên nhạc sĩ ghi "Andiez - NNeo" (theo Wikipedia en + mô tả MV); chưa rõ "NNeo" là nghệ danh của ai → giữ nguyên chuỗi "Andiez - NNeo".

## 5. Ngày phát hành mâu thuẫn (chỉ ghi năm trong JSON)

| Bài | Mâu thuẫn |
|---|---|
| Bảo Anh — "Anh muốn em sống sao" | Audio 26/8/2013 (Tripi/Tadiha) vs MV 22–23/1/2014 (Wikipedia) → year = 2014. |
| Bảo Anh — "Trái tim em cũng biết đau" | 26/4/2016 (Tadiha) vs 3/6/2016 (Tripi) → chỉ ghi năm 2016. |
| Bảo Anh — "Sống xa anh chẳng dễ dàng" | 1/11/2017 (Tripi/Tadiha) vs 8/11/2017 (Wikipedia en; thuthuat ghi "MV ra mắt tối 8/11/2017") → chỉ ghi năm 2017. |
| Trúc Nhân — "Thật bất ngờ" | Hồ sơ đề cử Cống hiến ghi phát hành tháng 8/2015; Wikipedia ghi MV 4/12/2015 → year = 2015. |
| Soobin — "Đi để trở về" | 1/1/2017 (Wikipedia) vs 2/1/2017 (Bách Hóa Xanh) → year = 2017. |
| Quân A.P — "Ai là người thương em" | 9/5/2019 (Wikipedia) vs "Tháng 6/2019" (Saostar, phỏng vấn Quân A.P) → year = 2019. |
| Rhyder — "Chịu cách mình nói thua" | Bảng đĩa đơn Wikipedia vi xếp bài này dưới năm 2020 (sai); phần prose + MusicBrainz ghi cuối tháng 11/2023 → year = 2023. |

## 6. Thời lượng mâu thuẫn / trống

- "Thật bất ngờ": Wikipedia 3:33 (213s) vs MusicBrainz 209,9s → giữ 213 (Wikipedia).
- "Phía sau một cô gái": MusicBrainz 330s (5:30) vs lyric video chính thức ~4:32 → giữ 330 (MB), có thể là bản khác.
- "Đi để trở về": MusicBrainz 202s vs thegioinem ghi MV 3:50 (230s) → giữ 202 (MB).
- "Chịu cách mình nói thua": 2 bản ghi MusicBrainz 182s và 193s → giữ 182 (bản có ISRC).
- **Thời lượng trống (14/40 bài)**: toàn bộ 4 bài Isaac, 4 bài Quân A.P, 4 bài Anh Tú, Chi Pu "Cung đàn vỡ đôi", Lou Hoàng "Cảm giác lúc ấy sẽ ra sao" (không có bản ghi MusicBrainz; chưa tra Spotify/Apple Music).

## 7. ISRC — lưu ý

- Min — "Y.Ê.U": ISRC `FRX762174975` lấy từ bản ghi MusicBrainz phát hành lại ngày 30/11/2021, **chưa xác nhận là ISRC của bản gốc 2015**.
- Bảo Anh — "Anh muốn em sống sao": MusicBrainz trả về **2 ISRC** (`VNR011038027`, `VNR011046964`); JSON chỉ giữ ISRC đầu, ISRC thứ hai ghi ở đây.
- Không có ISWC nào được xác minh cho cả 40 bài → `iswc` = null toàn bộ.
- Chỉ 12/40 bài có ISRC (30%).

## 8. Link YouTube / Spotify / Apple Music — chưa kiểm chứng

- **YouTube official chưa kiểm chứng: 29/40 bài** (để trống, không đoán video ID): toàn bộ Bảo Anh (4), Isaac (4), Quân A.P (4), Lou Hoàng (4), Anh Tú (4); Min "Ghen"; Soobin "Anh đã quen với cô đơn", "Heyyy"; Chi Pu "Từ hôm nay", "Anh ơi ở lại", "Cung đàn vỡ đôi"; Rhyder "Chịu cách mình nói thua", "Anh biết rồi", "Hào quang".
- Min — "Ghen": **KHÔNG dùng** video "Ghen Cô Vy" (`BtulL3oArQw`) — đó là bài khác (phiên bản COVID-19 năm 2020).
- Soobin — "Phía sau một cô gái": **KHÔNG dùng** video `w1_EJefzZMk` — đó là bản cover của fan (Kiyushi), không phải official.
- Isaac — "Anh sẽ về sớm thôi": video `xcUIBHapq20` xuất hiện trong kết quả ELLE chỉ là **teaser**, không phải MV chính thức → không dùng.
- Spotify track URL chỉ kiểm chứng được 1/40 bài (SOOBIN "Heyyy": `2fWYqr8yaQitqsjHMEstVh`).
- Apple Music track URL: 0/40 (chưa kiểm chứng bài nào).

## 9. Ghi chú kỹ thuật

- MusicBrainz API trả lỗi 503 gián đoạn trong lúc tra cứu (Min "Có em chờ", Soobin "Anh đã quen với cô đơn", Rhyder "Hào quang", Lou Hoàng "Cảm giác lúc ấy sẽ ra sao", Quân A.P "Lời xin lỗi vụng về", Chi Pu "Cung đàn vỡ đôi", Rhyder "Dân chơi sao phải khóc") — đã retry; kết quả trống sau retry được coi là không có bản ghi MusicBrainz.
- Edges ca sĩ–ca sĩ chỉ nối các ca sĩ trong Top 100 (Erik #9, LyLy #50, Andree Right Hand #42). Các nghệ sĩ feat. ngoài Top 100 (Trương Thảo Nhi, Mr.A, Only C, Miu Lê, Ban, CoolKid, Wokeup) chỉ xuất hiện trong `singers[]` của bài hát, không tạo node/edge.
- "Đi để trở về": Bách Hóa Xanh liệt kê "Album: Đi để trở về" — có thể chỉ là tên đĩa đơn, chưa xác nhận là album thật → `album` = null.

---

## Batch batch-31-40

# UNVERIFIED — Batch 31–40 (Binz, Karik, Suboi, Wowy, Rhymastic, JustaTee, BigDaddy, MCK, Low G, Obito)

> Nguyên tắc: trường nào chưa có nguồn thì để TRỐNG, không đoán. Cập nhật ngày 13/11/2026.

## 1. Spotify — chưa xác minh được cho cả 10 ca sĩ

- **spotify_id / spotify_url của cả 10 ca sĩ đều để trống.** Lý do: Spotify connector (`spotify-api`) ở trạng thái `not_connected` (không có config), MusicBrainz `url-rels` không trả về link Spotify cho các nghệ sĩ này.
- Music Metrics Vault có 2 trang trùng tên cho Binz (`/artists/binz/7lWmI63NFoOcNbFMHeYn79` và `/artists/binz/0CSEUsE0rQqZGrHHoZQdoL`) — không rõ trang nào là đúng nên KHÔNG dùng.
- Chỉ 2 bài có `spotify_url` đã kiểm chứng qua Kworb (trang Spotify chart của Kworb cho đúng track đó):
  - Binz — "Cho Mình Em": `https://open.spotify.com/track/51bYFYWODfYOZU0rwvjiCc`
  - MCK — "Chìm Sâu": `https://open.spotify.com/track/7jLSThU5Kg1RWt19Leiaxm`
- Cần làm sau: kết nối Spotify rồi chạy `spotify-api search --search-type ARTISTS` cho từng người để lấy ID chuẩn.

## 2. ISRC / ISWC — 0/40 bài có ISRC

- Tra MusicBrainz Recording API cho 10 bài đại diện (Bigcityboi, Cho Mình Em, Người Lạ Ơi, N-Sao?, Khu Tao Sống, Yêu 5, Đã Lỡ Yêu Em Nhiều, Mượn Rượu Tỏ Tình, Chìm Sâu, Simple Love): các recording **có tồn tại trên MusicBrainz nhưng không gắn ISRC nào**; 3 truy vấn còn gặp HTTP 503.
- `isrc` và `iswc` của toàn bộ 40 bài đều để trống. Không tra được qua VCPMC/Cục Bản quyền (không đăng nhập trái phép, không bypass).
- Cần làm sau: tra ISRC qua Spotify API (khi đã kết nối) hoặc qua Apple Music API có quyền, hoặc tra cứu VCPMC công khai theo từng bài.

## 3. Mâu thuẫn giữa các nguồn (ngày sinh)

| Ca sĩ | Nguồn A | Nguồn B | Cách xử lý trong file |
|---|---|---|---|
| Rhymastic | Wikipedia EN: 08/04/1991, Hà Nội | MusicBrainz: begin 1991-08-04 | Dùng 08/04/1991 (Wikipedia), confidence ca sĩ = medium |
| JustaTee | Wikipedia EN: 01/11/1990, Hà Nội | MusicBrainz: begin 1991-11-01 | Dùng 01/11/1990 (Wikipedia + thecityceleb + ask-oracle), confidence = medium |
| Wowy | top100-list + Fandom: tên thật Nguyễn Minh Huy | Fandom Masked Singer: "Nguyễn Ngọc Minh Huy" | Dùng Nguyễn Minh Huy (theo danh sách chốt); chỉ có năm sinh 1988, **không có ngày/tháng sinh** |
| Binz | MusicBrainz begin 1988-05-24; nguoinoitieng.tv 24-5-1988 | vietnam.vn chỉ ghi sinh năm 1988, Gia Lai | Dùng 24/05/1988 (2 nguồn khớp ngày) |

## 4. YouTube official — chỉ 3/40 bài có link đã kiểm chứng

Có link: Binz "Bigcityboi" (`jgZkrA8E5do`, nhúng trong bài VnExpress về MV), Binz "Cho Mình Em" (`2OKYsYErfFo`, nhúng trong bài The Dot Magazine), Obito "Lost" (`AjYHDs63jrk`, nhúng trong bài NME về Def Jam Vietnam).
37 bài còn lại chưa có `youtube_official_url` — **không đoán video ID**. Cần mở kênh YouTube official từng ca sĩ để lấy link MV từng bài.

## 5. Bài hát thiếu trường / chỉ 1 nguồn (confidence medium/low)

### Chỉ 1 nguồn metadata (chủ yếu chỉ có Apple Music/iTunes) — cần nguồn thứ 2
- JustaTee: "Đã Lỡ Yêu Em Nhiều", "Thằng Điên", "Bâng Khuâng", "Forever Alone" (chỉ iTunes).
- BigDaddy: "Nóng", "Yêu Nắm" (chỉ iTunes).
- Obito: "Hà Nội" (chỉ iTunes).
- Karik: "Có Lẽ Anh Chưa Từng" (iTunes + Viberate liệt kê chung, chưa đủ mạnh cho nhạc sĩ).
- Rhymastic: "Lặng" — xem mục low dưới đây.

### Confidence low (chỉ có tên bài, thiếu năm/thời lượng/nhạc sĩ)
- Rhymastic — "Lặng": Viberate liệt kê trong top bài; iTunes chỉ có bản live "Anh Trai Vượt Ngàn Chông Gai 2024" nên **năm phát hành và thời lượng bản gốc để trống**.
- BigDaddy — "Mẩy Thật Mẩy": không tìm thấy trên iTunes VN/US; **năm, album, thời lượng, link đều trống**; nhạc sĩ ghi BigDaddy là tạm (chưa có nguồn).
- Low G — "Tán Gái 101": chỉ Wikipedia liệt kê trong series Tán Gái; **năm, thời lượng trống**.
- Low G — "Flexin Trên Circle K": tên bài theo top100-list; **không tìm thấy trên iTunes, mọi trường metadata trống, sources rỗng**.

### Năm phát hành chưa xác minh (để trống)
- Binz — "OK": chỉ tìm thấy bản "OK (TINLE Remix)" 2023 trên iTunes; năm bản gốc chưa xác minh.
- Các bài trên đã ghi `year: null`.

### Mâu thuẫn năm phát hành / ngày phát hành
- Wowy — "Khu Tao Sống": single trên Apple Music 04/07/2012, nhưng CV Galerie Quynh ghi MV 2010; Blaqlyte nói "dropped in 2012". File dùng 2012 (ngày phát hành single).
- Wowy — "Chạy": single gốc 2013 theo CV Galerie Quynh; Apple Music chỉ có bản "Chạy (feat. LD SouthGanz) [From Ròm]" 28/07/2020 — file dùng 2013, **không dùng thời lượng/link của bản 2020**.
- Suboi — "Cho Không", "Bet On Me": Wikipedia/NME ghi single 2019; Apple Music hiển thị 15/06/2021 (nhiều khả năng là ngày phát hành lại theo album No Nê). File dùng 2019, giữ link Apple Music.
- BigDaddy — "Mượn Rượu Tỏ Tình": Apple Music 18/01/2019, Qobuz 18/02/2019 — chỉ lệch ngày, năm 2019 thống nhất.
- Binz — "Bigcityboi": Apple Music chỉ còn bản remix (Kriss Ngo Remix, 2026) nên **không dùng link/thời lượng Apple Music**; năm 2020 lấy từ VnExpress.

### Nhạc sĩ chỉ ở mức medium (tự sáng tác theo thông lệ, chưa có credit ghi rõ từng bài)
- Hầu hết bài rap trong batch do chính rapper sáng tác (thông lệ), nhưng credit nhạc sĩ từng bài chưa đối chiếu được với 2 nguồn độc lập — trừ 3 bài sau (xem §6).
- Karik — "Anh Không Đòi Quà": nhạc sĩ OnlyC ở mức medium.
- Karik — "Bạn Đời", "Có Lẽ Anh Chưa Từng": nhạc sĩ ghi theo ca sĩ thể hiện, chưa có credit độc lập.

## 6. Nhạc sĩ confidence high (đã có credit ghi rõ)

- Binz — "Bigcityboi": nhạc sĩ Binz (VnExpress: "Written by Binz"; PR Newswire: "As the writer of the song, Binz").
- Karik/Orange — "Người Lạ Ơi": nhạc sĩ Châu Đăng Khoa (credits MV: Music Composer Châu Đăng Khoa, Producer Superbrothers).
- BigDaddy/Emily — "Mượn Rượu Tỏ Tình": nhạc sĩ Tiên Cookie & BigDaddy (Wikipedia EN, bài Tiên Cookie — bảng songs written).
- → **3/40 bài (7,5%) có nhạc sĩ confidence high.**

## 7. Ca sĩ — trường còn trống

- **Ảnh đại diện:** chỉ 6/10 có `image_url` Wikimedia Commons kèm license (Karik, Suboi, Wowy, Rhymastic, JustaTee CC BY 3.0/4.0; BigDaddy có ảnh Commons nhưng **license chưa xác minh** nên `image_license` để trống). Binz, MCK, Low G, Obito: **không có ảnh Commons/Wikipedia đã kiểm chứng** — để trống, không hotlink ảnh có bản quyền.
- **years_active để trống:** Binz, Karik, Suboi, BigDaddy (chưa có nguồn chắc chắn; không đoán).
- **labels để trống:** Karik, MCK, Low G. MCK: YouTube ghi ℗ 2026 "ah311synd. & MCK" cho album HVL nhưng chưa đủ căn cứ ghi là label chính thức.
- **Wowy:** chỉ có năm sinh 1988, không ngày/tháng; tên thật còn mâu thuẫn (xem §3).
- **Suboi:** `years_active` để trống (album đầu 2010 nhưng năm bắt đầu hoạt động chưa xác minh).

## 8. Lời bài hát (hook_line / lyric_url)

- Toàn bộ 40 bài: `hook_line` để trống (không chép lời khi chưa xác minh câu mở đầu từ nguồn có bản quyền).
- Chỉ 1 bài có `lyric_url`: Binz — "Cho Mình Em" (LyricsTranslate, trang lời + dịch đã kiểm chứng qua kết quả tìm kiếm).
- Các bài còn lại chưa có link trang lời có bản quyền — cần tra NhacCuaTui/Zing MP3/Genius từng bài sau.

---

## Batch batch-41-50

# UNVERIFIED — Batch 41–50 (13/11/2026)

Mọi mục dưới đây là trường còn trống, chỉ có 1 nguồn, hoặc mâu thuẫn giữa các nguồn.
KHÔNG đoán — cần xác minh thêm trước khi dùng làm dữ liệu chắc chắn.

## 1. Spotify / MusicBrainz / Wikidata / ISRC / ISWC — chưa xác minh được cho CẢ 10 ca sĩ

- Spotify chưa kết nối trong phiên làm việc này (`spotify-api status` = `not_connected`), nên
  **không có spotify_id / spotify_url nào được ghi** cho cả 10 ca sĩ và 42 bài.
  Chỉ có 1 manh mối chưa đủ dùng: mô tả video YouTube của Lil Wuyn ghi
  `https://open.spotify.com/artist/3Wj34...` (bị cắt ngắn, không khôi phục được ID đầy đủ).
- **MusicBrainz ID: trống cho cả 10 ca sĩ** — tìm kiếm web không trả về trang MusicBrainz
  có MBID cho bất kỳ ai trong batch này. Cần tra trực tiếp musicbrainz.org.
- **Wikidata ID: trống cho cả 10 ca sĩ** — chưa tra.
- **ISRC / ISWC: 0/42 bài có mã** — chưa tra được từ nguồn công khai nào trong phiên này.
  Cần tra MusicBrainz / Spotify API / Apple Music khi có kết nối.
- **duration_seconds: trống cho cả 42 bài** (chỉ có "Người lạ ơi" = 288 giây theo bachhoaxanh).
- **lyric_url / apple_music_url: trống cho cả 42 bài** — chưa kiểm chứng link lời / Apple Music.

## 2. Mâu thuẫn tên thật / ngày sinh (quan trọng)

### LyLy (#50) — tên thật mâu thuẫn
- Danh sách top100 ghi: **Nguyễn Hoàng Ly**.
- Wikipedia (vi + en) ghi tên khai sinh: **Nguyễn Hoàng Lan**, sinh 1/1/1996 tại Quảng Nam – Đà Nẵng,
  kèm chú thích: "Phần lớn các nguồn đều đề cập tên gốc của nhân vật là 'Nguyễn Hoàng Ly',
  kể cả trên trang Facebook cá nhân" (nguồn: Đời sống & Pháp luật 26/9/2024).
- Trong file đã ghi `real_name = Nguyễn Hoàng Lan` + `real_name_note` ghi rõ mâu thuẫn;
  confidence của ca sĩ để `medium`. Cần LyLy hoặc nguồn chính thức xác nhận.

### Thịnh Suy (#46) — tên thật mâu thuẫn (nhẹ)
- Wikipedia + Men's Folio + Saigoneer: **Đỗ Quốc Thịnh** (sinh 18/10/1999, Bình Định).
- Revelogue ghi: **Nguyễn Quốc Thịnh** ("Thịnh Suy hay Nguyễn Quốc Thịnh sinh năm 1999").
- Đã ghi theo đa số (Đỗ Quốc Thịnh), confidence ca sĩ vẫn `high` vì 3 nguồn độc lập đồng thuận.

### Orange (#49) — năm sinh mâu thuẫn
- Wikipedia (vi + en) + Deezer: sinh **15/2/1997**.
- Thanh Niên (14/1/2018) ghi: "Cô sinh năm **1996**".
- Đã ghi 1997 theo đa số, cần xác minh thêm.

### Andree Right Hand (#42) — 1 nguồn kém tin cậy ghi sai
- Wikipedia + VOH + VTC Pay + nguoinoitieng.tv: **Bùi Thế Anh, 18/6/1987, Toronto, Canada**.
- doanhnhanonline.com.vn ghi sai: "Lê Xuân Đức, 18/4/1987, Hà Nội" và liệt kê hit của
  rapper khác ("Kẹo", "Anh là ai" không phải của Andree). Nguồn này KHÔNG được dùng.

### Vũ Cát Tường (#44) — tên khai sinh chưa xác minh
- Một nguồn (zaidap.com) cho rằng tên khai sinh là **Vũ Phượng Tường**. Chỉ 1 nguồn yếu,
  không ghi vào file. Tên thật ghi = nghệ danh (đồng thuận nhiều nguồn).

## 3. Bài hát trong danh sách top100 nhưng KIỂM CHỨNG SAI / KHÔNG PHẢI của ca sĩ đó

- **Seachains (#41): "Cảm Ơn Và Xin Lỗi" là bài của Chillies** (OST phim "Thưa Mẹ Con Đi"),
  không phải của Seachains. **"Trở Về" không tìm thấy bằng chứng là bài của Seachains.**
  Đã thay bằng: Simple Love, Slow Down, Anh 17, Chó chạy ngoài đồng.
- **Lil Wuyn (#43): "Không Sao Cả" là bài của 7dnight** (Rap Việt mùa 4, đội BigDaddy),
  không phải của Lil Wuyn. **"Lãng Du" không tìm thấy bằng chứng là bài của Lil Wuyn**
  (kết quả tìm kiếm chỉ ra bài "Lãng Du" của MCK ft. Wren Evans và các bài cùng tên khác).
  Đã thay bằng: Silence, Còn Thở Còn Gỡ, Mở Mắt (ft. Đen), Như Vậy Nhé (ft. Wxrdie).
- **Phùng Khánh Linh (#48): "Quý Cô Say Xỉn"** không tìm thấy trong các nguồn đã đọc
  (Wikipedia en/vi, nguoiquansat). Đã thay bằng: Hôm Nay Tôi Buồn, World Without You,
  Cô gái nhân ái (He Said She Said), Sweet Summer.
- **Lê Cát Trọng Lý (#47): "Khói Thuốc Cà Phê"** không tìm thấy trong các nguồn đã đọc.
  Đã thay bằng: Chênh vênh, Tám chữ có, Em đứng trên cánh đồng, Không sao về bắt đầu.

## 4. Trường bài hát chỉ có 1 nguồn / chưa xác minh

- **Nhạc sĩ (composers) để trống** (chưa xác minh, cần tra thêm): Simple Love, Slow Down,
  Anh 17, Chó chạy ngoài đồng (Seachains); Tiểu thuyết tình yêu, Ngọn nến trước gió,
  Nhạc anh, Krazy (Andree — chỉ biết người trình bày, chưa rõ tác giả);
  Có người (Vũ Cát Tường); Đôi lời tình ca (Hoàng Dũng); Chân ái, Em hát ai nghe (Orange).
- **Năm phát hành để trống**: Mở Mắt (Lil Wuyn, album "An" — chưa rõ năm phát hành album),
  Nghe em (Thịnh Suy — có MV chính thức nhưng chưa rõ năm).
- **YouTube official để trống** (biết có MV chính thức nhưng chưa xác minh được video ID):
  Người lạ ơi (chỉ tìm thấy bản "SHORT FILM" https://www.youtube.com/watch?v=POGYM9OqylA,
  chưa chắc là MV chính thức — KHÔNG ghi); Nàng thơ (Hoàng Dũng); Yêu xa, Mơ, Đông,
  Có người (Vũ Cát Tường); Yếu đuối, Chờ anh nhé, Đôi lời tình ca (Hoàng Dũng);
  Tiểu thuyết tình yêu, Ngọn nến trước gió, Nhạc anh, Krazy (Andree);
  Simple Love, Slow Down, Anh 17, Chó chạy ngoài đồng (Seachains);
  Silence, Còn Thở Còn Gỡ, Mở Mắt (Lil Wuyn); tất cả bài của Lê Cát Trọng Lý,
  Phùng Khánh Linh, Orange (trừ Người lạ ơi đã ghi chú ở trên), LyLy (trừ 24h).
- **"Người lạ ơi" — duration 288 giây** chỉ có 1 nguồn (bachhoaxanh.com), chưa đối chiếu.
- **Hook line**: chỉ xác minh được 3 bài (Một đêm say, Người lạ ơi, 24h); 39 bài còn lại để trống.
- **Album của "Khi em lớn" (Orange)**: ghi album "Cam'On" (2024) theo Wikipedia
  (bài nằm trong tracklist album), nhưng bài phát hành lần đầu 2021 dưới dạng đĩa đơn —
  cần phân biệt single gốc vs. album tổng hợp khi dùng dữ liệu.
- **Labels của Hoàng Dũng**: ghi Sony Music Entertainment + Believe Music theo các EP
  ("Tình ca mùa thu" 2018 — Sony; "Yên" 2022 — Believe); anh hoạt động chủ yếu độc lập,
  chưa có hãng đĩa dài hạn được xác nhận — cần rà lại.
- **Labels của Orange / LyLy**: ghi Superbrothers (thời kỳ 2018–2020); cả hai đã rời
  công ty tháng 2–3/2020 và hoạt động độc lập sau đó — file chưa ghi hãng hiện tại (trống).

## 5. Ảnh ca sĩ

- Chỉ có ảnh Wikimedia Commons đã xác minh qua trang Wikipedia cho 4 người:
  Vũ Cát Tường, Hoàng Dũng, Phùng Khánh Linh, Orange (đường dẫn file Commons lấy từ
  infobox Wikipedia; **license cụ thể chưa kiểm tra trên trang file** — cần kiểm tra
  trước khi dùng công khai).
- 6 người còn lại (Seachains, Andree Right Hand, Lil Wuyn, Thịnh Suy, Lê Cát Trọng Lý,
  LyLy) chưa có ảnh nào xác minh được từ Wikimedia Commons / Wikipedia / official —
  để trống, không hotlink ảnh random.

## 6. Nguồn chưa tra được trong phiên này

- VCPMC / Cục Bản quyền tác giả: chưa tra (không có kênh tra cứu công khai phù hợp
  trong phiên này) — nhạc sĩ các bài rap underground và bài của Seachains/Andree/Lil Wuyn
  là nhóm cần tra VCPMC nhất.
- Spotify Web API / Apple Music: chưa kết nối — cần làm khi có kết nối để bổ sung
  spotify_id, ISRC, duration, album chính xác.
- MusicBrainz: cần tra trực tiếp để bổ sung MBID + ISRC/ISWC cho 42 bài.

---

## Batch batch-51-60

# Batch 51–60 — Chưa xác minh / chỉ 1 nguồn / mâu thuẫn

Ngày làm: 13/11/2026. Nguyên tắc: trường nào chưa có nguồn thì để TRỐNG (null), không đoán.

## 1. Toàn batch — chưa kiểm chứng trực tiếp (áp dụng cho cả 10 ca sĩ, 40 bài)

- **spotify_id / spotify_url, musicbrainz_id, wikidata_id, image_url**: để trống cho cả 10 ca sĩ. Chưa tra trực tiếp Spotify Web API / MusicBrainz / Wikidata trong đợt này; không đoán ID. Cần batch bổ sung tra MusicBrainz API + Wikidata SPARQL + Spotify artist search.
- **ISRC / ISWC**: 0/40 bài có. Chưa tra MusicBrainz/Spotify; không đoán mã.
- **youtube_official_url / spotify_url / apple_music_url / lyric_url (từng bài)**: 0/40 bài có link đã kiểm chứng trực tiếp (chỉ biết có MV official qua Wikipedia, ví dụ Cả Một Trời Thương Nhớ — Ho Ngoc Ha's Official Channel, 25/07/2017 — nhưng chưa mở link để lấy video ID nên không ghi).
- **duration_seconds**: 0/40 bài. Cần Spotify/Apple Music metadata.
- **hook_line**: 0/40 bài. Không trích lời để tránh sai/trích quá dài; cần lấy câu mở đầu từ trang lời có bản quyền.
- **album**: chỉ ghi khi có nguồn (vd. The First Single, Love Songs 2, Vol. 1…); các bài để trống album cần đối chiếu Spotify/Apple Music.
- **VCPMC / Cục Bản quyền tác giả**: chưa tra được trong đợt này (không đăng nhập/bypass); nhạc sĩ chỉ đối chiếu qua Wikipedia / Shazam / TruongCa / báo chí.

## 2. Ca sĩ — trường trống / mâu thuẫn

- **Noo Phước Thịnh (#52)**: birth_date TRỐNG. Nguồn Báo Nghệ An chỉ ghi sinh ngày 18/12, không ghi năm; năm 1988 chưa kiểm chứng trong đợt này. Tên thật Nguyễn Phước Thịnh: nguồn Báo Nghệ An ghi lúc sinh ông nội đặt tên Nguyễn Phước Thanh, mẹ đổi thành Thịnh — tên khai sinh đầy đủ cần đối chiếu thêm. years_active 2009–nay: medium (album Three Dots 2009 theo Famous Birthdays). labels: trống.
- **Tuấn Hưng (#56)**: confidence medium (không có trang Wikipedia EN riêng trong kết quả tìm kiếm đợt này; dựa vào NguoiNoiTieng + Mytour + Viberate). Tên thật Nguyễn Tuấn Hưng: chỉ 1 nguồn (NguoiNoiTieng). years_active 1998–nay: medium (nhóm Quả Dưa Hấu 1998).
- **Quang Dũng (#57)**: confidence medium (không có trang Wikipedia EN riêng cho ca sĩ — trang Wikipedia trả về nhà thơ Quang Dũng 1921–1988, dễ nhầm). MÂU THUẪN năm sinh: Last.fm + NguoiNoiTieng ghi 08/08/1976, Quy Nhơn; Mytour ghi 08/08/1980. File này lấy 1976 theo 2 nguồn. Tên thật Thái Văn Dũng: 1 nguồn (NguoiNoiTieng).
- **Hồ Ngọc Hà (#51)**: MÂU THUẪN nơi sinh: Wikipedia EN ghi Huế; Simple Wikipedia ghi Đồng Hới, Quảng Bình; bài EverybodyWiki ghi An Cựu, Huế rồi chuyển về Quảng Bình. File này lấy Huế theo Wikipedia EN, cần đối chiếu thêm.
- **Đông Nhi (#53)**: years_active 2007–nay: medium (Vietnam Idol 2007 theo Famous Birthdays; album đầu 2009). labels: trống.
- **Hồ Quỳnh Hương (#55)**: labels: trống. years_active 2003–nay theo album Vào Đời (2003).
- **Đàm Vĩnh Hưng (#59)**: years_active 1996–nay: medium (Alchetron ghi 1996–present). labels: trống.
- **Thu Minh (#54), Bằng Kiều (#58), Lam Trường (#60)**: labels đã ghi theo Wikipedia (TM Solutions / Thúy Nga); Lam Trường labels trống.
- **Tất cả ca sĩ**: image_url trống (chưa xác minh ảnh Wikimedia Commons + license).

## 3. Bài hát — nhạc sĩ / năm chỉ 1 nguồn (confidence medium, cần nguồn thứ 2)

- **Noo Phước Thịnh (4 bài)**: nhạc sĩ Chạm Khẽ Tim Anh Một Chút Thôi (Đỗ Hiếu), Thương Em Là Điều Anh Không Thể Ngờ (Triết Phạm), Như Phút Ban Đầu (Đỗ Hiếu), Gạt Đi Nước Mắt (Nguyễn Hoàng Duy) — chỉ 1 nguồn tổng (Viberate liệt kê bài phổ biến, không ghi nhạc sĩ); năm 2014/2015/2017 chưa đối chiếu nguồn thứ 2.
- **Đông Nhi (3 bài)**: Bad Boy / Vì Ai Vì Anh / Xin Lỗi Anh Quá Phiền — nhạc sĩ Đỗ Hiếu chỉ có gợi ý gián tiếp (Wikipedia trích bài báo "hit mới của Đỗ Hiếu" cho Bad Boy); năm Vì Ai Vì Anh (2011) và Xin Lỗi Anh Quá Phiền (2015) chưa đối chiếu nguồn thứ 2.
- **Thu Minh (4 bài)**: Đường Cong / Bay / Taxi — nhạc sĩ Nguyễn Hải Phong chưa có nguồn trực tiếp ghi tên nhạc sĩ trong đợt này (chỉ có năm phát hành + album từ Wikipedia); Chuông Gió — nhạc sĩ Võ Thiện Thanh, năm 2006, chỉ 1 nguồn gián tiếp.
- **Hồ Quỳnh Hương (4 bài)**: nhạc sĩ TRỐNG cả 4 bài (Anh, Hoang Mang, Với Anh Em Vẫn Là Cô Bé, Bức Thư Tình Thứ Hai); năm Với Anh Em Vẫn Là Cô Bé và Bức Thư Tình Thứ Hai TRỐNG.
- **Tuấn Hưng**: Nắm Lấy Tay Anh (Anh Tú/Tú Dưa, 2013), Cầu Vồng Khuyết (Minh Khang, 2008), Anh Nhớ Em (Anh Tú, năm TRỐNG) — chỉ 1 nguồn (Mytour). MÂU THUẪN năm Tìm Lại Bầu Trời: danh sách top100 gợi ý 2012, Mytour ghi phát hành 2013; file này lấy 2013 theo Mytour.
- **Quang Dũng (4 bài)**: nhạc sĩ Vì Đó Là Em (Diệu Hương, 2003), Còn Ta Với Nồng Nàn (Quốc Bảo), Anh Còn Nợ Em (Anh Bằng), Biển Tình (Lam Phương) — chỉ 1 nguồn (Mytour top 10); năm của 3 bài sau TRỐNG.
- **Bằng Kiều**: Anh Sẽ Nhớ Mãi — nhạc sĩ TRỐNG (chỉ biết album cuối 2003 qua Last.fm); Để Nhớ Một Thời Ta Đã Yêu — nhạc sĩ Thái Thịnh, năm TRỐNG, chỉ 1 nguồn gián tiếp; Trái Tim Bên Lề và Nơi Tình Yêu Bắt Đầu — năm TRỐNG (chưa đối chiếu).
- **Đàm Vĩnh Hưng (4 bài)**: nhạc sĩ TRỐNG cả 4 bài (Bình Minh Sẽ Mang Em Đi, Xin Lỗi Tình Yêu, Say Tình, Tình Ơi Xin Ngủ Yên); năm Bình Minh Sẽ Mang Em Đi và Say Tình TRỐNG.
- **Lam Trường**: Katy Katy — năm TRỐNG; Mưa Phi Trường — nhạc sĩ TRỐNG, năm TRỐNG; Đôi Giày Vải — nhạc sĩ Nguyễn Hải Phong chỉ 1 nguồn (Vietnam.vn).
- **Đông Nhi — Trốn Tìm (s53-04)**: confidence LOW — nhạc sĩ TRỐNG, năm TRỐNG; chỉ biết tên bài trong danh sách top100 + Wikipedia.
- **Hồ Ngọc Hà — Hãy Thứ Tha Cho Em (s51-02)**: nhạc sĩ Dương Khắc Linh + lời Hoàng Huy Long chỉ 1 nguồn (EverybodyWiki trích Wikipedia); cần đối chiếu nguồn thứ 2.

## 4. Edge cần lưu ý

- Edge ca sĩ–ca sĩ Hồ Ngọc Hà–Suboi: Suboi không thuộc Top 100 batch này (nằm ở #33, batch khác) — edge vẫn ghi vì có bằng chứng feat trong Xin Hãy Thứ Tha.
- Edge Bằng Kiều–Lam Anh (duet Nơi Tình Yêu Bắt Đầu): Lam Anh ngoài Top 100.
- Các edge same_composer của Noo/Đông Nhi/Thu Minh/Tuấn Hưng mang confidence medium theo nhạc sĩ (xem mục 3).

---

## Batch batch-61-70

# Batch 61–70 — Danh sách chưa xác minh (UNVERIFIED)

Ngày làm: 13/11/2026. Nguồn chính: Wikipedia (vi/en), iTunes/Apple Music Search API, MusicBrainz API, Wikidata API, mô tả MV official trên YouTube, báo VnExpress/Kenh14/VTV/VOH.

## 1. Lỗi trong danh sách top100 đã phát hiện (cần coordinator xác nhận, KHÔNG tự sửa danh sách)

| # | Vấn đề | Bằng chứng |
|---|--------|-----------|
| 63 Trung Quân | Danh sách ghi tên thật **Nguyễn Trần Trung Quân**. Đây là **một ca sĩ khác** (sinh 16/11/1992, Hà Nội). Người của batch này là **Bùi Nguyễn Trung Quân — Trung Quân Idol** (sinh 20/1/1989, Đà Lạt); các bài Trót Yêu / Dấu Mưa / Chưa Bao Giờ đều của Bùi Nguyễn Trung Quân. | Wikipedia (vi): trang "Trung Quân" = Bùi Nguyễn Trung Quân; trang "Nguyễn Trần Trung Quân" là người khác (1992, Hà Nội). |
| 70 Hiền Hồ | Danh sách ghi tên thật **Võ Thị Hiền Hồ**. Wikipedia (vi) và nhiều báo ghi **Hồ Thị Hiền**. | https://vi.wikipedia.org/wiki/Hi%E1%BB%81n_H%E1%BB%93 |
| 61 Uyên Linh | Năm sinh mâu thuẫn: Wikipedia (vi/en) ghi **1987** (theo chính ca sĩ xác nhận tuổi mèo); nhiều báo năm 2010 ghi **1988**. File ghi 1987-12-31. | Wikipedia (vi) Uyên Linh, ghi chú [1]. |
| 67 Myra Trần | Không có bài Wikipedia (vi/en), không có Wikidata QID. Tên thật Trần Minh Như + sinh 3/6/1999 chỉ có Fandom Thúy Nga (ngày sinh) + báo Eva/Vietnamnet (tên thật) — confidence medium. | Fandom Thúy Nga, eva.vn, vietnamnet.vn |

## 2. Trường còn trống cho mọi ca sĩ

- **spotify_id / spotify_url: trống 10/10.** Không có quyền truy cập Spotify Web API có token trong batch này; tìm qua web search không trả về artist ID đáng tin. Cần batch bổ sung có token Spotify.
- **image_url: trống 10/10.** Chưa kiểm chứng ảnh nào trên Wikimedia Commons; không hotlink ảnh random. Cần tra Commons riêng.
- **labels: trống** với Trung Quân, Bùi Anh Tuấn, Lâm Bảo Ngọc, Dương Hoàng Yến, Juky San, Myra Trần, Hiền Hồ (không có hãng đĩa ổn định được nguồn xác nhận).
- **musicbrainz_id: trống** với Dương Hoàng Yến và Myra Trần — API MusicBrainz trả **503** lúc tra cứu, đã dừng theo quy tắc (không retry dồn dập).
- **wikidata_id: trống** với Myra Trần (không có bài Wikipedia vi).

## 3. Bài hát — ISRC / ISWC / Spotify / YouTube

- **ISRC: 0/35 bài (0%).** iTunes Search API (VN) không trả trường ISRC; MusicBrainz có bản ghi cho Dấu Mưa, Chưa Bao Giờ, Phải Chăng Em Đã Yêu nhưng **không gắn ISRC nào**; 2 query MusicBrainz trả 503. Đã lưu `musicbrainz_recording_id` cho 3 bài trên để tra tiếp.
- **ISWC: 0/35.** Chưa tra được nguồn nào.
- **spotify_url: 0/35.** Chưa có token Spotify.
- **YouTube official: 8/35 (22,9%).** Chỉ ghi link khi kết quả search trả về đúng MV/Lyrics video official (xem songs.json). Các bài còn lại chưa xác minh được video ID official — không đoán ID.
- **apple_music_url: 27/35 (77,1%).** Lấy từ iTunes Search API; một số link là bản tái phát hành (ghi chú trong từng bài).
- **duration_seconds: trống** với Cảm Ơn Tình Yêu, Chia Cách Bình Yên, Vì Yêu Là Nhớ, Xe Anh Đến Đâu Em Theo Đến Đó, Thiên Hạ Hữu Tình Nhân (không có bản Apple Music gốc khớp để lấy thời lượng).
- **lyric_url: chỉ 2/35** (Tình Yêu Đến Sau — HoaTieu; Rồi Người Thương Cũng Hóa Người Dưng — Lyricvn). Các bài khác chưa có link trang lời đã kiểm chứng.

## 4. Nhạc sĩ chưa xác minh / chỉ 1 nguồn (confidence medium)

| Bài — Ca sĩ | Vấn đề |
|---|---|
| Xe Anh Đến Đâu Em Theo Đến Đó — Dương Hoàng Yến | Nhạc sĩ **trống** (chưa xác minh; không đoán là Đạt G dù Đạt G feat). Năm 2021 theo hosongoisao (1 nguồn). |
| Thiên Hạ Hữu Tình Nhân — Juky San | Nhạc sĩ gốc (Trung Quốc) + người viết lời Việt **trống**. Đây là bản cover nhạc Hoa lời Việt 2020. |
| Buông — Lâm Bảo Ngọc | Nhạc sĩ Nguyễn Duy Anh (VnExpress, 1 nguồn). Thời lượng 339s lấy từ album Hoa Nắng Tôi (2025), có thể khác bản 2023. |
| Nói Không Thành Lời — Lâm Bảo Ngọc | Nhạc sĩ Nguyễn Hải Minh (VnExpress, 1 nguồn). |
| Rồi Cũng Sẽ Qua — Myra Trần | Nhạc sĩ/lời Huỳnh Quốc Huy (Gaana, 1 nguồn). |
| Tình Cũ Bao Giờ Cũng Tốt Hơn? — Dương Hoàng Yến | Năm mâu thuẫn: Kenh14 11/2019 nói mới tung MV; iTunes ghi 2020-01-01 (ngày placeholder). Ghi 2019. |
| Em Ngày Xưa Khác Rồi — Hiền Hồ | Năm mâu thuẫn: iTunes 1/12/2017; mục đĩa đơn Wikipedia Hiền Hồ ghi 2018. Ghi 2017. |
| Chia Cách Bình Yên — Quốc Thiên | Năm mâu thuẫn: album Khi Anh Lặng Im 2013 có bài này (Gaana 2013); bảng MV Wikipedia ghi ngày MV 10/11/2016. Ghi 2013 theo album. |
| Cảm Ơn Tình Yêu — Uyên Linh | Năm: hát chung kết 25/12/2010, đĩa đơn đầu tay đầu 2011. Ghi 2011. Không có link Apple/Spotify khớp; link YouTube là bản liveshow, không phải MV official. |
| Lỡ Yêu Mất Rồi — Han Sara | Thời lượng 239s từ iTunes nhưng link Apple chưa lưu được → để trống. |
| Giữa Đại Lộ Đông Tây — Uyên Linh | Thời lượng 227s là bản studio; link Apple chỉ lưu được bản live nên để trống. |
| Vì Yêu Là Nhớ — Han Sara | Không dùng duration/link Apple của bản The Heroes 2021 (feat T.R.I) làm bản gốc 2018. |
| Đại Lộ Tan Vỡ — Uyên Linh | Album Portrait 2017 nhưng đĩa đơn phát hành 10/7/2018 — ghi năm 2018. |
| Phố Không Mùa — Bùi Anh Tuấn | Thời lượng 394s + link Apple từ bản single tái phát hành 2019 (bản gốc 2013). |
| Nơi Tình Yêu Bắt Đầu — Bùi Anh Tuấn | Thời lượng 276s từ Album Collection 1: Xin Em (2016); bản Giọng hát Việt 2012 trên iTunes chỉ 137s (bản TV cắt ngắn). |

## 5. Lưu ý dễ nhầm đã xử lý

- "Chưa Bao Giờ" (Trung Quân) là sáng tác của **Tiên Tiên**, KHÔNG phải Tiên Cookie — đã xác minh bằng Wikipedia Tiên Tiên + Kenh14.
- "Cầu Vồng Khuyết" **không phải** bài của Dương Hoàng Yến (bài này của Cara, nhạc sĩ Minh Khang) — không đưa vào danh sách bài của cô.
- "Cưới Nhau Đi" (Hiền Hồ) không tìm thấy bản Apple Music khớp nên **không đưa vào**; Hiền Hồ giữ 3 bài.
- "Vùng Ký Ức" (Lâm Bảo Ngọc) không tìm thấy bản Apple Music solo khớp nên thay bằng "Nói Không Thành Lời" (2023, đã kiểm chứng).
- Myra Trần có bản song ca "Tình Yêu Đến Sau" với Đức Phúc (2023) — bản chính dùng trong file là bản solo 2022.

## 6. Cần làm tiếp (ngoài phạm vi batch)

1. Lấy Spotify artist ID + track URL cho 10 ca sĩ / 35 bài (cần token Spotify).
2. Tra ISRC/ISWC qua MusicBrainz (thử lại khi API hết 503) hoặc qua Spotify API (trả ISRC).
3. Lấy MusicBrainz ID cho Dương Hoàng Yến, Myra Trần (thử lại sau 503).
4. Kiểm chứng ảnh trên Wikimedia Commons cho 10 ca sĩ.
5. Xác minh nhạc sĩ: Xe Anh Đến Đâu Em Theo Đến Đó; Thiên Hạ Hữu Tình Nhân (nhạc gốc + lời Việt); Buông; Nói Không Thành Lời; Rồi Cũng Sẽ Qua.
6. Coordinator xác nhận 2 lỗi danh sách: tên thật Trung Quân (Nguyễn Trần → Bùi Nguyễn) và Hiền Hồ (Võ Thị Hiền Hồ → Hồ Thị Hiền).

---

## Batch batch-71-80

# UNVERIFIED — Batch 71–80 (Hồng Nhung → Đan Trường)

Ngày kiểm chứng: 13/11/2026. Mọi mục dưới đây là trường còn trống, chỉ 1 nguồn, hoặc mâu thuẫn giữa các nguồn — KHÔNG đoán, để trống trong JSON.

## 1. Ca sĩ — trường còn trống / chưa đủ nguồn

| # | Ca sĩ | Vấn đề |
|---|-------|--------|
| 71 | Hồng Nhung | `labels[]` trống — chưa xác minh hãng đĩa chính từ nguồn đã tra. `years_active` 1985 lấy từ Wikidata P2031 (1 nguồn). |
| 72 | Thu Phương | `spotify_id` chưa có (Wikidata không có P1902; chưa tra Spotify API có xác thực). `years_active` "1988–nay" chỉ suy từ Wikipedia (ban nhạc Tây Hồ cuối thập niên 1980) — medium. `labels` chỉ có Thúy Nga (album 2004). |
| 73 | Tuấn Ngọc | **MÂU THUẪN TÊN THẬT**: file top100-list.md ghi "Lữ Anh Tuấn", Wikipedia tiếng Việt ghi "Lã Anh Tuấn". JSON dùng "Lã Anh Tuấn" theo Wikipedia; cần John/coordinator chốt. `labels[]` trống. `years_active` "1964–nay" suy từ "17 tuổi bắt đầu biểu diễn chuyên nghiệp" (sinh 1947) — medium. `spotify_id` chưa có. |
| 74 | Khánh Ly | `labels` chỉ có Sơn Ca (album Sơn Ca 7, 1974, iTunes); Thúy Nga chưa đối chiếu. |
| 75 | Ý Lan | `image_url` trống — Wikidata Q10840001 không có ảnh P18. `birth_date` chỉ có năm 1958 (Wikidata precision 9; Wikipedia cũng chỉ ghi năm). `spotify_id` chưa có. |
| 76 | Elvis Phương | `image_url` trống — Wikidata không có ảnh P18. `birth_date` 1945-02-01 chỉ từ Wikipedia (Wikidata chỉ ghi năm 1945) — medium. `spotify_id` chưa có. |
| 77 | Thanh Hà | `wikidata_id` trống — **không tìm thấy thực thể Wikidata** cho ca sĩ Thanh Hà (Trương Minh Hà) qua wbsearchentities (vi/en). `image_url` trống. `spotify_id` chưa có. `years_active` "1990s–nay" ước lượng — medium. Confidence ca sĩ = medium. |
| 78 | Phương Thanh | `labels[]` trống. `spotify_id` chưa có. |
| 79 | Cẩm Ly | `spotify_id` chưa có (Wikidata có AllMusic ID mn0000573284 nhưng không có Spotify ID). |
| 80 | Đan Trường | `spotify_id` chưa có (Wikidata có AllMusic ID mn0002109459 nhưng không có Spotify ID). |

- Spotify artist ID: chỉ 2/10 xác minh được qua Wikidata (Hồng Nhung `5MibVKlWvof8lLAkOaaDmi`, Khánh Ly `2BT5812uC3XW9TukhlOfD0`). 8 ca sĩ còn lại KHÔNG đoán ID — cần Spotify API có xác thực hoặc tra tay trên open.spotify.com.
- Ảnh: chỉ 7/10 có ảnh Wikimedia Commons kèm giấy phép đã kiểm chứng qua Commons API (CC BY 3.0, riêng Tuấn Ngọc CC BY-SA 4.0). Ý Lan, Elvis Phương, Thanh Hà để trống.

## 2. Bài hát — ISRC / ISWC: 0/40

- Đã tra MusicBrainz recording search cho cả 40 bài (30 bài có bản ghi khớp, 10 bài không khớp/không có): **không bài nào có ISRC trong MusicBrainz**. ISRC và ISWC để trống toàn bộ — cần tra từ Spotify/Apple Music API có xác thực hoặc cơ sở dữ liệu ISRC, không đoán mã.
- 10 bài không có bản ghi MusicBrainz khớp: Nhớ về Hà Nội, Có phải em mùa thu Hà Nội (bản Hồng Nhung), Đoản khúc thu Hà Nội, Chưa bao giờ, Lệ đá, Trăm nhớ ngàn thương, Vết thù trên lưng ngựa hoang, Yêu em dài lâu, Sợ yêu, Mong manh tình về.

## 3. Bài hát — nhạc sĩ / lời chưa xác minh hoặc chỉ 1 nguồn

| Bài hát | Ca sĩ | Vấn đề |
|---|---|---|
| Tàn tro | Thanh Hà | Nhạc sĩ TRỐNG — không tìm thấy nguồn đáng tin ghi tác giả (đã tìm, chỉ thấy bản thu Spotify/iTunes). Đừng ghi Trần Trung Đức khi chưa có nguồn. |
| Trống vắng | Phương Thanh | Nhạc sĩ TRỐNG — báo Thanh Niên (2021) chỉ ghi nhạc sĩ Nguyễn Hà biên tập/hòa âm album, không phải tác giả bài hát. |
| Tình khúc vàng | Đan Trường | Nhạc sĩ TRỐNG — chỉ có metadata iTunes (album Trương Chi Mỵ Nương, 2003), chưa tìm thấy nguồn ghi tác giả. |
| Giọt sương trên mí mắt | Hồng Nhung | Nhạc sĩ Thanh Tùng — medium, chỉ 1 nguồn gián tiếp (Wikipedia liệt kê Thanh Tùng trong các nhạc sĩ gắn với Hồng Nhung + iTunes khớp bài). |
| Có phải em mùa thu Hà Nội | Hồng Nhung, Thu Phương | Nhạc sĩ Trần Quang Lộc — medium, 1 nguồn gián tiếp mỗi bản (Wikipedia ca sĩ + iTunes). Năm 1996/1997 là năm album iTunes, chưa chắc là năm thu âm gốc. |
| Đoản khúc thu Hà Nội | Hồng Nhung | Nhạc sĩ Trịnh Công Sơn — medium, gián tiếp (album đầu tay 1997). |
| Chưa bao giờ | Thu Phương | Nhạc sĩ Việt Anh — medium, gián tiếp. Năm phát hành trống. |
| Đêm nằm mơ phố | Thu Phương | Nhạc sĩ Việt Anh — medium, gián tiếp (album 2004 đã xác minh). |
| Dòng sông lơ đãng | Thu Phương | Nhạc sĩ Việt Anh — medium, gián tiếp. Năm trống. |
| Chiều một mình qua phố | Tuấn Ngọc | Nhạc sĩ Trịnh Công Sơn — medium, gián tiếp. Năm 1991 là năm album iTunes. |
| Lệ đá | Tuấn Ngọc | Nhạc sĩ Trần Trịnh, lời Hà Huyền Chi — medium, chưa đối chiếu nguồn thứ 2. Năm + album trống. |
| Mắt lệ cho người | Tuấn Ngọc | Nhạc sĩ Từ Công Phụng — medium, gián tiếp. Năm trống. |
| Tình ca | Ý Lan | Nhạc sĩ Phạm Duy — medium; hit iTunes khớp mơ hồ ("Tình" thay vì "Tình ca"), album "Hỡi Người Tình" 1990 chưa chắc đúng bản. |
| Vết thù trên lưng ngựa hoang | Elvis Phương | Nhạc Phạm Duy, lời Ngọc Chánh — medium, gián tiếp (Wikipedia chỉ xác nhận là ca khúc tiêu biểu của băng Shotguns). |
| Đàn bà | Elvis Phương | Nhạc sĩ Song Ngọc — medium, gián tiếp. |
| Yêu em dài lâu | Elvis Phương | Nhạc sĩ Đức Huy — medium, gián tiếp. |
| Áo anh sứt chỉ đường tà | Elvis Phương | Nhạc sĩ Phạm Duy — medium, gián tiếp. Năm + album trống. |
| Giã từ dĩ vãng | Phương Thanh | Nhạc sĩ Nguyễn Đức Trung — medium, chỉ 1 nguồn yếu (mô tả video YouTube AI cover). Cần nguồn thứ 2 (bìa album/phim hoặc VCPMC). |
| Kiếp ve sầu | Đan Trường | Lời Việt: Nguyễn Ngọc Thiện — high (2 báo). Tác giả nhạc gốc (nhạc Hoa) CHƯA xác minh — ghi trong notes. |
| Mưa trên cuộc tình | Đan Trường | Lê Quang viết lời Việt — medium (Wikipedia Lê Quang). Tác giả nhạc gốc (nhạc Hoa) CHƯA xác minh. |
| Một thời đã xa | Phương Thanh | Năm phát hành trống (Đàm Vĩnh Hưng thu bản của mình khoảng 1996–97, không phải bản Phương Thanh). |

## 4. Bài hát — năm / album / duration / link còn thiếu

- Năm phát hành trống ở 16/40 bài (chủ yếu là các ca khúc sáng tác trước thời streaming; năm album iTunes có nhiều mốc 1905-06-19 là placeholder rác — ĐÃ LOẠI, không dùng).
- Album trống ở 9 bài: Giọt sương trên mí mắt, Chưa bao giờ, Dòng sông lơ đãng, Lệ đá, Còn tuổi nào cho em, Áo anh sứt chỉ đường tà, Một thời đã xa, Giã từ dĩ vãng, Bờ bến lạ, Người về cuối phố.
- Duration trống ở 5 bài (hit iTunes đầu tiên sai bài/sai ca sĩ nên không dùng): Lệ đá, Còn tuổi nào cho em, Sợ bắt đầu sợ kết thúc, Bờ bến lạ, Người về cuối phố.
- Apple Music URL: 35/40. Thiếu 5 bài như trên (iTunes trả về bài khác/ca sĩ khác: "Còn tuổi nào cho em" trả về Mộc San; "Người về cuối phố" trả về Minh Tuyết; "Bờ bến lạ" trả về Em Xinh Say Hi 2025).
- YouTube official: chỉ 2/40 có link đã kiểm chứng trực tiếp qua mô tả kênh official — "Người về cuối phố" (Cẩm Ly Official) và "Sợ bắt đầu sợ kết thúc" (Thanh Hà Official). Các bài còn lại: MV/audio trên YouTube tồn tại nhưng chưa xác minh được kênh official, KHÔNG ghi link đoán.
- Spotify track URL: chỉ 1/40 — "Tàn tro" (open.spotify.com/track/1xnQpl6Fu5qSGtyYAwBRAS, thấy trong kết quả tìm kiếm).
- Lyric URL: chỉ 3/40 (Shazam): Chim trắng mồ côi, Em còn nhớ hay em đã quên, Tàn tro. Không chép lời trong JSON; hook_line tối đa 1 câu mở đầu, 17/40 bài có hook_line, 23 bài để trống vì chưa chắc câu mở đầu.
- "Mong manh tình về": bản gốc do Quốc Thiên thể hiện đầu tiên (Đức Trí nhạc, Trương Hồ Phương Nga lời); Thanh Hà là bản cover nổi tiếng — đã ghi trong notes.

## 5. Edge — lưu ý

- Edge song-song "cùng nhạc sĩ Trịnh Công Sơn" dùng dạng hub (mọi bài nối về "Diễm xưa") để tránh bùng nổ tổ hợp; không phải tất cả các cặp đều có edge trực tiếp.
- Edge "Có phải em mùa thu Hà Nội" xuất hiện 2 lần (2 ca sĩ) — cố ý, nối bằng edge same_song_different_singer.
- Không tạo edge ca sĩ–ca sĩ ngoài batch (VD: Ý Lan–Vũ Khanh chỉ xuất hiện trong bài "Trăm nhớ ngàn thương"; Vũ Khanh không thuộc Top 100 batch này nên không tạo node).

---

## Batch batch-81-90

# Batch 81–90 — Danh sách chưa xác minh (UNVERIFIED)

> Ngày làm: 13/11/2026. Spotify API **không kết nối** (`spotify-api status` = `not_connected`, không có config) nên toàn bộ Spotify ID/URL và ISRC đều chưa lấy được. MusicBrainz/Wikidata cũng chưa tra được trực tiếp (xem mục 1). Mọi trường để trống dưới đây là **chưa xác minh, không phải không tồn tại**.

## 1. Toàn batch — thiếu định danh chuẩn (cả 10 ca sĩ, 36 bài)

- `spotify_id` / `spotify_url` (ca sĩ): **trống cả 10**. Cần chạy lại bằng Spotify Web API khi đã kết nối (kiểm tra trùng/tách đôi artist).
- `musicbrainz_id` (ca sĩ): **trống cả 10**. MusicBrainz search không trả kết quả qua web search; cần tra trực tiếp musicbrainz.org.
- `wikidata_id` (ca sĩ): **trống cả 10**. Các trang Wikipedia đều có mục Wikidata nhưng đợt này chưa trích được QID — cần mở Wikidata hoặc dùng API Wikipedia.
- `image_url`: **trống cả 10**. Ảnh infobox Wikipedia/Wikimedia Commons tồn tại nhưng chưa trích được URL file + license; không hotlink ảnh random. Cần lấy từ Commons kèm giấy phép.
- `isrc` / `iswc`: **trống cả 36 bài (0%)**. Nhạc bolero/trữ tình trước 1975 phần lớn không có ISRC công khai dễ tra; cần MusicBrainz recordings hoặc metadata Spotify/Apple Music.
- `spotify_url` (bài), `apple_music_url` (bài): **trống cả 36 bài**. Chưa kiểm chứng qua API/store.
- `lyric_url`: **trống cả 36 bài**. Chỉ có các trang lời tổng hợp (lyricvn, thuthuat.taimienphi.vn, loibaihat.me) chưa rõ bản quyền nên không ghi — cần nguồn lời được cấp phép (ví dụ Musixmatch/Apple Music) mới ghi.
- `duration_seconds`: chỉ có 5/36 bài (Giấc Mơ Có Thật 260s; Tình Lỡ 353s; Chuyện Hoa Sim 318s; Hoa Sứ Nhà Nàng bản Trường Vũ 249s; Nỗi Buồn Hoa Phượng bản 1984 349s). Còn lại trống.
- `year`: trống 19/36 bài (xem mục 4).

## 2. Mâu thuẫn giữa các nguồn (đã chọn 1 phương án, ghi rõ trong file JSON)

### Ca sĩ
- **Chế Linh (#90) — SAI TÊN THẬT TRONG DANH SÁCH GỐC**: top100-list.md ghi "Lưu Văn Linh". Đúng là **Lưu Văn Liên** (Wikipedia VI/EN + trang official chelinh.com). Đã sửa trong singers.json; cần sửa lại top100-list.md.
- **Quang Lê (#83) — năm sinh**: 1979 (Wikipedia hiện tại + chính Quang Lê trả lời Dân trí 2018: hộ chiếu ghi 1979, trước đây anh nói 1981 cho trẻ) vs 1980 (Fandom Thúy Nga) vs 1981 (nhiều nguồn cũ, nguoinoitieng.tv). Dùng 1979-01-24.
- **Phi Nhung (#84) — năm sinh**: 1970 (Wikipedia VI/EN hiện tại, VnExpress 2024) vs 1972 (bản tin TTXVN lúc mất, Alchetron, VietCeleb). Dùng 1970-04-10. Ngày mất 28/9/2021 do COVID-19 thì thống nhất.
- **Mạnh Quỳnh (#85) — năm sinh + nơi sinh**: 22/4/1971, Sài Gòn (Wikipedia) vs 1972 (Thanh Niên 2016 chú thích ảnh; loibaihat.me) và nơi sinh Biên Hòa, Đồng Nai (tieusu.com; nhacxua.vn). Dùng 1971-04-22, Sài Gòn. `years_active` = "1996–nay" chỉ suy từ liveshow 20 năm (2016) — cần xác minh.
- **Thanh Tuyền (#89) — năm sinh**: 29/10/1948 (Wikipedia VI hiện tại) vs 1947 (nhaxinhplaza: sinh 1947, giấy tờ 1948) vs 1949 (hopamviet, Last.fm, nguoinoitieng.tv). Dùng 1948-10-29. Tên thật Phạm Như Mai thống nhất (Last.fm ghi "Nguyen Nhu Mai" là sai họ).
- **Hương Lan (#88) — tên thật**: "Trần Thị Ngọc Ánh" (Wikipedia) vs "Trần Ngọc Ánh" (top100-list.md, thiếu chữ "Thị"). Dùng Trần Thị Ngọc Ánh.
- **Trường Vũ (#87) — nguồn sai**: izumi.edu.vn ghi "Phan Thanh Sơn, sinh 20/9/1971 tại Quảng Trị" — SAI hoàn toàn so với Wikipedia + nhiều nguồn (Huỳnh Văn Ngoảnh, 25/2/1963, Vĩnh Châu, Bạc Liêu). Không dùng nguồn này cho Trường Vũ.
- **Đan Nguyên (#86)**: không có trang Wikipedia; tên thật Nguyễn Đặng Đan + sinh 9/7/1984 chỉ có từ mô tả video official và Izumi — confidence medium, cần đối chiếu thêm.
- **Hương Lan (#88) — labels**: để trống (bà thu âm cho nhiều trung tâm, chưa xác minh hãng chính thức).
- **Mạnh Quỳnh (#85) — labels**: chỉ ghi ["Thúy Nga"] (medium); thời kỳ đầu còn Người Đẹp Bình Dương, Asia — chưa xác minh đầy đủ.

### Bài hát
- **Đập Vỡ Cây Đàn**: ghi công mâu thuẫn — Hoa Linh Bảo (Thúy Nga PBN 82; Đan Nguyên Official; Gaana) vs Tùng Vân – Tuyết Sơn (bản Làng Văn của Duy Khánh). Giữ Hoa Linh Bảo (bút danh Lê Mộng Bảo), confidence medium.
- **Căn Nhà Màu Tím**: Wikipedia Hoài Linh ghi một mình Hoài Linh (1969); Dân Việt (bài Phi Nhung) ghi "Hoài Linh, Loan Thảo". Giữ Hoài Linh.
- **Xin Làm Người Xa Lạ**: Wikipedia VI đánh dấu * (bút hiệu Lưu Trần Lê) nhưng Wikipedia EN, Làng Văn, nhiều nguồn ghi Tú Nhi. Cả hai đều là bút danh của Chế Linh nên không ảnh hưởng tác giả; giữ Tú Nhi.
- **Mai Lỡ Mình Xa Nhau**: top100 gốc ghi Lưu Trần Lê; nhiều nguồn (Phụ Nữ Today, Nông nghiệp & Môi trường) ghi Tú Nhi. Cùng tác giả Chế Linh; giữ Lưu Trần Lê theo top100, confidence medium.
- **Đoạn Cuối Tình Yêu**: năm sáng tác 1970 (Ký Ức Miền Nam) vs Shazam ghi phát hành 1/1/1974 (album Băng Nhạc Chế Linh 1). Giữ year=1970, ghi chú 1974.
- **Thành Phố Buồn**: năm 1970 (Wikipedia) vs một video MP Melody ghi 1973. Giữ 1970.
- **Giấc Mơ Có Thật (album)**: ngày phát hành 24/10/2004 (trang album Wikipedia) vs 27/8/2004 (trang danh sách đĩa nhạc Wikipedia). Chưa phân xử.
- **Chuyện Hoa Sim**: năm sáng tác 1994 (danh sách bài Anh Bằng) vs phát hành 1995 (trang bài hát). Giữ year=1995, ghi chú 1994.
- **Vợ Tôi**: tác giả Mạnh Quỳnh — cần phân biệt ca sĩ Nguyễn Thanh Dũng (tự sáng tác) với nhạc sĩ Mạnh Quỳnh trước 1975; mới có 1 nguồn trực tiếp.
- **Đám Cưới Nghèo (Trường Vũ)**: ĐÃ LOẠI khỏi danh sách vì ghi công mâu thuẫn không phân xử được (Gaana: Giao Linh; truongca: Thu Anh; Gaana khác: Anh Thy). Thay bằng Hoa Sứ Nhà Nàng (đã xác minh).

## 3. Bài hát chỉ có 1 nguồn cho nhạc sĩ (confidence = medium)

- Ai Khổ Vì Ai (Thương Linh) — chỉ tracklist Wikipedia Khúc Tình Xưa 2.
- Bông Điên Điển (Hà Phương) — chỉ Dân Việt. Lưu ý: đã đính chính không phải Trịnh Công Sơn.
- Chiều Lên Bản Thượng (Lê Dinh) — chỉ Dân Việt.
- Vợ Tôi (Mạnh Quỳnh) — chỉ mô tả video + liệt kê trong tiểu sử.
- Sương Trắng Miền Quê Ngoại (Đinh Miên Vũ) — nguồn thứ 2 (Alchetron) chỉ là bản sao Wikipedia.
- Đêm Nghe Bài Vọng Cổ (Bắc Sơn, 1999) — chỉ Nhạc Xưa.
- Đà Lạt Hoàng Hôn (Minh Kỳ, Dạ Cầm) — chỉ tracklist Wikipedia Dạ khúc cho tình nhân 2.
- Mai Lỡ Mình Xa Nhau (Lưu Trần Lê) — mâu thuẫn bút danh (xem mục 2).
- Đập Vỡ Cây Đàn (Hoa Linh Bảo) — mâu thuẫn ghi công (xem mục 2).

## 4. Trường còn trống theo bài (year/album/duration)

- `year` trống (19 bài): Ai Khổ Vì Ai, Chuyện Tình Hoa Trắng, Đập Vỡ Cây Đàn, Sầu Tím Thiệp Hồng, Sương Trắng Miền Quê Ngoại, Bông Điên Điển, Chiều Lên Bản Thượng, Áo Mới Cà Mau, Phải Lòng Con Gái Bến Tre, Vợ Tôi, Tình Đẹp Như Mơ, Gõ Cửa, Phút Cuối, Không Giờ Rồi, Em Đi Trên Cỏ Non, Sa Mưa Giông, Chuyến Tàu Hoàng Hôn, Đà Lạt Hoàng Hôn, Mai Lỡ Mình Xa Nhau.
- `album` trống với hầu hết bài hải ngoại trước 1975 (chỉ ghi PBN/Asia/Music Box khi có bằng chứng cụ thể).
- `youtube_official_url` chỉ có 4/36 bài đã xác minh trực tiếp từ mô tả video có ghi © Thúy Nga / © Làng Văn: Đập Vỡ Cây Đàn (Thúy Nga PBN 82), Về Đâu Mái Tóc Người Thương (Thúy Nga PBN 84), Phải Lòng Con Gái Bến Tre (Thúy Nga Music Box #30), Xin Làm Người Xa Lạ (Làng Văn). Các MV official khác (ví dụ Duyên Phận trên kênh Thúy Nga, đăng 16/4/2016, >100 triệu view) đã xác nhận là **có tồn tại** nhưng chưa lấy được video ID nên chưa ghi link — cần bổ sung bằng cách mở kênh Thúy Nga.
- `hook_line` trống với 19/36 bài (chỉ ghi khi thấy đúng câu mở đầu trong nguồn đã kiểm chứng; riêng Còn Thương Rau Đắng Mọc Sau Hè cố tình bỏ trống vì tranh cãi lời "coi cỏi" vs "coi khói đốt đồng").

## 5. Việc cần làm tiếp (cho coordinator/batch sau)

1. Kết nối Spotify rồi chạy lại để lấy `spotify_id` ca sĩ + track, ISRC, duration, album — ưu tiên 10 ca sĩ này.
2. Tra MusicBrainz (artist + recording) để lấy MBID + ISRC/ISWC; tra Wikidata lấy QID + ảnh Commons có license.
3. Sửa top100-list.md: Chế Linh tên thật Lưu Văn **Liên** (không phải Linh); Hương Lan tên thật Trần **Thị** Ngọc Ánh.
4. Bổ sung nguồn thứ 2 cho 9 bài confidence medium (mục 3), đặc biệt Bông Điên Điển (Hà Phương) và Đập Vỡ Cây Đàn.
5. Bổ sung video ID YouTube official cho Duyên Phận (kênh Thúy Nga) và các bài còn lại.
6. Xác minh `years_active` của Mạnh Quỳnh (1996–nay, hiện suy luận) và Đan Nguyên (2007–nay).

---

## Batch batch-91-100

# UNVERIFIED — Batch 91–100 (13/11/2026)

Mọi trường để trống / chỉ 1 nguồn / mâu thuẫn giữa các nguồn. Không đoán, không điền bừa.

## 1. Toàn batch — Spotify / MusicBrainz / ISRC / ISWC / ảnh

- **Spotify artist ID + URL: 0/10 ca sĩ xác minh được.** Tìm kiếm `site:open.spotify.com` không trả kết quả; không có credential Spotify API trong batch này. Cần tra lại bằng Spotify Web API / app Spotify.
- **MusicBrainz ID: 0/10.** API MusicBrainz trả lỗi "web server is currently busy" trong lúc crawl (2 lần thử). Chưa thử lại được.
- **ISRC / ISWC: 0/36 bài.** Không tra được từ nguồn công khai trong batch này (MusicBrainz lỗi, không có quyền VCPMC). Cần tra lại bằng MusicBrainz / Apple Music API.
- **YouTube official: chỉ 3/36 bài có link đã kiểm chứng** (xem songs.json): "Bên nhau thật khó" (kênh Châu Khải Phong), "Tài sản của bố" (kênh King of Rap), "Vợ người ta" (link do Wikipedia ghi là đăng trên YouTube của Zing MP3 — chưa mở trực tiếp để đối chiếu). Các bài còn lại chưa tra link MV official.
- **Apple Music: chỉ 3 bài** có link album PAK 1 (Ngựa ô thương nhớ, Lý quạ kêu, Thời gian tôi). Còn lại chưa tra.
- **Ảnh đại diện (image_url): 0/10.** Chưa xác minh được ảnh Wikimedia Commons nào cho 10 ca sĩ này. Không hotlink ảnh random.
- **hook_line: 0/36 bài.** Không chép lời khi chưa đối chiếu được nguồn lời có bản quyền; cần tra lyric site có bản quyền sau.
- **duration_seconds: chỉ 6/36 bài** (Ôi quê tôi 367s, Con cò 389s, Ngựa ô thương nhớ 219s, Lý quạ kêu 234s, Ngắm hoa lệ rơi 308s, Bên nhau thật khó 262s). Còn lại chưa có nguồn thời lượng đáng tin.
- **labels: trống với Hồ Văn Cường, Ngọc Sơn, Siu Black, Phan Mạnh Quỳnh, Đạt G.** Chưa xác minh được hãng đĩa hiện tại của họ.

## 2. Tên thật / thông tin ca sĩ

- **Châu Khải Phong (#98) — MÂU THUẪN tên thật:** Dân Việt (31/03/2018) và vietnam.net ghi **"Lê Văn Thuận"**; báo Gia đình & Xã hội ghi **"Lê Minh Thuận"**. File singers.json tạm ghi "Lê Văn Thuận" (2 nguồn vs 1) với confidence=medium. Không có bài Wikipedia riêng để đối chiếu. Cần xác minh bằng CCCD/phỏng vấn chính thức hoặc Spotify/Wikipedia.
- **Châu Khải Phong — năm bắt đầu hoạt động:** ghi "2010–nay" là ước lượng (hit "Anh thích em như xưa" 2010; Dân Việt 2018 nói "sau hơn 10 năm hoạt động"). Chưa có nguồn chốt năm bắt đầu. Ngày sinh 30/10/1986, quê Nghệ An: chỉ có nguồn dnulib.edu.vn (trang tổng hợp, chất lượng trung bình) + vietnam.net.
- **Siu Black (#94) — tên khai sinh:** Wikipedia tiếng Việt ghi tên khai sinh là **"Siu Black"**; một số nguồn khác ghi "Nguyễn Thị Siu Black". Chưa đối chiếu được nguồn chính thức. Tạm ghi "Siu Black", confidence=medium.
- **Ngọc Sơn (#93) — Wikidata ID:** tra Wikidata API không ra mục ca sĩ (kết quả toàn núi Ngọc Sơn Đài Loan). wikidata_id để trống. Cần tra qua trang Wikipedia → liên kết Wikidata.
- **Ngọc Sơn — năm sinh:** Wikipedia vi/en và VietnamNet ghi 1968; Wikipedia tiếng Tây Ban Nha ghi 1970 trong infobox (nhưng thân bài ghi 1968). Tạm ghi 1968 (đa số nguồn), ghi nhận mâu thuẫn.
- **Tùng Dương (#95) — nơi sinh:** Wikipedia vi ghi "Hà Bắc" (nay Bắc Ninh), Wikipedia en ghi "Hanoi"; một số trang tiểu sử ghi quê Quảng Trị (đó là quê gốc, không phải nơi sinh). Tạm ghi "Hà Bắc (nay là Bắc Ninh)" theo Wikipedia vi, quê gốc Quảng Trị ghi trong bio là chưa đủ nguồn thứ 2.

## 3. Bài hát — tên bài trong top100-list sai / chưa xác minh

- **ICD (#100) — "Tài Sản Của Cha":** tên đúng là **"Tài Sản Của Bố"** (Wikipedia ICD + YouTube King of Rap tập 12). Đã sửa trong songs.json, ghi chú ở đây.
- **ICD — "Sau Này":** KHÔNG tìm thấy bằng chứng đây là bài của ICD (Wikipedia ICD liệt kê discography: The Killing ICD 2020, Sao em không... 2020, các tiết mục King of Rap). **Không đưa vào songs.json.** Thay bằng "Chân chạm đất" (2021, đã xác minh qua Znews + Tuổi Trẻ).
- **Phạm Anh Khoa (#99) — "Lý Quạu":** tên đúng là **"Lý Quạ Kêu"** (track 3 album PAK 01, sáng tác ghi "Dân ca"). Đã sửa trong songs.json.
- **Siu Black — "Đôi chân trần":** bài do Y Phôn Ksor sáng tác 1995, nổi tiếng nhất qua giọng **Y Moan** (Wikipedia có bài riêng). Chưa xác minh được bản thu/MV chính thức của Siu Black hát bài này. Giữ trong songs.json ở confidence=medium theo top100-list, cần kiểm chứng lại hoặc thay bằng bài khác của Siu Black.
- **Siu Black — "Ngọn lửa cao nguyên":** nhạc sĩ Trần Tiến đã xác minh (2 nguồn), nhưng **năm phát hành bản Siu Black để trống** (chỉ có bản live 2023 trên Gaana). Bài gốc ra đời khoảng 40 năm trước (theo Báo Gia Lai, ~1985) — không ghi năm vì chưa chắc năm đó là bản Siu Black.
- **Siu Black — "Đôi mắt Pleiku":** nhạc sĩ Nguyễn Cường xác minh (2 nguồn), **năm để trống**.
- **Hồ Văn Cường — năm của "Bà Năm", "Về miền Tây", "Còn thương rau đắng mọc sau hè":** ghi 2016 (năm thi Vietnam Idol Kids); album "Về miền Tây" phát hành 2017. Năm 2016 là năm trình diễn, không phải năm phát hành bản thu — cần phân biệt khi bổ sung sau.

## 4. Bài hát — chỉ 1 nguồn (confidence=medium)

- **Phan Mạnh Quỳnh — "Có chàng trai viết lên cây" (2019):** chỉ 1 nguồn (Cafef) nêu tên bài trong loạt hit; chưa đối chiếu Wikipedia/Apple Music của bài.
- **Châu Khải Phong — "Nếu ta ngược lối" (2018, nhạc sĩ Đinh Tùng):** chỉ 1 nguồn (dnulib).
- **Châu Khải Phong — "Nỗi đau mình anh" (nhạc sĩ Hùng Nguyễn, ft Trịnh Đình Quang):** chỉ 1 nguồn chính (dnulib) + Viberate xác nhận feat; **năm phát hành để trống**.
- **Phạm Anh Khoa — "Thời gian tôi":** mâu thuẫn đồng sáng tác (Wikipedia: Đức Trí; Deezer: Võ Thiện Thanh – Đức Trí) và thời lượng (Apple 3:43 vs Deezer 4:06) → duration để trống.
- **Tùng Dương — "Chiếc khăn piêu":** năm ghi 2013 (giải Cống hiến Bài hát của năm 2013, album Độc đạo 2013) nhưng danh sách đĩa đơn Wikipedia ghi đĩa đơn 2016 → mâu thuẫn nhỏ, cần làm rõ (có thể 2013 là năm biểu diễn/giải, 2016 là năm phát hành single).
- **Tùng Dương — "Con cò":** quán quân Bài hát Việt 2007 nhưng album "Li ti" 2010 → năm trong file là 2010 (năm album), cần ghi chú khi hiển thị.
- **Ngọc Sơn — "Tình cha":** Wikipedia bài riêng ghi "sáng tác từ khi 16 tuổi" nhưng cũng ghi "phát hành 1995"; chính Ngọc Sơn nói sáng tác năm 1995 (27 tuổi). File ghi 1995.
- **Đạt G — "Buồn của anh": MÂU THUẪN feat:** Wikipedia discography ghi "ft KHÁNH ft Masew"; Eva và Cafef ghi hát cùng **K-ICM và Masew**. File tạm ghi singers [Đạt G, K-ICM, Masew] theo 2 nguồn báo, ghi nhận KHÁNH là biến thể chưa rõ (có thể KHÁNH là tên khác của K-ICM thời đó). Cần đối chiếu credit Spotify/Apple Music.

## 5. Chưa tra

- VCPMC / Cục Bản quyền tác giả: không tra được trong batch này (không đăng nhập, không bypass) — nhạc sĩ các bài bolero/dân ca cũ (Bắc Sơn, Tô Thanh Tùng, Vũ Quốc Việt, Thanh Sơn, Tiến Luân) chỉ đối chiếu qua Wikipedia/báo, chưa qua VCPMC.
- Spotify monthly listeners / lượt nghe: không ghi (theo quy tắc không bịa số liệu).
- Lyric URL: chỉ 1 bài ("Thêm bao nhiêu lâu" — lyricvn.com). Còn lại chưa tra trang lời có bản quyền.

---

# (B) Mâu thuẫn và vấn đề PHÁT HIỆN KHI GỘP

## 1. Đính chính danh sách gốc — CẦN coordinator/John chốt (KHÔNG tự sửa `top100-list.md`)

| # | Ca sĩ | Danh sách gốc ghi | Batch phát hiện (bằng chứng) | Cần chốt |
|---|---|---|---|---|
| 90 | **Chế Linh** | Lưu Văn **Linh** | Batch 81-90: tên thật đúng là **Lưu Văn Liên** (Wikipedia VI/EN + trang official chelinh.com). Batch đã sửa trong `singers.json`. | Sửa `top100-list.md`: Lưu Văn Liên |
| 63 | **Trung Quân** | Nguyễn Trần Trung Quân | Batch 61-70: Nguyễn Trần Trung Quân là **một ca sĩ khác** (sinh 16/11/1992, Hà Nội). Người đúng là **Bùi Nguyễn Trung Quân — Trung Quân Idol** (sinh 20/1/1989, Đà Lạt); các bài Trót Yêu / Dấu Mưa / Chưa Bao Giờ đều của Bùi Nguyễn Trung Quân. Wikipedia (vi): trang "Trung Quân" = Bùi Nguyễn Trung Quân; trang "Nguyễn Trần Trung Quân" là người khác. Batch đã ghi Bùi Nguyễn Trung Quân trong `singers.json`. | Sửa `top100-list.md`: Bùi Nguyễn Trung Quân |
| 70 | **Hiền Hồ** | Võ Thị Hiền Hồ | Batch 61-70: tên thật đúng là **Hồ Thị Hiền** (Wikipedia vi + nhiều báo). Batch đã ghi Hồ Thị Hiền trong `singers.json`. | Sửa `top100-list.md`: Hồ Thị Hiền |
| 6 | **Vũ.** | Trần Anh Vũ | Batch 01-10: tên thật đúng là **Hoàng Thái Vũ** (ghi trong `singers.json` batch 01-10). | Sửa `top100-list.md`: Hoàng Thái Vũ |
| 73 | **Tuấn Ngọc** | Lữ Anh Tuấn | Batch 71-80: Wikipedia tiếng Việt ghi **Lã Anh Tuấn**. Batch đã ghi Lã Anh Tuấn trong `singers.json`. | Chốt Lã Anh Tuấn (theo Wikipedia) hay giữ Lữ Anh Tuấn |
| 50 | **LyLy** | Nguyễn Hoàng Ly | Batch 41-50: Wikipedia (vi + en) ghi tên khai sinh **Nguyễn Hoàng Lan** (sinh 1/1/1996, Quảng Nam – Đà Nẵng), kèm chú thích: "Phần lớn các nguồn đều đề cập tên gốc của nhân vật là 'Nguyễn Hoàng Ly', kể cả trên trang Facebook cá nhân" (Đời sống & Pháp luật 26/9/2024). Batch đã ghi Nguyễn Hoàng Lan + `real_name_note`, confidence ca sĩ = medium. | Chốt tên thật: Nguyễn Hoàng Lan hay Nguyễn Hoàng Ly |
| 88 | **Hương Lan** | Trần Ngọc Ánh | Batch 81-90: Wikipedia ghi **Trần Thị Ngọc Ánh** (danh sách gốc thiếu chữ "Thị"). Batch đã ghi Trần Thị Ngọc Ánh. | Sửa `top100-list.md`: Trần Thị Ngọc Ánh |
| 98 | **Châu Khải Phong** | (không ghi tên thật) | Batch 91-100: Dân Việt (31/03/2018) và vietnam.net ghi **"Lê Văn Thuận"**; báo Gia đình & Xã hội ghi **"Lê Minh Thuận"**. Batch tạm ghi "Lê Văn Thuận" (2 nguồn vs 1), confidence = medium. Không có bài Wikipedia riêng để đối chiếu. | Chốt Lê Văn Thuận hay Lê Minh Thuận |
| 94 | **Siu Black** | (không ghi tên thật) | Batch 91-100: Wikipedia tiếng Việt ghi tên khai sinh là **"Siu Black"**; một số nguồn khác ghi "Nguyễn Thị Siu Black". Batch tạm ghi "Siu Black", confidence = medium. | Chốt tên khai sinh |
| 46 | **Thịnh Suy** | (không ghi tên thật) | Batch 41-50: Wikipedia + Men's Folio + Saigoneer ghi **Đỗ Quốc Thịnh** (sinh 18/10/1999, Bình Định); Revelogue ghi **Nguyễn Quốc Thịnh**. Batch ghi theo đa số (Đỗ Quốc Thịnh). | Ghi nhận, cần nguồn chính thức nếu muốn chắc chắn |
| 49 | **Orange** | Khương Hoàn Mỹ | Batch 41-50: năm sinh mâu thuẫn — Wikipedia (vi + en) + Deezer ghi **15/2/1997**; Thanh Niên (14/1/2018) ghi **1996**. Batch ghi 1997 theo đa số. | Chốt năm sinh 1996 hay 1997 |
| 83 | **Quang Lê** | Lê Hữu Nghị | Batch 81-90: năm sinh mâu thuẫn — **1979** (Wikipedia hiện tại + chính Quang Lê trả lời Dân trí 2018: hộ chiếu ghi 1979, trước đây anh nói 1981 cho trẻ) vs 1980 (Fandom Thúy Nga) vs 1981 (nhiều nguồn cũ). Batch dùng 1979-01-24. | Chốt 1979 |
| 84 | **Phi Nhung** | Phạm Phi Nhung | Batch 81-90: năm sinh **1970** (Wikipedia VI/EN hiện tại, VnExpress 2024) vs 1972 (bản tin TTXVN lúc mất, Alchetron, VietCeleb). Batch dùng 1970-04-10. Ngày mất 28/9/2021 thống nhất. | Chốt 1970 |
| 85 | **Mạnh Quỳnh** | Nguyễn Thanh Dũng | Batch 81-90: năm sinh **22/4/1971, Sài Gòn** (Wikipedia) vs 1972 (Thanh Niên 2016; loibaihat.me) và nơi sinh Biên Hòa, Đồng Nai (tieusu.com; nhacxua.vn). Batch dùng 1971-04-22, Sài Gòn. | Chốt năm/nơi sinh |
| 89 | **Thanh Tuyền** | (không ghi tên thật) | Batch 81-90: năm sinh **29/10/1948** (Wikipedia VI hiện tại) vs 1947 (nhaxinhplaza) vs 1949 (hopamviet, Last.fm, nguoinoitieng.tv). Tên thật Phạm Như Mai thống nhất (Last.fm ghi "Nguyen Nhu Mai" là sai họ). Batch dùng 1948-10-29. | Chốt 1948 |
| 93 | **Ngọc Sơn** | Phạm Ngọc Sơn | Batch 91-100: năm sinh **1968** (Wikipedia vi/en, VietnamNet) vs 1970 (Wikipedia tiếng Tây Ban Nha, infobox — thân bài ghi 1968). Batch ghi 1968 theo đa số. Wikidata ID để trống (tra Wikidata API không ra mục ca sĩ). | Chốt 1968 |
| 95 | **Tùng Dương** | Nguyễn Tùng Dương | Batch 91-100: nơi sinh mâu thuẫn — Wikipedia vi ghi **"Hà Bắc"** (nay Bắc Ninh), Wikipedia en ghi "Hanoi"; một số trang ghi quê Quảng Trị (đó là quê gốc, không phải nơi sinh). Batch ghi "Hà Bắc (nay là Bắc Ninh)" theo Wikipedia vi. | Chốt nơi sinh |
| 57 | **Quang Dũng** | Thái Văn Dũng | Batch 51-60: năm sinh mâu thuẫn — Last.fm + NguoiNoiTieng ghi **08/08/1976**, Quy Nhơn; Mytour ghi 08/08/1980. Batch lấy 1976 theo 2 nguồn. Tên thật Thái Văn Dũng chỉ 1 nguồn. | Chốt 1976 |
| 52 | **Noo Phước Thịnh** | Nguyễn Phước Thịnh | Batch 51-60: `birth_date` **TRỐNG** — Báo Nghệ An chỉ ghi sinh ngày 18/12, không ghi năm; năm 1988 chưa kiểm chứng. Tên thật: lúc sinh ông nội đặt Nguyễn Phước Thanh, mẹ đổi thành Thịnh — tên khai sinh đầy đủ cần đối chiếu thêm. | Bổ sung ngày sinh |
| 34 | **Wowy** | Nguyễn Minh Huy | Batch 31-40: Fandom Masked Singer ghi **"Nguyễn Ngọc Minh Huy"**; chỉ có năm sinh 1988, **không có ngày/tháng sinh**. Batch dùng Nguyễn Minh Huy theo danh sách chốt. | Chốt tên thật + ngày sinh |
| 15 | **Grey D** | Đoàn Thế Lân | Batch 11-20: **không có MusicBrainz ID và Spotify artist ID** (MB search nhiều lần không có bản ghi VN khớp). Ngày sinh mâu thuẫn: Wikipedia ghi 11/12/2000, bloganchoi.com ghi 04/11/2000 — batch lấy 11/12/2000 theo Wikipedia, confidence ca sĩ = medium. | Chốt ngày sinh; bổ sung MBID/Spotify ID |
| 11 | **MONO** | Nguyễn Việt Hoàng | Batch 11-20: ngày sinh mâu thuẫn — Wikipedia vi/en ghi **21/1/2000**, báo Thanh Niên (7/8/2022) ghi 20/1/2000. Batch lấy 21/1/2000 (đa số nguồn). | Chốt 21/1/2000 |
| 20 | **Văn Mai Hương** | Văn Mai Hương | Batch 11-20: tên thật mâu thuẫn — Wikipedia ghi "Văn Mai Hương", Kenh14 ghi "Nguyễn Văn Mai Hương". Batch lấy theo Wikipedia. | Chốt tên thật |
| 61 | **Uyên Linh** | Trần Nguyễn Uyên Linh | Batch 61-70: năm sinh mâu thuẫn — Wikipedia (vi/en) ghi **1987** (theo chính ca sĩ xác nhận tuổi mèo); nhiều báo năm 2010 ghi **1988**. Batch ghi 1987-12-31. | Chốt 1987 |
| 4 | **Đen** | Nguyễn Đức Cường | Batch 01-10: nơi sinh mâu thuẫn — Wikipedia vi + VnExpress: **Hạ Long, Quảng Ninh**; Wikipedia en: tỉnh **Đồng Nai**; Wikidata P19 tra nhãn ra **Hưng Yên** (không khớp cả hai). Batch ghi "Hạ Long, Quảng Ninh" (2 nguồn vi). | Chốt nơi sinh |
| 86 | **Đan Nguyên** | Nguyễn Đặng Đan | Batch 81-90: **không có trang Wikipedia**; tên thật Nguyễn Đặng Đan + sinh 9/7/1984 chỉ có từ mô tả video official và Izumi — confidence medium, cần đối chiếu thêm. | Bổ sung nguồn thứ 2 |
| 67 | **Myra Trần** | (không ghi tên thật) | Batch 61-70: không có bài Wikipedia (vi/en), không có Wikidata QID. Tên thật Trần Minh Như + sinh 3/6/1999 chỉ có Fandom Thúy Nga + báo Eva/Vietnamnet — confidence medium. | Bổ sung nguồn |
| 77 | **Thanh Hà** | Trương Minh Hà | Batch 71-80: **không tìm thấy thực thể Wikidata** cho ca sĩ Thanh Hà (Trương Minh Hà) qua wbsearchentities (vi/en); `wikidata_id` trống; `image_url` trống; `years_active` "1990s–nay" ước lượng — confidence ca sĩ = medium. | Bổ sung Wikidata ID |
| 51 | **Hồ Ngọc Hà** | Hồ Ngọc Hà | Batch 51-60: nơi sinh mâu thuẫn — Wikipedia EN ghi **Huế**; Simple Wikipedia ghi Đồng Hới, Quảng Bình; EverybodyWiki ghi An Cựu, Huế rồi chuyển về Quảng Bình. Batch lấy Huế theo Wikipedia EN. | Chốt nơi sinh |

## 2. Bài hát trong danh sách gốc bị batch thay thế (vì sai / không có bằng chứng)

Danh sách đầy đủ, theo UNVERIFIED từng batch. Bài thay thế đã nằm trong file tổng; bài gốc
không đưa vào file tổng (trừ trường hợp ghi chú riêng).

| Ca sĩ | Bài trong danh sách gốc | Vấn đề (theo batch) | Bài thay thế trong file tổng |
|---|---|---|---|
| Seachains (#41) | "Cảm Ơn Và Xin Lỗi" | Là bài của **Chillies** (OST phim "Thưa Mẹ Con Đi"), không phải của Seachains (batch 41-50 §3) | Simple Love, Slow Down, Anh 17, Chó chạy ngoài đồng |
| Seachains (#41) | "Trở Về" | Không tìm thấy bằng chứng là bài của Seachains (batch 41-50 §3) | (như trên) |
| Lil Wuyn (#43) | "Không Sao Cả" | Là bài của **7dnight** (Rap Việt mùa 4, đội BigDaddy), không phải của Lil Wuyn (batch 41-50 §3) | Silence, Còn Thở Còn Gỡ, Mở Mắt (ft. Đen), Như Vậy Nhé (ft. Wxrdie) |
| Lil Wuyn (#43) | "Lãng Du" | Không tìm thấy bằng chứng là bài của Lil Wuyn — kết quả chỉ ra bài "Lãng Du" của MCK ft. Wren Evans và các bài cùng tên khác (batch 41-50 §3) | (như trên) |
| Phùng Khánh Linh (#48) | "Quý Cô Say Xỉn" | Không tìm thấy trong các nguồn đã đọc (Wikipedia en/vi, nguoiquansat) (batch 41-50 §3) | Hôm Nay Tôi Buồn, World Without You, Cô gái nhân ái (He Said She Said), Sweet Summer |
| Lê Cát Trọng Lý (#47) | "Khói Thuốc Cà Phê" | Không tìm thấy trong các nguồn đã đọc (batch 41-50 §3) | Chênh vênh, Tám chữ có, Em đứng trên cánh đồng, Không sao về bắt đầu |
| ICD (#100) | "Tài Sản Của Cha" | Tên đúng là **"Tài Sản Của Bố"** (Wikipedia ICD + YouTube King of Rap tập 12) (batch 91-100 §3) | Tài sản của bố |
| ICD (#100) | "Sau Này" | **KHÔNG tìm thấy bằng chứng đây là bài của ICD** (Wikipedia ICD liệt kê discography: The Killing ICD 2020, Sao em không... 2020, các tiết mục King of Rap). **Không đưa vào file tổng** (batch 91-100 §3) | Chân chạm đất (2021, đã xác minh qua Znews + Tuổi Trẻ) |
| Phạm Anh Khoa (#99) | "Lý Quạu" | Tên đúng là **"Lý Quạ Kêu"** (track 3 album PAK 01, sáng tác ghi "Dân ca") (batch 91-100 §3) | Lý quạ kêu |
| Trường Vũ (#87) | "Đám Cưới Nghèo" | **ĐÃ LOẠI** vì ghi công mâu thuẫn không phân xử được (Gaana: Giao Linh; truongca: Thu Anh; Gaana khác: Anh Thy) (batch 81-90 §2) | Hoa Sứ Nhà Nàng (đã xác minh) |
| Hiền Hồ (#70) | "Cưới Nhau Đi" | Không tìm thấy bản Apple Music khớp nên **không đưa vào**; Hiền Hồ giữ 3 bài (batch 61-70 §5) | — (không thay bằng bài khác) |
| Lâm Bảo Ngọc (#65) | "Vùng Ký Ức" | Không tìm thấy bản Apple Music solo khớp nên không đưa vào (batch 61-70 §5) | Nói Không Thành Lời (2023, đã kiểm chứng) |
| Dương Hoàng Yến (#66) | "Cầu Vồng Khuyết" | **Không phải bài của Dương Hoàng Yến** — bài này của Cara, nhạc sĩ Minh Khang (batch 61-70 §5) | — (không đưa vào) |
| Vũ. (#6) | "Mùa Mưa Ngâu Nằm Cạnh Nhau" (tên trong bản demo cũ) | Wikipedia vi (danh sách MV) ghi **"Mùa mưa ngâu nằm cạnh"**, MV 25/9/2016 (batch 01-10 §1.8) | Mùa Mưa Ngâu Nằm Cạnh |
| Siu Black (#94) | "Đôi chân trần" | Bài do Y Phôn Ksor sáng tác 1995, nổi tiếng nhất qua giọng **Y Moan** (Wikipedia có bài riêng). **Chưa xác minh được bản thu/MV chính thức của Siu Black** hát bài này. Batch giữ trong file tổng ở confidence = medium theo top100-list — **cần kiểm chứng lại hoặc thay bằng bài khác của Siu Black** (batch 91-100 §3) | — (đang giữ tạm, cần chốt) |
| Đạt G (#97) | "Buồn của anh" | **Mâu thuẫn feat:** Wikipedia discography ghi "ft KHÁNH ft Masew"; Eva và Cafef ghi hát cùng **K-ICM và Masew**. Batch tạm ghi singers [Đạt G, K-ICM, Masew] theo 2 nguồn báo; KHÁNH có thể là tên khác của K-ICM thời đó. Cần đối chiếu credit Spotify/Apple Music (batch 91-100 §4) | — (đang giữ tạm, cần chốt) |

Các trường hợp "không dùng link/video sai" (ghi nhận để đợt sau không dùng nhầm):

- Min — "Ghen": **KHÔNG dùng** video "Ghen Cô Vy" (`BtulL3oArQw`) — đó là bài khác (phiên bản COVID-19 năm 2020) (batch 21-30 §8).
- Soobin — "Phía sau một cô gái": **KHÔNG dùng** video `w1_EJefzZMk` — đó là bản cover của fan (Kiyushi), không phải official (batch 21-30 §8).
- Isaac — "Anh sẽ về sớm thôi": video `xcUIBHapq20` chỉ là **teaser**, không phải MV chính thức → không dùng (batch 21-30 §8).
- Sơn Tùng M-TP — "Chạy Ngay Đi": link YouTube tìm được (`-vtBgNxMyZI`) là bản **Onionn Remix**, KHÔNG phải bản gốc nên không ghi vào bản gốc (batch 01-10 §2).
- Andree Right Hand (#42): nguồn doanhnhanonline.com.vn ghi sai "Lê Xuân Đức, 18/4/1987, Hà Nội" và liệt kê hit của rapper khác — nguồn này KHÔNG được dùng (batch 41-50 §2).
- Trường Vũ (#87): nguồn izumi.edu.vn ghi "Phan Thanh Sơn, sinh 20/9/1971 tại Quảng Trị" — SAI hoàn toàn so với Wikipedia + nhiều nguồn (Huỳnh Văn Ngoảnh, 25/2/1963, Vĩnh Châu, Bạc Liêu). Không dùng nguồn này (batch 81-90 §2).
- tlinh — "Thích Quá Rùi Nà" feat: hay nhầm với MCK; Wikipedia vi + Kworb + MusicBrainz đều ghi feat. **Trung Trần**, phát hành 24/3/2020 — KHÔNG phải MCK (batch 01-10 §1.9).
- Wowy — "Chạy": Apple Music chỉ có bản "Chạy (feat. LD SouthGanz) [From Ròm]" 28/07/2020 — batch dùng năm bản gốc 2013, **không dùng thời lượng/link của bản 2020** (batch 31-40 §5).
- Binz — "Bigcityboi": Apple Music chỉ còn bản remix (Kriss Ngo Remix, 2026) nên **không dùng link/thời lượng Apple Music**; năm 2020 lấy từ VnExpress (batch 31-40 §5).
- Min — "Có em chờ": vanhoadoisong.vn liệt kê "Sáng tác: Khắc Hưng" mâu thuẫn với Wikipedia vi ("Sáng tác: Kai Đinh, Sản xuất: Khắc Hưng"), mô tả YouTube và phỏng vấn Znews → giữ Kai Đinh; Khắc Hưng là nhà sản xuất, không phải nhạc sĩ (batch 21-30 §4).
- Isaac — "Yêu không nghỉ phép": Wikipedia vi — Only C liệt kê bài này trong danh sách sáng tác của Only C, mâu thuẫn với Dân Việt, Kenh14, Văn hóa Đời sống và bảng Hòa âm Ánh sáng (đều ghi Nguyễn Phúc Thiện) → giữ Nguyễn Phúc Thiện (batch 21-30 §4).
- Isaac — "Mr. Right (Khi anh yêu em)": Wikipedia vi — Only C ghi "lời của Mr. Doji" (nhạc: Only C); Gaana ghi "composed by OnlyC"; nhưng VTC News ghi "Nhạc: Hoàng Touliver, Lời: OnlyC" → giữ composers [Only C], lyricists [Mr. Doji] theo đa số, hạ `composer_confidence` = medium (batch 21-30 §4).

## 3. Vấn đề phát hiện khi gộp (không có trong UNVERIFIED từng batch)

### 3.1. Bài trùng tên nhưng khác bài — đã tách

- **"Chưa Bao Giờ" là 2 bài khác nhau**, không gộp: bản của Trung Quân (nhạc sĩ Tiên Tiên, 2015,
  album "Chưa Bao Giờ - Single") và bản của Thu Phương (nhạc sĩ Việt Anh, chưa rõ năm).
  Batch 61-70 đã xác minh: "Chưa Bao Giờ" (Trung Quân) là sáng tác của **Tiên Tiên, KHÔNG phải
  Tiên Cookie**. File tổng giữ 2 bản ghi riêng (`song-248`, `song-249`).

### 3.2. Bài trùng đã gộp — mâu thuẫn giá trị giữa các batch

- **9 nhóm gộp thành 1 bản ghi** (xem README.md mục 7): "Anh Nhà Ở Đâu Thế", "Có Chàng Trai Viết
  Lên Cây", "Có phải em mùa thu Hà Nội", "Còn Thương Rau Đắng Mọc Sau Hè", "Người Lạ Ơi",
  "Nơi Tình Yêu Bắt Đầu", "Sa Mưa Giông", "Simple Love", "vaicaunoicokhiennguoithaydoi".
  Mâu thuẫn đã xử lý: năm "Có Chàng Trai Viết Lên Cây" 2019 vs 2020 (giữ 2019);
  năm "Có phải em mùa thu Hà Nội" 1996 vs 1997 (giữ 1996 — cả hai đều là năm album iTunes,
  chưa chắc là năm thu âm gốc, theo batch 71-80 §3); năm "Còn Thương Rau Đắng Mọc Sau Hè"
  1974 (năm sáng tác) vs 2016 (năm bản thu của Hồ Văn Cường — batch 91-100 §3 lưu ý năm 2016 là
  năm trình diễn, không phải năm phát hành bản thu) — giữ 1974; album "Có Chàng Trai Viết Lên Cây":
  "Truyện Ngắn" vs "OST Mắt Biếc (2019)"; duration/link Apple khác nhau giữa hai bản
  "Có phải em mùa thu Hà Nội" (344s vs 341s). Các giá trị không được chọn vẫn ghi trong `notes`
  của bản ghi bài hát — cần đối chiếu lại ngày phát hành gốc trước khi dùng làm dữ liệu bán hàng.
- **"Sa Mưa Giông"**: bản batch 81-90 để trống năm, bản batch 91-100 ghi 2017 — 2017 là năm bản thu
  của Hồ Văn Cường (theo cách ghi của batch 91-100), chưa phải năm sáng tác gốc của Bắc Sơn;
  file tổng giữ year = 2017 theo bản ghi duy nhất có năm, cần xác minh năm sáng tác gốc.
- **"Anh Nhà Ở Đâu Thế"**: `composers` gộp thành [Hứa Kim Tuyền, "Lyly", "LyLy"] — "Lyly"
  (batch 01-10, theo Wikipedia bài Dreamee) và "LyLy" (batch 41-50) là **cùng một người, hai cách
  viết**. File tổng giữ nguyên cả hai chuỗi như batch đã ghi (không tự sửa), cần chuẩn hoá tên
  nhạc sĩ về một dạng duy nhất ở đợt sau.

### 3.3. Edge không đưa vào file tổng (105/735 edge thô)

- **98 edge có đầu mút là nghệ sĩ ngoài Top 100** (52 người, không có node trong file tổng nên
  không giữ edge; thông tin feat/collab của họ vẫn giữ trong `songs[].singers` — 75 lượt gắn,
  ở 65 bài): 2pillz, B Ray, Biên, Boyzed, Chillies, Da LAB, Davis, Drum7, Du Uyên,
  Dương Trường Giang, Emily, F.HERO, GDucky, Hoàng Rob, Hoàng Tôn, K-ICM, Masew, Kay Trần,
  Khang Việt, Khói, Lam Anh, Lena, Linh Cáo, Magazine, Marzuz, Mew Amazing, Mr. Siro, NIT, Nah,
  Negav, Nguyên Thảo, OnlyC, Pháo, Phương Ly, PiaLinh, RedT, Ricky Star, Ronboogz, SUNI Hạ Linh,
  Shiki, Thai Viet G, Thắng, Touliver, Trung Trần, Trịnh Đình Quang, Tuấn Cry, Tùng Maru, VSOUL,
  VSTRA, Vương Anh Tú, Wxrdie, Xuân Hinh, buitruonglinh. Trong đó có cả các edge `performs` từ
  ca sĩ feat ngoài Top 100 (ví dụ Mr. Siro → "Không Thể Cùng Nhau Suốt Kiếp", Xuân Hinh /
  Tuấn Cry → "Bắc Bling (Bắc Ninh)", Chillies → "Đưa Em Về Nhàa") — tên người thể hiện vẫn giữ
  trong `singers[]` của bài hát, chỉ không có edge riêng.
  Ngoại lệ ghi nhận: edge batch 91-100 Đạt G → **"K-ICM, Masew"** (một chuỗi gộp 2 tên trong một
  endpoint) không phân giải được thành 1 người — cần batch 91-100 tách lại nếu muốn giữ edge này.
- **5 edge trùng** (cùng ca sĩ–bài / ca sĩ–ca sĩ đã có ở batch khác, đã gộp `sources[]` vào edge
  giữ lại): Grey D → tlinh ("vaicaunoicokhiennguoithaydoi"); Seachains → "Simple Love";
  Orange → "Người lạ ơi"; Seachains → Obito; Orange → Karik.
- **1 edge sai của batch, đã bỏ:** batch 41-50 `singer-singer-composer-for` **LyLy → Lou Hoàng**,
  evidence: "LyLy sáng tác 'Không sao mà, em đây rồi' cho Suni Hạ Linh; Lou Hoàng là #28 trong
  top100" — evidence nêu người nhận là **Suni Hạ Linh** (ngoài Top 100), không phải Lou Hoàng.
  Việc LyLy sáng tác bài này vẫn được giữ qua edge `composed` LyLy → bài hát (batch 41-50).
  Vai trò của Lou Hoàng trong bài "Không sao mà, em đây rồi" còn mâu thuẫn: `singers[]` của batch
  41-50 ghi [Suni Hạ Linh, Lou Hoàng] nhưng không có edge `performed_by` nào chứng minh Lou Hoàng
  thể hiện bài này — cần xác minh lại.
- **1 edge tự trỏ sau khi gộp:** batch 71-80 `same_song_different_singer` "Có phải em mùa thu Hà
  Nội" → chính nó — sau khi gộp 2 bản ghi thành 1 bài, edge này thành self-loop nên bỏ; việc hai
  ca sĩ cùng thể hiện bài này đã ghi trong `singers[]` = [Hồng Nhung, Thu Phương] và edge
  `same_song` Hồng Nhung → Thu Phương vẫn giữ.
- **1 edge đổi chiều theo evidence:** batch 11-20 ghi `same_composer` "Hòa Minzy → Tăng Duy Tân"
  nhưng evidence viết "Tăng Duy Tân sáng tác 'Bật Tình Yêu Lên' cho Hòa Minzy" → file tổng ghi
  `composed_for` **Tăng Duy Tân → Hòa Minzy** (đổi chiều cho khớp evidence).
- **6 edge `same_composer` ca sĩ–ca sĩ được đổi nhãn thành `shared_composer`** (cùng nhạc sĩ, không
  phải cùng bài hát): Mỹ Tâm → Erik (cùng Khắc Hưng); Bùi Anh Tuấn → Hiền Hồ, Bùi Anh Tuấn →
  Myra Trần, Myra Trần → Hiền Hồ, Bùi Anh Tuấn → Lâm Bảo Ngọc (cùng Vương Anh Tú);
  Uyên Linh → Lâm Bảo Ngọc (cùng Hứa Kim Tuyền).

### 3.4. Hiệu chỉnh tên người thể hiện khi gộp (có bằng chứng trong batch)

- Batch 41-50 ghi nhầm nhạc sĩ **LyLy** vào `singer_stage_names` (trường ca sĩ thể hiện) ở 2 bài:
  "Anh nhà ở đâu thế" (`singers` đúng là [AMEE, B Ray]) và "Không sao mà, em đây rồi"
  (`singers` đúng là [Suni Hạ Linh, Lou Hoàng]) → file tổng đã bỏ LyLy khỏi `singers[]` của 2 bài
  này; LyLy vẫn giữ trong `composers[]`.
- Batch 21-30 viết tắt **"Anh Tú"** trong `singers[]` của 4 bài ("Cuộc sống em ổn không",
  "Mình làm người yêu nhé em", "Mạnh mẽ lên cô gái", "Nếu ta không may") trong khi edge
  `performed_by` ghi `singer-029` = **Anh Tú Atus** → file tổng chuẩn hoá thành "Anh Tú Atus".
- Batch 61-70 để `singers = null` ở cả 35 bài, chỉ ghi `singer_stage_names` — file tổng đã lấy
  danh sách người thể hiện từ `singer_stage_names` + edge `performs` của batch (bao gồm cả người
  feat ngoài Top 100 như Dương Trường Giang, Vương Anh Tú, Kay Trần, Tùng Maru, RedT,
  buitruonglinh — những người này vừa là nhạc sĩ vừa góp giọng theo edge của batch, nên vẫn giữ
  trong `singers[]` của bài).

### 3.5. Hai bài không có ca sĩ chính trong Top 100

- **"Ex's Hate Me"** — bài của B Ray ft. AMEE (AMEE có edge `featured_on`); không có edge
  `performed_by` tới ca sĩ Top 100 vì ca sĩ chính B Ray nằm ngoài Top 100.
- **"Không sao mà, em đây rồi"** — LyLy sáng tác cho Suni Hạ Linh (edge `composed`); `singers[]`
  ghi [Suni Hạ Linh, Lou Hoàng] nhưng vai trò Lou Hoàng chưa được edge nào chứng minh (xem §3.3).
  Cả 2 bài vẫn giữ trong file tổng vì đã có trong batch; không tự xoá dữ liệu batch.

### 3.6. Mâu thuẫn năm phát hành / metadata khác (đã ghi trong file tổng, chưa ngã ngũ)

Toàn bộ các mục này đã có trong UNVERIFIED từng batch ở phần (A) — liệt kê lại các mục còn ảnh
hưởng trực tiếp tới file tổng:

- Tăng Duy Tân — "Bên Trên Tầng Lầu": thân bài Wikipedia vi ghi phát hành tháng 8/2021; bảng đĩa
  đơn Wikipedia ghi 2022; Soha/Kenh14 ghi 2022. File tổng tạm lấy **2021** (batch 11-20 §5).
- Sơn Tùng M-TP — "Lạc Trôi": MusicBrainz + en Wikipedia: 31/12/2016; vi Wikipedia infobox:
  1/1/2017 (ngày MV lên YouTube). File tổng ghi 2016 (batch 01-10 §1.2).
- Vũ. — "Bước Qua Nhau": Wikipedia/Kenh14 gắn với album Một Vạn Năm (2022) và đề cử Cống hiến
  2019; MusicBrainz single ghi 2021-11-11. File tổng ghi 2020, confidence medium (batch 01-10 §1.7).
- Wowy — "Khu Tao Sống": single Apple Music 04/07/2012, nhưng CV Galerie Quynh ghi MV 2010.
  File tổng dùng 2012 (batch 31-40 §5). Suboi — "Cho Không", "Bet On Me": Wikipedia/NME ghi
  single 2019; Apple Music hiển thị 15/06/2021 (nhiều khả năng là ngày phát hành lại theo album
  No Nê). File tổng dùng 2019 (batch 31-40 §5).
- Tuấn Hưng — "Tìm Lại Bầu Trời": danh sách top100 gợi ý 2012, Mytour ghi phát hành 2013.
  File tổng lấy 2013 theo Mytour (batch 51-60 §3).
- Tùng Dương — "Chiếc khăn piêu": năm ghi 2013 (giải Cống hiến Bài hát của năm 2013, album Độc đạo
  2013) nhưng danh sách đĩa đơn Wikipedia ghi đĩa đơn 2016 (batch 91-100 §4).
- Tùng Dương — "Con cò": quán quân Bài hát Việt 2007 nhưng album "Li ti" 2010 → file tổng ghi
  2010 (năm album) (batch 91-100 §4). Ngọc Sơn — "Tình cha": Wikipedia bài riêng ghi "sáng tác từ
  khi 16 tuổi" nhưng cũng ghi "phát hành 1995"; chính Ngọc Sơn nói sáng tác năm 1995 (27 tuổi).
  File tổng ghi 1995 (batch 91-100 §4).
- Phạm Anh Khoa — "Thời gian tôi": mâu thuẫn đồng sáng tác (Wikipedia: Đức Trí; Deezer:
  Võ Thiện Thanh – Đức Trí) và thời lượng (Apple 3:43 vs Deezer 4:06) → duration để trống
  (batch 91-100 §4).
- Min — "Y.Ê.U": ISRC `FRX762174975` lấy từ bản ghi MusicBrainz phát hành lại ngày 30/11/2021,
  **chưa xác nhận là ISRC của bản gốc 2015** (batch 21-30 §7). Bảo Anh — "Anh muốn em sống sao":
  MusicBrainz trả về **2 ISRC** (`VNR011038027`, `VNR011046964`); file tổng chỉ giữ ISRC đầu,
  ISRC thứ hai ghi ở đây (batch 21-30 §7).
- AMEE — "Sao Anh Chưa Về Nhà" / "Yêu Thì Yêu Không Yêu Thì Yêu": duration/ISRC trong file tổng
  lấy từ **bản acoustic** trên MusicBrainz (có chú thích trong `sources`), chưa chắc bằng bản
  album gốc (batch 01-10 §1.10–1.11).
- Đập Vỡ Cây Đàn: ghi công mâu thuẫn — Hoa Linh Bảo (Thúy Nga PBN 82; Đan Nguyên Official; Gaana)
  vs Tùng Vân – Tuyết Sơn (bản Làng Văn của Duy Khánh). File tổng giữ Hoa Linh Bảo (bút danh
  Lê Mộng Bảo), confidence medium (batch 81-90 §2). Căn Nhà Màu Tím: Wikipedia Hoài Linh ghi một
  mình Hoài Linh (1969); Dân Việt ghi "Hoài Linh, Loan Thảo". File tổng giữ Hoài Linh
  (batch 81-90 §2). Xin Làm Người Xa Lạ / Mai Lỡ Mình Xa Nhau: bút danh Tú Nhi vs Lưu Trần Lê —
  cả hai đều là bút danh của Chế Linh (batch 81-90 §2).
- Chuyện Hoa Sim: năm sáng tác 1994 vs phát hành 1995 — file tổng giữ year = 1995, ghi chú 1994
  (batch 81-90 §2). Đoạn Cuối Tình Yêu: năm sáng tác 1970 vs Shazam ghi phát hành 1/1/1974 —
  file tổng giữ 1970, ghi chú 1974 (batch 81-90 §2). Thành Phố Buồn: 1970 (Wikipedia) vs một
  video MP Melody ghi 1973 — giữ 1970 (batch 81-90 §2). Giấc Mơ Có Thật (album): 24/10/2004 vs
  27/8/2004 — chưa phân xử (batch 81-90 §2).
- Đan Trường — "Kiếp ve sầu": lời Việt Nguyễn Ngọc Thiện — high (2 báo); tác giả nhạc gốc (nhạc
  Hoa) CHƯA xác minh. "Mưa trên cuộc tình": Lê Quang viết lời Việt — medium; tác giả nhạc gốc
  (nhạc Hoa) CHƯA xác minh (batch 71-80 §3). "Mong manh tình về": bản gốc do Quốc Thiên thể hiện
  đầu tiên (Đức Trí nhạc, Trương Hồ Phương Nga lời); Thanh Hà là bản cover nổi tiếng (batch 71-80 §4).
- Phương Thanh — "Giã từ dĩ vãng": nhạc sĩ Nguyễn Đức Trung — medium, chỉ 1 nguồn yếu (mô tả video
  YouTube AI cover). Cần nguồn thứ 2 (bìa album/phim hoặc VCPMC) (batch 71-80 §3).
- Bảo Anh — "Sống xa anh chẳng dễ dàng": Wikipedia vi — Mr. Siro ghi "(Bảo Anh ft. Mr. Siro)";
  trang lời có đoạn lời ghi "[Mr.Siro:]" → có thể Mr. Siro có góp giọng, nhưng file tổng vẫn chỉ
  ghi `singers` = [Bảo Anh] vì Wikipedia vi — Bảo Anh không ghi feat. Cần kiểm chứng MV gốc trước
  khi thêm Mr. Siro (batch 21-30 §4).
- Orange — "Khi em lớn": album "Cam'On" (2024) theo Wikipedia, nhưng bài phát hành lần đầu 2021
  dưới dạng đĩa đơn — cần phân biệt single gốc vs. album tổng hợp khi dùng dữ liệu (batch 41-50 §4).
- Châu Khải Phong — "Bà Năm" / "Về miền Tây" / "Còn thương rau đắng mọc sau hè" (Hồ Văn Cường):
  năm 2016 ghi trong file là năm thi Vietnam Idol Kids; album "Về miền Tây" phát hành 2017.
  Năm 2016 là năm trình diễn, không phải năm phát hành bản thu (batch 91-100 §3).
- Siu Black — "Ngọn lửa cao nguyên": nhạc sĩ Trần Tiến đã xác minh (2 nguồn), nhưng **năm phát hành
  bản Siu Black để trống** (chỉ có bản live 2023 trên Gaana). Bài gốc ra đời khoảng 40 năm trước
  (theo Báo Gia Lai, ~1985) — không ghi năm vì chưa chắc năm đó là bản Siu Black (batch 91-100 §3).

## 4. Field trống hàng loạt trong file tổng (để trống, không đoán)

- **ISWC: 0/380 bài.** Không tra được từ nguồn công khai nào trong 10 batch.
- **ISRC: chỉ 31/380 bài (8,2%).** Batch 01-10: 16/40; 21-30: 12/40; 11-20: 3/40;
  7 batch còn lại: 0 bài.
- **YouTube official: chỉ 39/380 bài (10,3%).** MV official chắc chắn tồn tại với hầu hết các bài,
  nhưng các batch KHÔNG đoán video ID — cần mở kênh official từng ca sĩ để lấy đúng video ID.
- **Spotify track URL: 7/380 bài; Apple Music URL: 96/380; duration: 163/380; lyric URL: 12/380.**
- **Nhạc sĩ trống: 35/380 bài (9,2%)** — tập trung ở batch 41-50 (12 bài) và 51-60 (11 bài).
  Danh sách đầy đủ các bài trống nhạc sĩ xem README.md mục 5–6 và `songs.json`
  (`composers == []`).
- **Năm trống: 58/380 bài (15,3%)** — tập trung ở batch 81-90 (19 bài), 71-80 (16 bài), 51-60 (15 bài).
- **Spotify ID ca sĩ trống: 76/100** — các batch 31-40, 41-50, 51-60, 61-70, 81-90, 91-100 đều 0/10.
- **MusicBrainz ID ca sĩ trống: 44/100; Wikidata ID trống: 33/100.** Batch 41-50 và 81-90 trống cả 10
  ca sĩ ở cả hai field này (chưa tra trực tiếp).
- **Ảnh ca sĩ trống: 64/100** — các batch 11-20, 51-60, 61-70, 81-90, 91-100 đều 0/10 ảnh.
  Trong 36 ảnh đã có, **20 ảnh chưa rà giấy phép từng file** (`image_license` null) — cần rà trên
  trang file Commons trước khi hiển thị/hotlink công khai (theo UNVERIFIED batch 01-10 §2,
  21-30 §1, 41-50 §5).
- **Hook line trống ở phần lớn bài; `lyric_url` trống ở 368/380 bài** — không chép lời khi chưa đối
  chiếu nguồn lời có bản quyền.

---

*Hết file UNVERIFIED tổng. Mọi mục trong phần (A) là nguyên văn từ batch; phần (B) là ghi nhận
của Merge agent khi gộp, chưa phải quyết định cuối — coordinator/John chốt các mục ở (B) §1–§2.*
