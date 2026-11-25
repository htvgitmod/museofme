# GOAL — Các thí nghiệm tâm lý nổi tiếng (tra cứu tiếng Việt)

- **Deliverable:** 1 file HTML duy nhất, tự chứa, offline: `~/workspace/tam-ly-thi-nghiem/tam-ly-thi-nghiem.html`
- **Data nguồn:** `~/workspace/tam-ly-thi-nghiem/data.json` + `data.md` cùng thư mục
- **GitHub (quy tắc John bổ sung 25/11 23:34, áp dụng khi project hoàn thiện + QA xong):** lập folder riêng `source/tam-ly-thi-nghiem/` trên repo htvgitmod/museofme, đưa CẢ data raw (md/json) + bản final (HTML) + ảnh đã cào (giữ nguyên cấu trúc thư mục ảnh) vào folder đó. Upload bằng trình duyệt qua Upload Files với tài khoản GitHub đã lưu htvgitmod (không hỏi OAuth lại), TUYỆT ĐỐI KHÔNG dùng trình sửa web GitHub cho file >1 MB, file trùng tên thì upload đè trực tiếp. Xong kiểm chứng live (mở file trên github.com và qua GitHub Pages) rồi báo số commit trong báo cáo bàn giao.
- **Số mục tối thiểu:** 50 thí nghiệm thật. Mục tiêu coordinator: **60 mục** (6 batch × 10). Làm hơn được thì hơn, miễn mục nào cũng thật, đủ trường, có nguồn.
- **Ngôn ngữ:** tiếng Việt toàn bộ giao diện + nội dung; giữ tên tiếng Anh gốc mỗi mục.

## Bộ trường bắt buộc mỗi mục
`id` (vd `tn-01`), `en_name`, `vi_name`, `researcher`, `year` (số, năm công bố/chạy thí nghiệm chính),
`field` (1 trong 6 lĩnh vực dưới), `controversy` (`Thấp`|`Trung bình`|`Cao`|`Rất cao`),
`method` (cách làm, 3–6 câu), `results` (kết quả, con số CHỈ khi có nguồn), `lesson` (bài học rút ra, 2–4 câu),
`controversy_text` (phần "Đang tranh cãi": ghi rõ thí nghiệm có bị nghi ngờ tái lập / đạo đức / phương pháp không; nếu không tranh cãi thì ghi "Ít tranh cãi — ..." với lý do ngắn, KHÔNG bỏ trống),
`sources` (≥2 link: Wikipedia EN bắt buộc + nguồn gốc/bài báo gốc hoặc nguồn uy tín khác),
`image` (object hoặc null — xem dưới), `verified` (true/false + ghi chú nếu có phần chưa kiểm chứng).

## 6 lĩnh vực (field)
- `Tam ly xa hoi` — hiển thị "Tâm lý xã hội"
- `Nhan thuc va Tri nho` — "Nhận thức & Trí nhớ"
- `Phat trien` — "Phát triển"
- `Hanh vi va Hoc tap` — "Hành vi & Học tập"
- `Cam xuc, Dong luc, Nhan cach` — "Cảm xúc, Động lực & Nhân cách"
- `Ra quyet dinh va Kinh te hanh vi` — "Ra quyết định & Kinh tế hành vi"

## Quy tắc dữ liệu (bắt buộc)
- Chỉ lấy từ nguồn kiểm chứng được: Wikipedia EN + nguồn gốc từng thí nghiệm (bài báo gốc / Britannica / APA / Simply Psychology chỉ là phụ, không thay nguồn gốc).
- KHÔNG bịa số, không bịa thí nghiệm. Số nào không tìm được nguồn thì BỎ số đó hoặc ghi rõ "chưa kiểm chứng" trong mục.
- Nguồn bị chặn (403/429) thì ghi rõ trong `verified`/ghi chú và làm tiếp phần kiểm chứng được.
- Tên tiếng Việt: dịch tự nhiên, đúng chuyên môn (vd Milgram = "Thí nghiệm vâng lời Milgram", Stanford = "Thí nghiệm nhà tù Stanford"), không dịch máy móc.
- Không trùng mục giữa các batch. Mỗi thí nghiệm chỉ xuất hiện 1 lần.

## Ảnh (bắt buộc kiểm tra, không bắt buộc có)
- Chỉ ảnh tự do: public domain / CC-BY / CC-BY-SA, ƯU TIÊN Wikimedia Commons.
- Mỗi ảnh ghi: `url` (link file Commons trực tiếp), `page` (link trang file Commons), `caption`, `license`, `author` (nếu có).
- Ưu tiên: chân dung nhà nghiên cứu (ảnh cũ public domain) hoặc sơ đồ thí nghiệm.
- Không có ảnh tự do xác minh được → `image: null`, KHÔNG dùng ảnh bản quyền không rõ nguồn, KHÔNG hotlink ảnh random.
- Ảnh đã duyệt sẽ được TẢI VỀ local vào `~/workspace/tam-ly-thi-nghiem/images/<id>.<ext>` (giữ nguyên cấu trúc thư mục khi upload GitHub); file HTML tham chiếu ảnh local tương đối, data JSON vẫn giữ link Commons gốc + giấy phép.

