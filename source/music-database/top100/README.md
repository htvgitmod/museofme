# Cơ sở dữ liệu nhạc Việt — Top 100 ca sĩ Việt Nam (file tổng)

> **Ngày gộp:** 13/11/2026 — Merge + Verify từ 10 batch đã xong.
> **Phạm vi:** chỉ gộp + đếm thật + viết tài liệu. KHÔNG crawl thêm dữ liệu mới, KHÔNG bịa field thiếu,
> KHÔNG làm giao diện, KHÔNG sửa `top100-list.md`, KHÔNG sửa dữ liệu trong `batches/`.

## 1. File trong thư mục này

| File | Nội dung | Số dòng / bản ghi |
|---|---|---|
| `top100-list.md` | Danh sách chốt 100 ca sĩ (không đụng tới khi gộp) | 100 ca sĩ |
| `singers.json` | 100 ca sĩ, ID chuẩn `singer-001`…`singer-100` theo số thứ tự top100 | 100 bản ghi |
| `songs.json` | Bài hát unique sau khử trùng | **380 bản ghi** |
| `edges.json` | Edge chuẩn hoá, chỉ giữ edge có bằng chứng, đầu mút đều là node trong file tổng | **630 edge** |
| `singers.csv` | Cùng dữ liệu `singers.json`, mở được bằng Excel (UTF-8 + BOM, mảng nối bằng `"; "`) | 100 dòng + header |
| `songs.csv` | Cùng dữ liệu `songs.json`, mở được bằng Excel (UTF-8 + BOM) | 380 dòng + header |
| `README.md` | File này | — |
| `UNVERIFIED.md` | Toàn bộ UNVERIFIED của 10 batch + mâu thuẫn phát hiện khi gộp | — |

Nguồn: `batches/batch-01-10/` … `batches/batch-91-100/` (mỗi batch có `singers.json`, `songs.json`,
`edges.json`, `UNVERIFIED.md`).

## 2. Phương pháp chọn Top 100 (trích từ `top100-list.md`, chốt 13/11/2026)

Tiêu chí chọn:

1. **Ca sĩ Việt, ưu tiên đang hoạt động / có ảnh hưởng lớn** — vẫn được nghe nhiều trên streaming,
   YouTube, radio, sân khấu; không chọn ca sĩ chỉ nổi tiếng về mặt lịch sử mà không còn bản ghi được nghe nhiều.
2. **Có catalogue đủ để crawl:** mỗi ca sĩ 3–5 bài nổi tiếng nhất (mục tiêu chung: 100 ca sĩ → 300–500 bài).
3. **Cân bằng nhiều chiều:** nam/nữ; nhiều thế hệ (hải ngoại/trữ tình → 2000s → Gen Z); nhiều thể loại
   (Pop, Ballad, R&B, Rap/Hip-hop, Indie, Bolero/trữ tình, Rock, EDM).
4. **Chỉ ca sĩ solo.** Không đưa nhóm nhạc / ban nhạc / duo (tránh 1 người bị tính 2 lần).
5. **Không bịa số liệu:** không ghi lượt nghe, lượt xem hay thứ hạng cụ thể nếu không kiểm chứng được.

Phương pháp: kết hợp nhiều tín hiệu, **không dựa vào một bảng xếp hạng duy nhất** — Spotify/Apple Music
(monthly listeners, độ dày discography, độ phủ playlist); Wikipedia/Wikidata; chart Zing MP3 /
Billboard Vietnam (khi có dữ liệu công khai); lượt xem MV official trên YouTube (mức chung, không lấy
con số cụ thể); độ nhận biết chung trong công chúng Việt Nam qua nhiều năm.

> **⚠️ "Top" ở đây là ước lượng tổng hợp từ các nguồn trên, KHÔNG phải bảng xếp hạng chính thức duy nhất.**
> Thứ tự 1–100 là cách sắp xếp theo nhóm (demo trước, rồi theo dòng nhạc / thế hệ) để tiện theo dõi và crawl,
> **không phải thứ hạng 1 là hay nhất / nghe nhiều nhất**. Không dùng thứ tự này để khẳng định
> "ca sĩ A hơn ca sĩ B".

