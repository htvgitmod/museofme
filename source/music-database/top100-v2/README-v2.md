# Cơ sở dữ liệu nhạc Việt — Top 100, Vòng 2: Enrich (15/11/2026)

Làm giàu 380 bài từ vòng 1 (`../top100/`, giữ nguyên, không ghi đè) bằng các API
công khai **không cần key, không nối Spotify**, theo chuỗi đã test thật 15/11.

## Phương pháp kéo

Thứ tự, cho mỗi bài (ca sĩ chính = ca sĩ Top-100 đầu tiên trong `singers[]`):

1. **Deezer** — `GET https://api.deezer.com/search?q={ca sĩ} {tên bài}`
   Không cần key, ~50 req/5s (sleep 0,2s). Trả ISRC, album, duration, preview,
   link Deezer. Chỉ nhận khi tên bài + ca sĩ khớp (chuẩn hóa không dấu, map đ→d
   — lưu ý: `Đ` không tách dấu được bằng NFD nên nhiều batch suýt khớp sai).
   Phân biệt bản gốc vs remix/live: remix có ISRC khác, ghi vào `title_version`.
2. **iTunes Search** — `GET https://itunes.apple.com/search?term={ca sĩ} {tên bài}&media=music&entity=song&limit=3&country=VN`
   Không cần key, ~20 req/phút (sleep 3s). Trả releaseDate, album
   (collectionName), Apple Music URL, preview. **iTunes VN không trả trường
   ISRC** — mọi ISRC đều từ Deezer; bài chỉ khớp iTunes thì không có ISRC để
   lookup bước 3.
3. **Credits.fm** — **chỉ lookup theo ISRC**: `GET https://api.credits.fm/v1/isrc/{ISRC}`
   Không cần key, 30 lookup/phút (sleep 2s). Trả ISWC, songwriters (tên + IPI +
   role), release_date, UPC, nguồn MLC/MusicBrainz/CISAC. **Không dùng
   `/v1/search` (trả 503).**
4. **MusicBrainz** — chỉ khi cần MBID, 1 req/s, bắt buộc User-Agent định danh.
   Thực tế vòng 2 hầu như không cần dùng (vòng 1 đã có MBID cho nhiều bài).

Quy tắc khớp và ghi chép:
- ISRC/ISWC/nhạc sĩ/ngày chỉ ghi khi API trả về đúng bài đó. Không khớp thì
  để trống + ghi lý do vào UNVERIFIED.
- **Không sửa đè dữ liệu vòng 1**: các trường gốc (`composers`, `year`,
  `album`) giữ nguyên; giá trị API nằm ở trường riêng (`deezer_album`,
  `apple_release_date`, `credits_songwriters`). Mâu thuẫn ghi vào
  `batches/batch-*/conflicts.md` và tổng hợp ở UNVERIFIED-v2.md mục 7.
- **Không điền năm mới vào trường `year`**: `apple_release_date` hay là ngày
  tái phát hành/tuyển tập nên chỉ ghi làm bằng chứng đối chiếu.
- Không đoán link YouTube, không chép lời bài hát.
- Tôn trọng rate limit từng API, cache response thô trong `batches/batch-*/raw/`,
  gặp 429/503 thì backoff và ghi lại, không retry dồn dập.
- Tên nhạc sĩ Credits.fm trả dạng HỌ TÊN không dấu, đảo thứ tự (vd `HUNG KHAC`
  = Khắc Hưng, `QUYNH PHAN MANH` = Phan Mạnh Quỳnh) — các batch đối chiếu theo
  tập token, không tính đó là mâu thuẫn.

## Cách chạy / gộp lại

- Mỗi batch có script riêng: `batches/batch-*/enrich.py` (+ `raw/` cache).
- Gộp 10 batch: `python3 merge.py` trong thư mục này. Script gộp kiểm tra:
  đủ 380 id duy nhất, không thiếu/không thừa so với vòng 1.
- Ghi chú gộp (MERGE_NOTES):
  - `song-115` Nếu ta không may và `song-118` Dân chơi sao phải khóc bị trùng
    ở cả batch-03 và batch-05 (batch-03 lấy theo ca sĩ bất kỳ trong bài thay vì
    ca sĩ Top-100 đầu tiên) — 2 bản sao giống hệt nhau, giữ 1 bản, đã log trong
    `merge-stats.json`.
  - `song-086` Ghen (Min, Erik, Khắc Hưng) bị batch-03 sót — coordinator enrich
    trực tiếp 15/11: Deezer ISRC `SGUM72400059` (album Ghen, 247s), iTunes
    release 2017-05-23, Credits.fm ISWC `T-301049471-6`, nhạc sĩ HUNG KHAC
    IPI 00690117845 (= Khắc Hưng, khớp vòng 1), MLC GA0QE5.

## Số liệu phủ — TRƯỚC (vòng 1) vs SAU (vòng 2), đếm thật bằng script

Tổng 380 bài. YouTube official giữ nguyên vòng 1: 39/380 (10,3%) — vòng 2
không tra YouTube.