## Thiết kế (chuẩn Letter, tham khảo từ điển Vibe Coding)
- Nền giấy ấm (#F7F1E3 / #FBF6EC), serif Alegreya cho nội dung, Caveat cho tiêu đề chính / tiêu đề mục, accent terracotta #B85C38.
- Header: tên trang, mô tả 1–2 dòng, thống kê (số mục, số lĩnh vực, số mục tranh cãi cao).
- Controls sticky: ô tìm kiếm (không dấu — normalize NFD, bỏ dấu), lọc lĩnh vực (select + chip), lọc mức tranh cãi, nút "Ngẫu nhiên", đếm kết quả "Hiển thị X / 60".
- Card mỗi mục: tiêu đề EN + VI, tag lĩnh vực + mức tranh cãi (màu khác nhau), nhà nghiên cứu + năm, ảnh (nếu có, kèm credit + license nhỏ), các mục Cách làm / Kết quả / Bài học / Đang tranh cãi (hộp riêng, nền khác), link nguồn.
- 1 file HTML duy nhất, tự chứa (CSS+JS inline, font dùng system serif fallback nếu offline — KHÔNG phụ thuộc CDN bắt buộc; có thể link Google Fonts nhưng trang vẫn đẹp khi offline).
- Responsive, đọc tốt trên mobile.

## QA trước bàn giao
- Đếm đủ ≥50 mục, mỗi mục đủ trường, không trùng id/tên EN.
- HTML 0 lỗi thẻ (kiểm tra bằng parser), tìm kiếm không dấu + lọc chạy thật trên trình duyệt.
- Báo cáo: đường dẫn, dung lượng, số mục, QA, danh sách "chưa kiểm chứng".

## Phân batch (60 mục)
- **Batch A — Tâm lý xã hội:** tn-01 Milgram, tn-02 Stanford Prison, tn-03 Asch, tn-04 Robbers Cave, tn-05 Festinger dissonance $1/$20, tn-06 Bystander Darley-Latané, tn-07 LaPiere 1934, tn-08 Pygmalion Rosenthal-Jacobson, tn-09 Good Samaritan, tn-10 Blue Eyes/Brown Eyes Jane Elliott.
- **Batch B — Nhận thức & Trí nhớ:** tn-11 Stroop, tn-12 Loftus misinformation, tn-13 Ebbinghaus, tn-14 Miller 7±2, tn-15 Wason selection, tn-16 Marshmallow Mischel, tn-17 Sperling iconic memory, tn-18 Bartlett War of the Ghosts, tn-19 Inattentional blindness (gorilla), tn-20 Loftus lost-in-the-mall false memory.
- **Batch C — Phát triển:** tn-21 Harlow khỉ, tn-22 Ainsworth Strange Situation, tn-23 Piaget bảo toàn, tn-24 Kohlberg Heinz, tn-25 Bandura Bobo doll, tn-26 Still Face Tronick, tn-27 Bowlby 44 thieves, tn-28 Baumrind parenting styles, tn-29 Sally-Anne false belief, tn-30 Meltzoff bắt chước trẻ sơ sinh.
- **Batch D — Hành vi & Học tập:** tn-31 Pavlov, tn-32 Skinner box, tn-33 Thorndike puzzle box, tn-34 Little Albert Watson, tn-35 Tolman cognitive map, tn-36 Seligman learned helplessness, tn-37 Garcia taste aversion, tn-38 Skinner superstition pigeons, tn-39 Little Peter Mary Cover Jones, tn-40 Lorenz imprinting.
- **Batch E — Cảm xúc, Động lực, Nhân cách:** tn-41 Schachter-Singer two-factor, tn-42 Dutton-Aron cầu treo, tn-43 Ekman biểu cảm khuôn mặt, tn-44 Zajonc mere exposure, tn-45 Deci động lực nội tại, tn-46 Schachter affiliation/anxiety, tn-47 Olds-Milner pleasure center, tn-48 Brickman lottery winners hedonic treadmill, tn-49 Csikszentmihalyi flow, tn-50 Rosenhan On Being Sane.
- **Batch F — Ra quyết định & Kinh tế hành vi:** tn-51 Kahneman-Tversky Asian disease framing, tn-52 Anchoring Tversky-Kahneman, tn-53 Endowment Thaler mug, tn-54 Linda conjunction fallacy, tn-55 Dunning-Kruger, tn-56 Bargh priming người già, tn-57 Power posing Cuddy, tn-58 Ego depletion Baumeister, tn-59 Hawthorne effect, tn-60 Bem precognition.