Trường hợp phân vân đã xử lý (theo `top100-list.md` mục 4): ca sĩ hải ngoại GIỮ nếu repertoire tiếng Việt
vẫn được nghe nhiều tại Việt Nam; ca sĩ đã mất CHỈ GIỮ nếu catalogue vẫn được nghe/stream nhiều
(trong danh sách chỉ có Phi Nhung); một người hai nghệ danh thì chỉ lấy 1 mục (1 "Trung Quân" là
Trung Quân Idol, 1 "Anh Tú" là Anh Tú Atus); rapper có sản phẩm chính thức GIỮ; ca sĩ gây tranh cãi
nhưng vẫn được nghe nhiều thì GIỮ theo tiêu chí "được nghe nhiều", không đánh giá đạo đức trong file này.

## 3. Nguồn — thứ tự ưu tiên

Thứ tự ưu tiên khi xác minh một field (theo thiết kế dự án + thực hành của các batch):

1. **VCPMC / Cục Bản quyền tác giả** — cho tác giả/quyền của bài hát.
2. **Spotify Web API** — metadata bản ghi, ISRC, Spotify ID (ca sĩ + track).
3. **MusicBrainz** — MBID ca sĩ, recording ID, ISRC, duration.
4. **Wikidata / Wikipedia (vi/en)** — tên thật, ngày sinh, nhạc sĩ, năm, album.
5. **Mô tả MV / kênh YouTube official** — nhạc sĩ, năm, xác nhận bản thu chính thức.
6. **Apple Music / iTunes Search API** — năm, album, duration, link.
7. **Báo chí uy tín** (VnExpress, Tuổi Trẻ, Thanh Niên, Kenh14, Znews…) — đối chiếu, không dùng làm nguồn duy nhất cho field quan trọng.

**Thực tế đạt được (xem UNVERIFIED.md):** mục 1 chưa tra được ở batch nào (không có kênh tra cứu công khai
phù hợp, không đăng nhập/bypass); mục 2 **không kết nối được ở hầu hết các batch** (Spotify API
`not_connected`, không có token/config) nên Spotify ID/ISRC thiếu hàng loạt — đây là **giới hạn hệ thống,
không phải dữ liệu không tồn tại**; mục 3 tra được một phần, hay gặp HTTP 503 ngắt quãng. Vì vậy độ phủ
ISRC/ISWC/Spotify/YouTube trong file tổng còn thấp (xem mục 5) và cần một đợt bổ sung có kết nối Spotify.

## 4. Định nghĩa confidence: high / medium / low

Áp dụng cho cả `confidence` (bản ghi) và `composer_confidence` (nhạc sĩ của bài):

| Mức | Nghĩa |
|---|---|
| **high** | Có **≥ 2 nguồn độc lập khớp nhau**, hoặc credit ghi rõ trực tiếp (mô tả MV official, tracklist album, bài Wikipedia có nguồn). |
| **medium** | Chỉ có **1 nguồn** độc lập, hoặc suy từ vai trò album/producer (producer ≠ composer — cần đối chiếu thêm). |
| **low** | Chỉ biết tên bài/tên người, thiếu năm/thời lượng/nhạc sĩ, hoặc nguồn yếu/mâu thuẫn chưa phân xử được. |

**Lưu ý quan trọng về tính nhất quán:** field `composer_confidence` chỉ được ghi ở **2/10 batch**
(batch 01-10 và 21-30); 8 batch còn lại để `null` (300/380 bài). Các batch khi báo cáo "% nhạc sĩ high"
đã dùng định nghĩa **không thống nhất** (xem mục 6): đa số dùng `confidence` của bài hát, riêng batch 31-40
dùng "credit nhạc sĩ ghi rõ" (3/40 = 7,5%). Vì vậy con số "% nhạc sĩ high" trong file tổng (mục 5) được
tính theo **một định nghĩa duy nhất** (`composer_confidence == 'high'`), và đi kèm con số "% bài có ghi tên
nhạc sĩ" để không đánh giá sai chất lượng dữ liệu.

## 5. Số liệu phủ THẬT — đếm bằng script từ file tổng (không lấy từ báo cáo batch)

Đếm lại độc lập từ `singers.json` / `songs.json` / `edges.json` sau khi gộp
(script đếm + kiểm chứng: đếm từ file tổng, không đếm từ báo cáo batch).