| Chỉ số | Vòng 1 | Vòng 2 | Thay đổi |
|---|---|---|---|
| ISRC | 31 (8,2%) | **320 (84,2%)** | +289 |
| ISWC | 0 (0%) | **211 (55,5%)** | +211 |
| Apple Music URL | 96 (25,3%) | **343 (90,3%)** | +247 |
| Deezer URL | 0 | **318 (83,7%)** | +318 |
| Duration | 163 (42,9%) | **348 (91,6%)** | +185 |
| Có nhạc sĩ (vòng 1 hoặc Credits.fm) | 345 (90,8%) | **362 (95,3%)** | +17 |
| Có năm (trường year vòng 1) | 322 (84,7%) | 322 (84,7%) | 0 — không điền năm mới |
| Confidence | — | high 264 / medium 87 / none 29 | — |

Theo batch (ISRC / ISWC / Apple):

| Batch | Bài | ISRC | ISWC | Apple |
|---|---|---|---|---|
| 01 (1–10) | 39 | 38 | 26 | 39 |
| 02 (11–20) | 40 | 39 | 24 | 38 |
| 03 (21–30) | 40 | 31 | 23 | 34 |
| 04 (31–40) | 41 | 31 | 13 | 35 |
| 05 (41–50) | 39 | 33 | 15 | 34 |
| 06 (51–60) | 40 | 34 | 27 | 37 |
| 07 (61–70) | 34 | 31 | 23 | 33 |
| 08 (71–80) | 39 | 29 | 25 | 35 |
| 09 (81–90) | 34 | 29 | 18 | 30 |
| 10 (91–100) | 35 | 26 | 17 | 29 |

Batch yếu nhất vòng 2: batch 04 (ISWC 13/41), batch 05 (ISWC 15/39) —
phần lớn do Credits.fm trả `iswc: null` cho ISRC đã khớp.

## File đầu ra

- `songs-enriched.json` — đủ 380 bài, giữ nguyên mọi trường vòng 1 + trường
  enrich mới (`isrc`, `iswc`, `deezer_id`, `deezer_url`, `deezer_album`,
  `apple_music_url`, `apple_release_date`, `credits_songwriters[]`,
  `credits_source`, `isrc_source`, `iswc_source`, `enrichment_confidence`,
  `conflicts[]`, `title_version` khi là bản remix/live).
- `songs-enriched.csv` — cùng dữ liệu, UTF-8 + BOM.
- `singers.json` — copy từ vòng 1 (không đổi).
- `merge.py` + `merge-stats.json` — script gộp và số liệu đếm thật.
- `UNVERIFIED-v2.md` — bài vẫn thiếu ISRC/ISWC/nhạc sĩ/năm/Apple sau vòng 2.
- `batches/batch-01/` … `batch-10/` — file enrich từng batch + `raw/` cache
  response + `conflicts.md` + `UNVERIFIED-batch-*.md` + `enrich.py`.

## Chưa đạt — đừng nói "đã chuẩn hết"

- Thiếu ISRC: **60/380** — Deezer/iTunes không có đúng bản thu của đúng ca sĩ
  (nhạc xưa/bolero, rap underground, Anh Tú Atus, bài song ca chỉ có bản solo).
- Thiếu ISWC: **169/380** — chủ yếu Credits.fm trả `iswc: null` cho ISRC đã
  khớp, hoặc không có ISRC để lookup.
- Thiếu nhạc sĩ (cả vòng 1 lẫn Credits.fm): **17/380** (đã sửa 1: song-231, xem
  "Sửa sau vòng 2" bên dưới). Thiếu năm: **57/380** (đã sửa 1: song-231).
- Confidence none (không enrich được gì mới): **29 bài** — liệt kê ở
  UNVERIFIED-v2.md mục 6.
- Mâu thuẫn mục 7 **đã chốt hết ngày 16/11/2026** — xem UNVERIFIED-v2.md mục 7
  (ISRC "Waiting for You" sửa sang VNA092201159; "Bên Trên Tầng Lầu" chốt năm
  2022; "Bình Minh Sẽ Mang Em Đi" chốt năm 2001 + nhạc sĩ; LyLy chốt tên thật
  Nguyễn Hoàng Ly; Credits.fm map sai ISRC ở Dấu Mưa / Bình Minh đã ghi rõ).

## Sửa sau vòng 2 — 16/11/2026 (chỉ sửa local, chưa đưa lên GitHub)

7 mâu thuẫn ở UNVERIFIED-v2.md mục 7 đã được kiểm chứng lại bằng Deezer API,
Credits.fm API và Wikipedia rồi sửa trực tiếp vào `songs-enriched.json` /
`songs-enriched.csv` (và `singers.json`/`singers.csv` cho LyLy). Số liệu sau sửa,
đếm lại bằng script: ISRC 320, ISWC 211 (không đổi); có nhạc sĩ 362 → **363**;
có năm 322 → **323**; confidence high 264 → **266**, medium 87 → **85**, none 29.
File vòng 1 `top100/singers.json` + `singers.csv` cũng được sửa (chỉ 2 dòng LyLy,
giữ nguyên format) — khi đưa v2 lên GitHub thì đưa kèm 2 file ca sĩ này.