### Tổng quan

| Chỉ số | Số thật |
|---|---|
| Ca sĩ | **100** (không trùng `stage_name`, ID `singer-001`…`singer-100` khớp số thứ tự top100) |
| Bài hát unique | **380** (từ 389 bản ghi batch; gộp 9 nhóm trùng, tách 1 nhóm trùng tên thành 2 bài khác nhau — xem mục 7) |
| Lượt gắn ca sĩ–bài (Top 100) | **408** = 406 edge `performed_by` + 2 edge `featured_on` |
| Tổng edge | **630** (từ 735 edge thô; 105 edge không đưa vào file tổng — xem mục 7) |
| Ca sĩ có ≥ 3 bài (đếm qua edge `performed_by`) | **100/100** (ít nhất 3, nhiều nhất 6 bài/ca sĩ) |
| Bài dùng chung ≥ 2 ca sĩ Top 100 | **27 bài** (xem danh sách mục 7) |
| Lượt gắn thêm nghệ sĩ ngoài Top 100 (ghi trong `songs[].singers`, không tạo node/edge) | 75 lượt, ở 65 bài |

### Phủ field — bài hát (mẫu số 380)

| Field | Có | % |
|---|---|---|
| Có tên nhạc sĩ (`composers` non-empty) | 345 | **90,8%** |
| Nhạc sĩ `composer_confidence == 'high'` | 62 | **16,3%** (medium 12, low 6, **null 300** — 8/10 batch không ghi field này) |
| Bài hát `confidence == 'high'` | 213 | 56,1% (medium 159, low 8) |
| Có năm phát hành | 322 | **84,7%** |
| Có ISRC | 31 | **8,2%** |
| Có ISWC | 0 | **0%** |
| Có YouTube official URL | 39 | **10,3%** |
| Có Spotify track URL | 7 | 1,8% |
| Có Apple Music URL | 96 | 25,3% |
| Có duration | 163 | 42,9% |
| Có lyric URL | 12 | 3,2% |
| Chưa có tên nhạc sĩ (`composers` trống) | 35 | 9,2% |
| Chưa có năm | 58 | 15,3% |

### Phủ field — ca sĩ (mẫu số 100)

| Field | Có | % |
|---|---|---|
| Có Spotify artist ID | 24 | **24,0%** |
| Có MusicBrainz ID | 56 | 56,0% |
| Có Wikidata ID | 67 | 67,0% |
| Có ảnh (`image_url`) | 36 | 36,0% — toàn bộ 36 đều là ảnh Wikimedia Commons |
| Có ảnh **và** đã biết giấy phép (`image_license` non-null) | 16 | 16,0% (20 ảnh còn lại: có URL file Commons nhưng **chưa rà license từng file** — cần rà trước khi hiển thị/hotlink công khai) |
| Có tên thật | 100 | 100% |
| Có ngày sinh | 99 | 99% (thiếu: Noo Phước Thịnh — chỉ biết sinh 18/12, chưa rõ năm) |
| `confidence == 'high'` | 81 | 81% (medium 19) |

### ⚠️ Kết luận thẳng: CHƯA đạt chuẩn "100% bài có nhạc sĩ + năm có nguồn"

- **35/380 bài (9,2%) chưa có tên nhạc sĩ**, 58/380 bài (15,3%) chưa có năm.
- Chỉ **16,3%** bài có nhạc sĩ ở mức `high` theo định nghĩa chặt (credit ghi rõ / ≥ 2 nguồn);
  nhưng con số này bị kéo thấp vì 8/10 batch không ghi field `composer_confidence` — **không đồng nghĩa
  83,7% còn lại đều kém**. Chỉ số so sánh được là: 90,8% bài đã ghi tên nhạc sĩ, 56,1% bài ở `confidence high`.
- ISRC chỉ 8,2%, ISWC 0%, YouTube official chỉ 10,3%, Spotify track URL chỉ 1,8% — chủ yếu do
  **Spotify API chưa kết nối** ở hầu hết các batch, không phải do bài hát không có các mã/link này.
- Cần một đợt bổ sung: kết nối Spotify → lấy Spotify ID ca sĩ/track + ISRC + duration + album;
  tra lại MusicBrainz khi hết 503; tra VCPMC cho nhạc sĩ các bài bolero/trữ tình cũ.

## 6. Số liệu từng batch — đối chiếu báo cáo batch với đếm thật

Đếm lại từ file gốc từng batch, cùng một định nghĩa cho mọi batch (ISRC/YouTube/composers/year theo field;
`compConfHigh` = số bài có `composer_confidence == 'high'`; `songConfHigh` = số bài có `confidence == 'high'`).

| Batch | Bài | ISRC | YouTube | Có nhạc sĩ | compConf high | Bài conf high | Có năm | Ca sĩ có Spotify ID | Có ảnh |
|---|---|---|---|---|---|---|---|---|---|
| 01-10 | 40 | 16 (40,0%) | 1 (2,5%) | 38 (95,0%) | 38 | 30 (75,0%) | 40 (100%) | 5/10 | 10/10 |
| 11-20 | 40 | 3 (7,5%) | 1 (2,5%) | 38 (95,0%) | 0 | 16 (40,0%) | 40 (100%) | 9/10 | 0/10 |
| 21-30 | 40 | 12 (30,0%) | 11 (27,5%) | 36 (90,0%) | 24 | 24 (60,0%) | 40 (100%) | 8/10 | 9/10 |
| 31-40 | 40 | 0 | 3 (7,5%) | 40 (100%) | 0 | 22 (55,0%) | 35 (87,5%) | 0/10 | 6/10 |
| 41-50 | 42 | 0 | 6 (14,3%) | 30 (71,4%) | 0 | 17 (40,5%) | 40 (95,2%) | 0/10 | 4/10 |
| 51-60 | 40 | 0 | 0 | 29 (72,5%) | 0 | 8 (20,0%) | 25 (62,5%) | 0/10 | 0/10 |
| 61-70 | 35 | 0 | 8 (22,9%) | 33 (94,3%) | 0 | 25 (71,4%) | 35 (100%) | 0/10 | 0/10 |
| 71-80 | 40 | 0 | 2 (5,0%) | 37 (92,5%) | 0 | 20 (50,0%) | 24 (60,0%) | 2/10 | 7/10 |
| 81-90 | 36 | 0 | 4 (11,1%) | 35 (97,2%) | 0 | 27 (75,0%) | 17 (47,2%) | 0/10 | 0/10 |
| 91-100 | 36 | 0 | 3 (8,3%) | 36 (100%) | 0 | 30 (83,3%) | 33 (91,7%) | 0/10 | 0/10 |

**Đối chiếu với số "% nhạc sĩ high" các batch đã báo:** đa số batch báo đúng bằng `songConfHigh`
(11-20: 40%; 21-30: 60%; 51-60: 20%; 61-70: 71,4%; 71-80: 50%; 81-90: 75%; 91-100: 83,3%;
01-10: 95% = `compConfHigh`). Hai ngoại lệ: **31-40 báo 7,5%** — đó là số bài có **credit nhạc sĩ ghi rõ**
(3 bài: "Bigcityboi", "Người Lạ Ơi", "Mượn Rượu Tỏ Tình", xem UNVERIFIED batch 31-40 §6), trong khi
`songConfHigh` của batch này là 55%; **41-50 báo 33%** (~14/42) — không khớp `songConfHigh` 40,5% (17/42)
cũng không khớp `compConfHigh` (0) — cách tính của batch này không tái hiện được từ file JSON, ghi nhận
ở đây để coordinator hỏi lại batch 41-50 nếu cần. File tổng không dùng các con số báo cáo này mà đếm lại
theo một định nghĩa duy nhất (mục 5).

**Batch yếu nhất** (theo % nhạc sĩ có tên, % ISRC/YouTube, % có năm, % ảnh/Spotify ID ca sĩ):

- **Yếu nhất tổng thể: batch 51-60** — ISRC 0%, YouTube 0%, chỉ 62,5% bài có năm, 0/10 ca sĩ có ảnh,
  0/10 có Spotify ID, bài `confidence high` thấp nhất (20,0%), nhạc sĩ trống 11/40 bài (nhiều thứ hai).
- **Batch 81-90** — chỉ 47,2% bài có năm (thấp nhất), ISRC/Spotify/ảnh 0, 19/36 bài trống năm.
- **Batch 41-50** — nhạc sĩ trống nhiều nhất (12/42 bài, 28,6%), cả 10 ca sĩ đều trống Spotify ID /
  MusicBrainz ID / Wikidata ID / ISRC / duration.
- **Batch 71-80** — chỉ 60,0% bài có năm (16/40 trống, chủ yếu ca khúc sáng tác trước thời streaming).
- 7/10 batch có ISRC 0% (31-40, 41-50, 51-60, 61-70, 71-80, 81-90, 91-100); 5/10 batch có 0/10 ảnh
  (11-20, 51-60, 61-70, 81-90, 91-100); 6/10 batch có 0/10 Spotify ID ca sĩ.
- Batch mạnh nhất về phủ: **01-10** (ISRC 40%, ảnh 10/10) và **21-30** (ISRC 30%, YouTube 27,5% cao nhất).

## 7. Cách gộp — quy tắc đã áp dụng (để kiểm chứng lại)

### ID chuẩn

- Ca sĩ: `singer-001`…`singer-100` theo số thứ tự trong `top100-list.md` (batch dùng ID trùng nhau giữa
  các batch — ví dụ `singer-001` ở cả batch 01-10 và batch 21-30 — nên ID batch **không** giữ nguyên).
  Mỗi ca sĩ giữ nguyên toàn bộ field của batch, cộng thêm `top100_no` và `batch` (batch nguồn).
- Bài hát: `song-001`…`song-380` theo thứ tự xuất hiện (batch 01-10 → 91-100, theo thứ tự trong file batch).
  Mỗi bản ghi giữ `batches` (các batch nguồn) và `batch_song_ids` (ID gốc trong batch, có thể `null`).
- Edge: `edge-001`…`edge-630`, schema chuẩn `{id, source, target, relationship, evidence, sources,
  original_type, batch}`; `source`/`target` là ID chuẩn (`singer-XXX` / `song-XXX`).

### Khử trùng bài hát

- Gom theo tên bài chuẩn hoá (bỏ dấu, chữ thường). Trong cùng một nhóm tên, **chỉ tách ra khi nhạc sĩ
  của hai bản ghi disjoint và đều non-empty** (hai bài khác nhau trùng tên).
- **9 nhóm đã gộp thành 1 bản ghi** (giữ 1 bản ghi bài, `singers[]` gồm đủ ca sĩ, `sources[]` hợp nhất,
  `composers[]`/`lyricists[]` hợp nhất; field vô hướng lấy giá trị non-null đầu tiên theo thứ tự batch,
  mâu thuẫn ghi vào `notes` của bản ghi + UNVERIFIED.md):
  "Anh Nhà Ở Đâu Thế" (AMEE, B Ray); "Có Chàng Trai Viết Lên Cây" (Hà Anh Tuấn, Phan Mạnh Quỳnh);
  "Có phải em mùa thu Hà Nội" (Hồng Nhung, Thu Phương); "Còn Thương Rau Đắng Mọc Sau Hè"
  (Hương Lan, Hồ Văn Cường); "Người Lạ Ơi" (Karik, Orange); "Nơi Tình Yêu Bắt Đầu"
  (Bằng Kiều, Bùi Anh Tuấn); "Sa Mưa Giông" (Hương Lan, Hồ Văn Cường); "Simple Love"
  (Obito, Seachains); "vaicaunoicokhiennguoithaydoi" (Grey D, tlinh).
- **1 nhóm đã tách thành 2 bài khác nhau:** "Chưa Bao Giờ" — bản của Trung Quân (nhạc sĩ Tiên Tiên, 2015)
  và bản của Thu Phương (nhạc sĩ Việt Anh, chưa rõ năm) là hai sáng tác khác nhau trùng tên.
- Mâu thuẫn giá trị khi gộp (ghi trong `notes` từng bản ghi + UNVERIFIED.md): năm "Có Chàng Trai Viết
  Lên Cây" 2019 vs 2020 (giữ 2019); năm "Có phải em mùa thu Hà Nội" 1996 vs 1997 (giữ 1996);
  năm "Còn Thương Rau Đắng Mọc Sau Hè" 1974 (sáng tác) vs 2016 (bản thu Hồ Văn Cường) (giữ 1974);
  album/duration/link Apple khác nhau giữa hai bản "Có phải em mùa thu Hà Nội"; album "Có Chàng Trai
  Viết Lên Cây": "Truyện Ngắn" vs "OST Mắt Biếc (2019)".
- **27 bài dùng chung ≥ 2 ca sĩ Top 100** (theo edge `performed_by`): Có Chàng Trai Viết Lên Cây
  (Hà Anh Tuấn, Phan Mạnh Quỳnh); vaicaunoicokhiennguoithaydoi (Grey D, tlinh); Ánh Mắt Biết Cười
  (Quang Hùng MasterD, Tăng Duy Tân); Mưa Tháng Sáu (Grey D, Trung Quân, Văn Mai Hương); Ghen (Erik, Min);
  Nếu ta không may (Anh Tú Atus, LyLy); Dân chơi sao phải khóc (Andree Right Hand, Rhyder);
  Cho Mình Em (Binz, Đen); Người lạ ơi (Karik, Orange); Khu Tao Sống (Karik, Wowy);
  Hai Thế Giới (Karik, Wowy); Simple Love (Obito, Seachains); Buồn Hay Vui (MCK, Obito);
  Nơi Tình Yêu Bắt Đầu (Bùi Anh Tuấn, Bằng Kiều); Xe Anh Đến Đâu Em Theo Đến Đó (Dương Hoàng Yến, Đạt G);
  Có phải em mùa thu Hà Nội (Hồng Nhung, Thu Phương); Chim trắng mồ côi (Cẩm Ly, Đan Trường);
  Duyên Phận (Lệ Quyên, Như Quỳnh); Đập Vỡ Cây Đàn (Quang Lê, Đan Nguyên);
  Phải Lòng Con Gái Bến Tre (Phi Nhung, Quang Lê); Thói Đời (Chế Linh, Đan Nguyên);
  Thành Phố Buồn (Chế Linh, Đan Nguyên); Xin Làm Người Xa Lạ (Chế Linh, Đan Nguyên);
  Không Giờ Rồi (Như Quỳnh, Trường Vũ); Còn thương rau đắng mọc sau hè (Hương Lan, Hồ Văn Cường);
  Sa mưa giông (Hương Lan, Hồ Văn Cường); Đoạn Cuối Tình Yêu (Chế Linh, Thanh Tuyền).

### Chuẩn hoá edge

- 10 batch dùng **5 schema edge khác nhau** (`relationship`/`type`+`relation`/`from`-`to`/`source`-`target`,
  endpoint là ID nội bộ batch, slug, số thứ tự `song-NN`, hoặc tên bài/ca sĩ). Tất cả được quy về một
  schema (mục 7, đầu mục) và endpoint được phân giải về ID chuẩn; `original_type` giữ lại giá trị gốc
  của batch, `batch` ghi batch nguồn.
- Ánh xạ quan hệ: `performs` → `performed_by`; `feat`/`duet`/`feat_with`/`collaboration` (ca sĩ–ca sĩ)
  → `collaborated_with`; `feat` (ca sĩ→bài) → `featured_on`; `same_composer_song` /
  `song-song-same-composer` → `same_composer` (bài–bài); `singer-song-composer` → `composed` (ca sĩ→bài);
  `singer-singer-composer-for` → `composed_for`; `singer-mentor-singer` → `mentored`;
  `same_band_Quả Dưa Hấu` → `same_band`; `same_song` (ca sĩ–ca sĩ) → `same_song`;
  `shared_collaborator` giữ nguyên; `same_composer` ca sĩ–ca sĩ (cùng nhạc sĩ, không phải cùng bài)
  → `shared_composer` (mới, 6 edge). Edge `same_song_different_singer` (bài→chính nó sau khi gộp)
  được bỏ vì việc gộp đã ghi nhận trong `singers[]` của bài.
- **105/735 edge thô không vào file tổng** (ghi chi tiết trong UNVERIFIED.md mục 3):
  98 edge có đầu mút là nghệ sĩ **ngoài Top 100** (52 người: B Ray, Mr. Siro, Touliver, Chillies, Da LAB,
  Wxrdie, OnlyC, K-ICM, Masew, Xuân Hinh, Negav, Marzuz, …) — các edge này không có node đích trong
  file tổng nên không giữ; thông tin feat/collab của họ **vẫn giữ trong `songs[].singers`** (75 lượt gắn);
  5 edge trùng (gộp `sources[]` vào edge đã có); 1 edge sai của batch (LyLy → Lou Hoàng, xem UNVERIFIED);
  1 edge tự trỏ sau khi gộp bài trùng tên.
- **2 trường hợp hiệu chỉnh có bằng chứng rõ ràng** (ghi trong UNVERIFIED.md):
  (a) edge batch 11-20 "Hòa Minzy → Tăng Duy Tân" ghi `same_composer` nhưng evidence viết
  "Tăng Duy Tân sáng tác 'Bật Tình Yêu Lên' cho Hòa Minzy" → đổi chiều thành
  `composed_for` Tăng Duy Tân → Hòa Minzy;
  (b) `singer_stage_names` của batch 41-50 ghi nhầm nhạc sĩ LyLy thành ca sĩ thể hiện ở 2 bài
  ("Anh nhà ở đâu thế", "Không sao mà, em đây rồi") → đã bỏ LyLy khỏi `singers[]` của 2 bài này
  (LyLy vẫn giữ trong `composers[]`); "Anh Tú" (viết tắt trong batch 21-30) → "Anh Tú Atus" ở 4 bài.
- **2 bài không có edge `performed_by` tới ca sĩ Top 100** (ca sĩ chính nằm ngoài Top 100, chỉ feat/sáng
  tác bởi người trong Top 100): "Ex's Hate Me" (B Ray ft. AMEE — AMEE có edge `featured_on`) và
  "Không sao mà, em đây rồi" (Suni Hạ Linh ft. Lou Hoàng theo `singers[]` của batch; LyLy sáng tác —
  vai trò của Lou Hoàng trong bài này còn mâu thuẫn, xem UNVERIFIED.md). Cả 2 bài vẫn giữ trong file
  tổng vì đã có trong batch; không tự xoá dữ liệu batch.

### Edge theo quan hệ (630 edge)

`performed_by` 406 · `same_composer` 176 · `collaborated_with` 32 · `shared_composer` 6 ·
`featured_on` 2 · `composed_for` 2 · `composed` 2 · `shared_collaborator` 1 · `same_band` 1 ·
`same_song` 1 · `mentored` 1. Mọi edge đều có `evidence` non-empty; không có edge trùng
`(source, target, relationship)`; mọi đầu mút đều tồn tại trong `singers.json`/`songs.json`.

### Kiểm chứng đã chạy

- `python3 -m json.tool` cho cả 30 file JSON batch: hợp lệ.
- Đếm lại từ file tổng: đúng 100 ca sĩ không trùng; mỗi ca sĩ 3–6 bài qua `performed_by`;
  380 bài unique; 630 edge; CSV đọc lại được (101 / 381 dòng kể cả header).
- Mọi link trong file tổng đều là link đã có trong `sources[]` của batch (702 URL nguồn khác nhau) —
  không thêm link mới.

## 8. Việc cần làm tiếp (ngoài phạm vi gộp)

1. Coordinator/John chốt các mâu thuẫn trong UNVERIFIED.md mục 2 (tên thật Chế Linh, Trung Quân,
   Hiền Hồ, Vũ., Tuấn Ngọc, LyLy…; các bài trong danh sách gốc bị thay thế).
2. Kết nối Spotify rồi bổ sung: Spotify ID 76 ca sĩ còn thiếu, ISRC (349 bài), duration (217 bài),
   Spotify/Apple link, album — ưu tiên batch 51-60 và 81-90 (yếu nhất).
3. Tra MusicBrainz/Wikidata cho 44 ca sĩ chưa có MBID, 33 ca sĩ chưa có Wikidata ID; rà license
   20 ảnh Commons chưa rõ giấy phép.
4. Bổ sung nhạc sĩ cho 35 bài trống + năm cho 58 bài trống; ghi `composer_confidence` cho 300 bài
   đang `null` để số "% nhạc sĩ high" có ý nghĩa trở lại.
5. Bổ sung YouTube official URL cho 341 bài còn thiếu (mở kênh official từng ca sĩ, không đoán video ID).
