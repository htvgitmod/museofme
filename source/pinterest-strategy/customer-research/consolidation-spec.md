# BẢN ĐẶC TẢ HỢP NHẤT — Dự án Pinterest: Home Decor / Small Space / Renter

**Ngày lập:** 19/11/2026 · **Người lập:** biên tập viên kiểm soát chất lượng (subagent) · **Mục đích:** một tài liệu duy nhất nói rõ file nào là chuẩn, file nào lỗi thời, mọi mâu thuẫn giữa các file và cách giải quyết từng cái — làm chuẩn để đối chiếu với file master HTML đang được dựng song song.
**Quy tắc:** bản này KHÔNG sửa bất kỳ file nguồn nào. Mọi quyết định ở mục 2 là đề xuất có lý do; chỉ những quyết định ghi "CHỜ JOHN" mới cần đáp án của anh. Số dòng trích dẫn là số dòng trong file local tại thời điểm rà (19/11/2026).

---

## 1. Bản đồ file

| # | File (đường dẫn tương đối trong `files/`) | Vai trò | Trạng thái | Còn dùng được? |
|---|---|---|---|---|
| 1 | `pinterest-12-month-strategy/pinterest-12-month-strategy.html` (v1, 11/11, 43.545 B) | Chiến lược 12 tháng gốc: 40 bài đầu (Splinter Method), mở rộng 148–160, lịch mùa vụ, SOP tuần, tiền theo quý, 10 board, 3 mẫu pin | **LỖI THỜI — đã bị v2 thay thế** về nội dung (persona, 40 bài verdict, mở rộng, pin). Vẫn là gốc lịch sử của các con số. | Chỉ tham khảo lịch sử + bảng tiền (v2 giữ nguyên tiền). Không lấy nội dung chiến lược từ đây nữa. |
| 2 | `pinterest-content-strategy-v2.html` (v2, 19/11, 65.907 B) | **Chiến lược chuẩn hiện tại**: 3 persona + 5 JTBD, 40 bài verdict, lộ trình 40 → 150, 5 mẫu pin T1–T5, 25 đối thủ, plan thực thi từng tháng, quy trình biên tập con người cho Raptive | **CHUẨN** (đã sửa đính chính Pinterest của The Tidy Renter, commit efc059a). Còn 3 lỗi nội bộ cần sửa khi làm master (xem C11, C5, C1). | Có — là xương sống của file master. |
| 3 | `customer-research/pinterest-customer-research-pack.html` (19/11, 54.416 B) | Gói nghiên cứu khách hàng tổng hợp: 3 persona, 5 JTBD, bản đồ nỗi đau, verdict 19 ý bài 1 + 40 bài, mục chưa kiểm chứng, nguồn | **CHUẨN** (bằng chứng gốc cho v2). Lưu ý: bảng verdict dùng tiêu đề v1 (xem C15). | Có — nguồn bằng chứng cho mọi quyết định nội dung. |
| 4 | `customer-research/competitors.md` (19/11, 46.942 B) | 25 đối thủ: 3 site lớn + 11 blog ngách + 11 blog nhỏ, bảng so sánh, bản đồ cạnh tranh | **CHUẨN** (đã sửa đính chính Pinterest của The Tidy Renter, commit b9f4e17). | Có. |
| 5 | `customer-research/pin-styles.md` (19/11, 38.288 B) | 6 layout, 5 mẫu pin T1–T5 có spec Canva (px), quy tắc chữ/màu/kích thước, bảng phân bổ 3 pin/bài | **CHUẨN, nhưng số ý bài 1 trong file đang lệch** (xem C5). | Có, sau khi đồng bộ số ý bài 1. |
| 6 | `customer-research/content-expansion.md` (19/11, 37.439 B) | Lộ trình mở rộng 40 → 150 (40 + 50 + 60), 24 tiêu đề gợi ý, cluster mới, hub/spoke, lịch mùa vụ | **CHUẨN** (đã tự hòa giải mốc 148/160 của v1 thành 150). Thiếu bài lighting (xem C4). | Có. |
| 7 | `competitor-playbook.html` (19/11, 37.924 B) | Tổng hợp teardown: copy gì (5 format), tránh gì (5 sai lầm), beat sheet, bản đồ gap từ khóa 40 bài, nước đi theo thứ tự | **CHUẨN** (mới nhất về đối thủ; chứa hộp đính chính Pinterest). Có 2 chỗ "19 ý" về bài 1 sẽ lỗi thời nếu John chốt 18 (dòng 100, 140 — xem C1; dòng 103 là số ý của bài 29, không liên quan). | Có — là tài liệu hành động, không phải danh sách. |
| 8 | `customer-research/teardown-tidy-renter.md` (19/11, 53.216 B) | Teardown The Tidy Renter: đọc toàn văn 18 guide, cấu trúc, Renter Audit, beat sheet, copy/tránh/chiếm | **CHUẨN** (nguồn của đính chính Pinterest @tidyrenter). Có 2 chỗ "19 ý" sẽ lỗi thời nếu John chốt 18 (xem C1). | Có. |
| 9 | `customer-research/teardown-niche-blogs.md` (19/11, 77.990 B) | Teardown 9 blog ngách: bài đã đọc, mạnh/yếu, khoảng trống, beat sheet, 5 format copy, 5 sai lầm, 5 khoảng trống | **CHUẨN**. Có 1 chỗ "19 ý" sẽ lỗi thời nếu John chốt 18 (xem C1). | Có. |
| 10 | `customer-research/teardown-big3-keyword-gaps.md` (19/11, 62.847 B) | Teardown Apartment Therapy / Spruce / Real Simple + bản đồ gap từ khóa 40 bài | **CHUẨN, trừ 1 ô stale** (dòng 187: "Tidy Renter không có Pinterest" — xem C2). | Có, sau khi sửa ô dòng 187. |
| 11 | `customer-research/reddit-renter-insights.md` (19/11, 39.844 B) | Nguồn gốc: lời người thuê thật (mirror r/AskReddit, nhật ký, review), verdict từng ý bài 1 (đánh số theo bản v1) | **CHUẨN — tài liệu gốc** (bằng chứng, không phải chiến lược). Số ý trong file theo bản v1 (19 ý). | Có, làm bằng chứng. Khi trích phải map số ý cũ → mới (xem C17). |
| 12 | `customer-research/amazon-storage-reviews.md` (19/11, 60.576 B) | Nguồn gốc: review Amazon thật cho 14 nhóm sản phẩm + bảng đối chiếu 19 ý bài 1 (đánh số theo bản v1) | **CHUẨN — tài liệu gốc**, kèm 2 cảnh báo nguồn trong chính file (xem C10). | Có, làm bằng chứng. |
| 13 | `customer-research/pinterest-search-trends.md` (19/11, 32.012 B) | Kiểm chứng trend + ngưỡng Raptive/Journey + từ khóa; ghi rõ chỗ chưa kiểm chứng được (Google Trends 429, Pinterest 403) | **CHUẨN — tài liệu gốc** (có giới hạn ghi rõ). Chưa cập nhật va chạm #35 (xem C3). | Có, làm bằng chứng. |
| 14 | `customer-research/us-renter-data.md` (19/11, 24.806 B) | Nguồn gốc: số liệu người thuê Mỹ (diện tích, cọc, tiền thuê, di chuyển), bảng đối chiếu chân dung cũ | **CHUẨN — tài liệu gốc** (nguồn của 460/735 sq ft). Dòng 4 trích câu v1 để kiểm chứng — đó là phương pháp của file, không phải khẳng định. | Có, làm bằng chứng. |
| 15 | `pinterest-article-1-draft/pinterest-article-1-draft.html` (v1, 11/11, 13.199 B) | Bản nháp bài 1 gốc: 19 ý, tiêu đề "19 Small Bedroom Storage Ideas for Renters (No Drilling)" | **LỖI THỜI — đã bị draft v2 thay thế.** Ghi chú dòng 15 ("thêm 2 ý nữa là xong" để lên 21) đúng số học lúc đó (19+2=21) nhưng đã hết hiệu lực. | Không dùng làm nội dung. Giữ làm lịch sử. |
| 16 | `pinterest-article-1-draft-v2/pinterest-article-1-draft-v2.html` (v2, 19/11, 27.454 B) | **Bản nháp bài 1 chuẩn hiện tại: 18 ý** + Step 0 declutter, hộp Renter Audit / "What I'd skip", Sources, FAQ HUD, phụ lục map ảnh + plan pin | **CHUẨN (chờ John duyệt)**. Ghi chú duyệt dòng 19 có 2 lỗi (xem C1). Dòng 155 sai tên bài 2–3 (xem C14). | Có — là bản nháp duy nhất được duyệt/đăng. |
| 17 | `ai-photos/article-1-ai-prompts.md` (19/11, 8.623 B) | Công thức master + 12 prompt ảnh AI bài 1 (hero + 11 ý), ghi chú kỹ thuật giống thật | **CHUẨN, trừ 2 chỗ**: tiêu đề file ghi "19 ý" (xem C1); prompt 09 (ý 14 bedside caddy) đã mồ côi vì ý bị bỏ (xem C17). | Có. |
| 18 | `ai-photos/` — 12 file JPG (hero + 11 ý, 1280×1920, <200 KB) | Ảnh AI bài 1 đã duyệt, đã lên GitHub commit 159ec59 | **CHUẨN**. Tên file dùng số ý CŨ (v1) — không đổi tên (đã lên GitHub); bảng map trong draft v2 phụ lục là chuẩn đối chiếu (xem C17). | Có. |
| 19 | `ai-photos/` — 13 file JSON `media-generation-*.json` | Metadata kỹ thuật của lần tạo ảnh (mỗi ảnh 1 file) | **CHỈ THAM KHẢO** (log kỹ thuật, không phải nội dung). | Giữ làm log, không đưa vào master. |
| 20 | `pinterest-article-1-image-bank/pinterest-article-1-image-bank.html` (11/11, 20.014 B) | Kho ảnh bài 1 cũ: 11 ảnh tham chiếu license CHƯA xác minh + 3 prompt AI (AI-01/02/03) + 3 pin mẫu A/B/C + spec video | **LỖI THỜI** — ảnh tham chiếu đã bị bộ ảnh AI thay thế (pivot 19/11); pin A/B/C đã bị 5 mẫu T1–T5 thay thế; mọi chỗ ghi "19" đã lệch. Chỉ spec video (1000×1500, <50 MB) còn dùng được. Ảnh tham chiếu license chưa xác minh — TUYỆT ĐỐI không tải về đăng lại. | Archive. Không lấy ảnh/pin từ đây nữa. |
| 21 | `pinterest-article-1-real-photos.md` (18/11, 11.101 B) | Danh sách ảnh thật miễn phí Unsplash/Pexels cho bài 1 (6–7 Unsplash + 4 Pexels), kèm hướng dẫn tự chụp | **LỖI THỜI** — pivot AI 19/11 ("đừng dùng ảnh Unsplash, ưu tiên ảnh AI") đã hủy toàn bộ workflow này. Tiêu đề file còn ghi "19 ý". | Archive. Không tải ảnh theo file này nữa. |
| 22 | `pinterest-12-month-strategy/meta.json` + `.src/url_baseline.json` | Metadata kỹ thuật của file chiến lược v1 (slug, hash URL) | **CHỈ THAM KHẢO** (log kỹ thuật). | Giữ nguyên, không đưa vào master. |

**Tóm tắt đếm nhanh:** 22 mục (14 file nội dung chính + 12 JPG + 13 JSON + 2 JSON metadata). Trạng thái: CHUẨN 13 mục · LỖI THỜI 4 mục (v1, draft v1, image-bank, real-photos) · CHỈ THAM KHẢO 2 mục (JSON metadata, JSON media-generation) · còn lại là tài liệu gốc/ảnh (dùng được).

---

## 2. Mâu thuẫn — từng cái một, kèm quyết định

### 2.1. Bảng tóm tắt

| ID | Vấn đề | Quyết định chuẩn | Cần John? |
|---|---|---|---|
| C1 | Số ý bài 1: 21 / 19 / 18 | **Đề xuất 18** (xem chi tiết) — chờ John chốt | ✅ CHỜ JOHN |
| C2 | The Tidy Renter có/không có Pinterest | **CÓ @tidyrenter từ 07/11/2026** (0 follower, 18 pin, 7 board) | Không — đã đính chính |
| C3 | Tiêu đề bài 35 va chạm | **Đổi tiêu đề trước khi viết** (2 đối thủ gần giống, không chỉ 1) | Không (quyết đổi đã có); tiêu đề mới thì CHỜ JOHN hoặc để lúc viết |
| C4 | Lighting đặt ở đâu | **Bài riêng GĐ2**, không vào bài 1 | Không — nhưng cần ghi vào roadmap (hiện chưa có) |
| C5 | Số trên pin T2 (19) vs bài (18) | **Đồng bộ theo số ý cuối cùng của bài 1** (18 nếu chốt 18) | Không — hệ quả của C1 |
| C6 | real-photos.md (Unsplash/Pexels) | **LỖI THỜI, archive** — pivot AI 19/11 đã hủy | Không |
| C7 | Diện tích 1BR: "dưới 600" vs 735 sq ft | **735 sq ft** (studio 460) | Không |
| C8 | Quiet Luxury +412% | **KHÔNG dùng bất kỳ con số % nào** | Không |
| C9 | Raptive + nội dung AI | **Quy trình biên tập con người bắt buộc** cho cả 150 bài | Không |
| C10 | Số review Amazon 131.718 — nguồn nào? | **Dùng được, nhưng là nguồn thứ cấp (09/2026)** — kiểm tra lại trước khi đăng | Không |
| C11 | Tổng số bài 148/160 vs 150; pin 450–480 vs 600+ | **150 bài, 450–480 pin** là chuẩn; bảng tiền trong v2 còn sót số v1 | Không |
| C12 | Tiền theo quý (Q1 $0–30 … Q4 $380–900) | **Nhất quán v1↔v2 — không mâu thuẫn** | Không |
| C13 | FunHaus: chiến lược "bỏ qua" hay không? | **Đã có trong v2** (1 trong 4 bài trend thử) — khiếu nại cũ đã đóng | Không |
| C14 | Draft v2 dòng 155 sai tên bài 2–3 | **Sửa dòng 155** theo danh sách 40 bài thật | Không |
| C15 | Bảng verdict gói nghiên cứu dùng tiêu đề v1 | **Theo thiết kế** (tiêu đề đang bị xét) — master dùng tiêu đề cuối | Không |
| C16 | image-bank: pin A/B/C + ảnh tham chiếu | **LỖI THỜI, archive** — chỉ giữ spec video | Không |
| C17 | Đánh số ý: cũ (v1) vs mới (v2) — ảnh JPG + prompt dùng số cũ | **Giữ tên file cũ, bảng map trong draft v2 là chuẩn đối chiếu** | Không |
| C18 | "10-minute reset" vs "2-minute reset" | **2-minute reset** (lời người thuê) | Không |
| C19 | The Small Apartment "không có Pinterest" | **Đổi cách ghi thành "không tìm thấy profile"** — tránh lặp lại lỗi C2 | Không |
| C20 | Tiêu đề bài 1 của mình gần giống tiêu đề The Tidy Renter | **Giữ, vì có số đếm phân biệt** ("18/19/21 …" + "(No Drilling)") | Không |

### 2.2. Chi tiết từng mâu thuẫn

**C1 — Số ý bài 1: 21 / 19 / 18 (MÂU THUẪN LỚN NHẤT — đang chờ John)**
- Chiến lược v1 dòng 100 + dòng 242: "21 Small Bedroom Storage Ideas for Renters on a Budget" (cả bảng 40 bài lẫn mục "Bài đầu tiên"). V1 dòng 141: bản pin dùng biến thể "19 Small Bedroom Storage Ideas for Renters" — v1 tự mâu thuẫn nội bộ (21 trong bảng, 19 trên pin).
- Draft v1 (11/11): 19 ý, tiêu đề "19 Small Bedroom Storage Ideas for Renters (No Drilling)". Ghi chú dòng 15: "thêm 2 ý nữa là xong" để lên 21 — đúng số học lúc đó (19+2=21).
- Chiến lược v2 dòng 112: "Bài 1 (19 ý) sau kiểm chứng: giữ 8, sửa 10, bỏ 1". V2 dòng 114: "tiêu đề chiến lược v1 ghi '21 ý' nhưng bài đã chốt 19 ý — đồng bộ số 19 ở tiêu đề bài, pin và mọi nơi trước khi làm pin".
- Gói nghiên cứu dòng 45 + mục 5: verdict trên 19 ý (giữ 8 / sửa 10 / bỏ 1). Bảng verdict dòng 216: tiêu đề bài 1 vẫn ghi theo v1 ("21 Small Bedroom Storage Ideas for Renters on a Budget") — xem C15.
- Draft v2 (19/11): 18 ý đánh số (18 thẻ `<h3>`), tiêu đề "18 Small Bedroom Storage Ideas for Renters (No Drilling)" (dòng 3, dòng 30), plan pin dòng 175 ghi "18 ideas". Ghi chú duyệt dòng 19: "Số lượng đổi 19 → 18… Nếu anh muốn 21 thì thêm 2 ý nữa (gợi ý từ playbook: 2 ý lighting…)" — **sai số học: 18+2=20, không phải 21** (ghi chú chép nguyên từ thời bài còn 19 ý mà không sửa phép tính). Gợi ý "2 ý lighting" cũng sai về nội dung — xem C4.
- pin-styles.md: T2 spec ghi "19" (mục T2, ví dụ "19" + bảng phân bổ dòng 196: "19" + "No-Drill Storage for Renters"); bảng phân bổ 3 pin ghi "19 Small Bedroom Storage Ideas" (3 lần); T3 ví dụ ghi "21 SMALL BEDROOM STORAGE IDEAS" — **cùng một file có cả 19 lẫn 21**.
- Playbook dòng 100 ("Bài 1 — 19 ý"), dòng 140 ("19 ý vs 10 ý"); teardown-tidy-renter dòng 107, 240 ("19 ý"); teardown-niche-blogs dòng 69 ("Bài 1 (19 ý phòng ngủ)"); teardown-big3 dòng 187, 305 ("19 ý") — tất cả viết lúc bài còn 19 ý.
- **Quyết định đề xuất: 18.** Lý do: (a) 21 chưa bao giờ tồn tại — v1 ghi 21 nhưng John chỉ duyệt 19 ý (11/11) và chưa bao giờ có bản nháp 21 ý; (b) 19 đã bị verdict sửa thành 18 (bỏ bedside caddy — ý yếu nhất, chỉ ~374 review, use case dorm); (c) draft v2 đã viết xong ở 18, tiêu đề + plan pin đã là 18 — giữ 18 là không viết lại, không chụp lại; (d) nếu lên 21 thì phải thêm 3 ý storage thật có kiểm chứng (không phải lighting — xem C4; không dùng lại bedside caddy đã bỏ) + 3 ảnh AI nữa. **Nếu John chốt 18:** đồng bộ mọi file sang 18 (v1 dòng 100/242, v2 dòng 112/114, pin-styles T2 + bảng phân bổ + ví dụ T3, playbook dòng 100/140, 3 file teardown, gói nghiên cứu dòng 45, ai-prompts.md tiêu đề) và xóa/sửa ghi chú dòng 19 draft v2. **Nếu John chốt 21:** thêm 3 ý storage (không phải lighting), cập nhật draft v2 + pin + ảnh, đồng bộ ngược lại sang 21. **Trạng thái: CHỜ JOHN** (2 widget đang chờ: duyệt draft v2 + đính chính số ý).

**C2 — The Tidy Renter có/không có Pinterest (ĐÃ ĐÍNH CHÍNH — còn 1 chỗ sót)**
- competitors.md (bản gốc) kết luận "không có Pinterest" sau 2 lần tìm kiếm. Teardown-tidy-renter.md dòng 8 + playbook dòng 48 đính chính: **CÓ Pinterest @tidyrenter** (pinterest.com/tidyrenter/), tài khoản business, website đã claim/verify, tạo 07/11/2026, 0 follower · 18 pin · 7 board, pin mới nhất 18/11/2026 14:07 UTC (trích JSON state trực tiếp từ trang profile). competitors.md + chiến lược v2 đã sửa (commit b9f4e17 + efc059a).
- **Còn sót 1 chỗ:** teardown-big3-keyword-gaps.md dòng 187, ô "Cơ hội": "(Tidy Renter không có Pinterest; blog có 19 ý vs 10 ý của họ + ảnh AI + pin T1/T2/T3)" — viết trước khi có đính chính. **Quyết định: sửa ô này thành "(Tidy Renter mới mở Pinterest 07/11/2026, 0 follower, 1 pin/bài text-only; blog có 18 ý vs 10 ý của họ…)"** (đồng thời sửa "19 ý" → số cuối theo C1).
- Hệ quả: cửa sổ cơ hội vẫn mở nhưng đang hẹp lại — kiểm tra lại @tidyrenter tháng 01/2027 và 03/2027 (nếu họ vượt 100 follower hoặc ra 3+ pin/bài thì cửa sổ đã hẹp).

**C3 — Tiêu đề bài 35 va chạm (ĐỔI TIÊU ĐỀ — có tới 2 đối thủ, không chỉ 1)**
- Bài 35 trong v1 dòng 134: "25 Storage Ideas for Apartments Under 600 Square Feet ★".
- Teardown-big3 dòng 244: **cozycubby.top có bài ĐÚNG TIÊU ĐỀ** "25 Storage Ideas for Apartments Under 600 Square Feet" (cập nhật 27 ngày trước 19/11, room-by-room, số đo inch, giá $20–$35). V2 dòng 111 đã ghi chú: "đổi tiêu đề trước khi viết". Playbook dòng 109 + dòng 157 nhắc lại.
- **Phát hiện thêm khi rà:** competitors.md dòng 290 ghi một đối thủ khác — Small Spaces Made Easy (blogspot) có bài "25 Small Apartment Storage Ideas for Apartments Under 600 Sq Ft", đăng 12/11/2026 — tiêu đề gần giống (thêm từ "Small Apartment", "Sq Ft" viết tắt). Tức là có **2 tiêu đề gần giống** đang chiếm từ khóa, không chỉ 1.
- **Quyết định: đổi tiêu đề bài 35 trước khi viết** (đổi số khác — vd 27 — hoặc đổi góc). Từ khóa "storage ideas for apartments under 600 sq ft" giữ làm từ khóa phụ. Trong bài phải viết đúng số: "under 600 sq ft" chỉ đúng studio (460); 1BR trung bình 735 (xem C7) — đừng khẳng định 1BR dưới 600. Tiêu đề mới chưa được chọn — ghi vào quyết định mở (mục 4) hoặc để lúc viết bài mới chốt.

**C4 — Lighting đặt ở đâu (KHÔNG vào bài 1)**
- Teardown-tidy-renter dòng 54 + 208 + 248: The Tidy Renter có cluster lighting 11 ý (lumens, Kelvin, plug-in sconce, LED strips) mà 40 bài của mình thiếu — "thêm 1 bài lighting vào GĐ2 (hoặc 2 ý lighting vào Bài 9 + Bài 37)". Playbook dòng 108 + 157 nói y hệt. V2 dòng 111: "cân nhắc thêm 1 bài lighting vào GĐ2".
- Draft v2 dòng 19 (ghi chú): gợi ý "2 ý lighting renter-friendly" **vào bài 1** để lên 21 — **mâu thuẫn với playbook + v2**: bài 1 là listicle storage, nhét lighting vào là lạc đề; và 11 ý lighting của đối thủ mới chỉ được tóm tắt (lumens/Kelvin, plug-in sconce, LED strips), chưa có danh sách nào kiểm chứng để chèn.
- **Lỗ hổng trong roadmap:** content-expansion.md (lộ trình 40 → 150) **không hề nhắc lighting** (grep 0 kết quả) — v2 nói "cân nhắc thêm" nhưng roadmap không có chỗ cho nó.
- **Quyết định: lighting làm bài riêng ở GĐ2 (phương án chính của playbook).** Nếu thêm vào roadmap 150 thì tổng thành 151 — hoặc đổi 1 bài park (vd #16 loveseat hoặc #26 basket wall, cả hai đều "chưa đủ bằng chứng") lấy chỗ. Phương án dự phòng: 2 ý lighting vào bài 9 + bài 37 (không làm bài riêng). **Ghi chú dòng 19 draft v2 về "2 ý lighting vào bài 1" là sai — bỏ khi sửa ghi chú.**

**C5 — Số trên pin T2 (19) vs số ý trong bài (18)**
- pin-styles.md: T2 spec ví dụ số "19"; bảng phân bổ 3 pin/bài (dòng ~194–198) ghi T1 "19 Small Bedroom Storage Ideas", T2 "19" + "No-Drill Storage for Renters", T3 "Small Bedroom Storage — 19 Ideas"; T3 ví dụ ghi "21 SMALL BEDROOM STORAGE IDEAS" (sai dưới mọi kịch bản — kể cả chốt 21 thì ví dụ này cũng thiếu "(No Drilling)" và không khớp format T3).
- Draft v2 dòng 175 (plan pin): T2 "18 ideas" — đã đúng với 18.
- **Quyết định: đồng bộ tất cả số trên pin theo số ý cuối cùng của bài 1 (18 nếu chốt 18; 21 nếu chốt 21).** Quy tắc trong chính pin-styles.md dòng 136 ("số trên pin phải khớp số thật trong bài") vẫn đúng — chỉ các ví dụ số là sai và cần sửa. Sửa cả ví dụ T3 ("21" → số cuối).

**C6 — real-photos.md (Unsplash/Pexels) đã lỗi thời**
- File ngày 18/11: danh sách ảnh thật miễn phí Unsplash/Pexels cho bài 1 (6–7 Unsplash + 4 Pexels), tiêu đề "19 Small Bedroom Storage Ideas for Renters".
- Pivot 19/11 08:34 (John): "đừng dùng ảnh Unsplash, ưu tiên dùng ảnh AI, tìm cách tạo ảnh AI chân thực nhất" — toàn bộ workflow trong file này bị hủy; bộ 12 ảnh AI đã thay thế (commit 159ec59).
- **Quyết định: ARCHIVE file này (đánh dấu lỗi thời, không xóa).** Không tải ảnh theo file này nữa. Hướng dẫn tự chụp trong file (nếu có) không còn là bước bắt buộc — ảnh AI đã cover, trừ trường hợp John yêu cầu chụp thật sau này.

**C7 — Diện tích 1BR: "dưới 600 sq ft" vs 735 sq ft**
- V1 dòng 40: "người Mỹ thuê nhà, 20–35 tuổi, ở studio / căn 1 phòng ngủ dưới 600 sq ft…" — **sai một nửa**.
- us-renter-data.md dòng 34 + 84 + 97: studio mới trung bình 460 sq ft (dưới 600, đúng); 1BR mới trung bình **735 sq ft** (RentCafe/Yardi Matrix, dữ liệu đến 05/2026) — vượt 600. Dưới 600 chủ yếu ở thành phố đắt đỏ (Seattle trung bình mọi loại căn chỉ 645 sq ft). Đồng thời "căn hộ ngày càng nhỏ" đã sai hướng — diện tích căn mới tăng lại từ 2024–2025.
- Gói nghiên cứu dòng 44 + 71; v2 dòng 52: đã sửa thành "studio 460, 1BR 735".
- **Quyết định: dùng "studio ~460 sq ft, 1BR trung bình 735 sq ft (dưới 600 chủ yếu ở thành phố đắt đỏ)". Không viết "1BR dưới 600 sq ft" như fact chung nữa. Bỏ luận điểm "căn hộ ngày càng nhỏ".** V1 dòng 40 là lỗi thời (v1 đã archive về nội dung). Lưu ý: tiêu đề bài 35 "Under 600 Square Feet" là cụm từ khóa, không phải khẳng định về 1BR — giữ từ khóa nhưng viết đúng số trong bài (xem C3).

**C8 — Quiet Luxury +412%**
- V1 dòng 44: "+412% là phân tích thứ cấp của PinAutopilot, không phải số chính thức của Pinterest — vẫn dùng được, nhưng không ghi là Predicts 2026".
- pinterest-search-trends.md dòng 20 + 26: PinAutopilot là công cụ bán tự động hóa Pinterest (xung đột lợi ích); nguồn thứ cấp khác (Artfasad, trích "Pinterest's 2026 Home Report") nói **+312%** — hai nguồn mâu thuẫn nhau. Kết luận: **không được dùng +412% như fact trong bài viết hay pin.** Dòng 21: "Quiet Luxury là trend carryover từ 2025" — **CHƯA KIỂM CHỨNG** (không thấy trong 21 trend Predicts 2026).
- V2 dòng 111 (mục SỬA bài 13, 14): "bỏ mọi con số % Quiet Luxury".
- **Quyết định: KHÔNG dùng bất kỳ con số % nào cho Quiet Luxury trong bài/pin. Không ghi "carryover từ 2025" khi chưa kiểm chứng Predicts 2025.** V1 dòng 44 là lỗi thời.

**C9 — Raptive + nội dung AI (không mâu thuẫn — khoảng trống đã được lấp)**
- V1 (mục 8, dòng 176): Raptive 25.000 pageviews/tháng, dưới 100k cần ≥50% traffic Tier-1, domain ≥6 tháng — đúng, nhưng **không nhắc yêu cầu về nội dung AI**.
- pinterest-search-trends.md dòng 105: Raptive Help Center yêu cầu "meaningful human involvement"; các bài review ghi rõ **site dùng AI tạo nội dung sẽ không được monetize** — cờ đỏ cho blog dùng ảnh AI + bài AI.
- V2 dòng 56 + 284–285: thêm cờ đỏ + quy trình biên tập con người bắt buộc (viết lại giọng người, kiểm chứng từng ý + ngày kiểm tra, quotes thật, ảnh AI bật "Mark as AI-Modified" + ghi chú "AI-generated concept image", không before/after giả) — áp dụng cho cả 150 bài.
- **Quyết định: quy tắc v2 là chuẩn cho toàn bộ dự án. Không có gì phải sửa — chỉ ghi nhận v1 thiếu cảnh báo này.**

**C10 — Số review Amazon 131.718 — nguồn nào? (nhất quán về số, cần ghi chú về nguồn)**
- Số **131.718 reviews, 4,6★, #1 bestseller** (Simple Houseware over-door organizer) xuất hiện nhất quán: amazon-storage-reviews.md dòng 56, 218, 246, 276; gói nghiên cứu dòng 157, 186; draft v2 dòng 44 + Sources dòng 153; playbook + teardowns.
- **Nhưng nguồn gốc là thứ cấp:** amazon-storage-reviews.md dòng 56 ghi "(onlycaptions.com, 09/2026)" — số lấy qua trang tổng hợp, không phải đọc trực tiếp từ listing Amazon, và đã 2 tháng tuổi (09/2026 → 11/2026). Draft v2 dòng 153 ghi "Amazon listings as cited in the Pinterest customer research pack" — diễn đạt này làm số trông như đọc trực tiếp từ Amazon.
- Số **~374 ratings** (Amazon Basics bedside caddy) nhất quán: amazon-storage-reviews.md dòng 122, 252; gói nghiên cứu dòng 192; draft v2 dòng 130.
- **Quyết định: giữ cả hai số (nhất quán, không mâu thuẫn). Ghi chú nguồn trong master: "131.718 (nguồn thứ cấp onlycaptions.com, 09/2026 — kiểm tra lại trước khi đăng)".** Draft v2 đã tự ghi chú đúng điều này trong ghi chú duyệt dòng 5 ("kiểm tra lại số review/lượt rating nếu đã quá 2 tuần"). Lưu ý thêm: amazon-storage-reviews.md tự ghi 2 trang Amazon mở được là crawl cũ (Utopia risers 03/07/2024; Command 28/06/2024) — các số review lấy từ các trang đó cần kiểm tra lại trước khi đăng.

**C11 — Tổng số bài 148/160 vs 150; pin 450–480 vs 600+**
- V1: stat card dòng 34 "~450–480 pin tươi tích lũy (3 pin/bài + pin refresh mùa vụ)"; bảng tháng 10/2027 dòng 159 "148 bền / 160 căng"; Q4 dòng 184 "110–148 bài, 600+ pin ở nhịp căng" — **v1 tự mâu thuẫn nội bộ: 450–480 pin (dòng 34) vs 600+ pin (dòng 184).**
- content-expansion.md dòng 21 + 232: "Giữ mốc ~150 bài. Lộ trình chốt ở 150 bài (40 + 50 + 60), khớp mốc '148 bền' của chiến lược" — đã tự hòa giải.
- V2 dòng 53 + 117 + 125 + 301: chốt **150 bài** (40 + 50 + 60), "150 bài · 450–480 pin tươi" (dòng 301). **Nhưng bảng tiền v2 dòng 320 (Q4) vẫn chép nguyên hàng v1: "110–148 bài, 600+ pin ở nhịp căng"** — mâu thuẫn với dòng 301 trong cùng một file. Các hàng Q1–Q3 (dòng 317–319: 40 / 65–76 / 90–112 bài) cũng là số v1, không khớp lộ trình 150 (GĐ2 kết thúc 05/2027 ở bài 90, GĐ3 06–10/2027 lên 150 — Q3 05–07/2027 phải là ~90–112 thì đúng, nhưng Q4 08–10/2027 phải là 113–150, không phải 110–148).
- **Quyết định: 150 bài và 450–480 pin tươi là chuẩn (3 pin/bài × 150). Sửa bảng tiền v2 dòng 320 thành "113–150 bài, 450–480 pin tươi".** V1 dòng 159/184 là lỗi thời. Tiền theo quý giữ nguyên (xem C12).

**C12 — Tiền theo quý (không mâu thuẫn)**
- V1 dòng 184 + v2 dòng 317–320: Q1 $0–30 · Q2 $70–200 · Q3 $200–500 · Q4 $380–900; $100/tháng tháng 7–9 (thận trọng), $300/tháng tháng 11–12/2027. Baseline RPM Productive Blogging 2025 (Journey $11,15 / Mediavine $31,55 / Raptive $34,86) giống nhau ở cả hai file. **Không có mâu thuẫn — chỉ ghi nhận để khỏi rà lại.**

**C13 — FunHaus: chiến lược "bỏ qua" hay không? (đã đóng trong v2)**
- pinterest-search-trends.md dòng 23: "FunHaus cũng là trend nhà cửa chính thức 2026… Chiến lược chỉ dùng 2/3" (Predicts 2026 có 3 trend nhà cửa: FunHaus +130%, Afrohemian, Neo Deco). Gói nghiên cứu dòng 281: ghi chú FunHaus "bị bỏ qua".
- **Nửa đúng:** v1 dòng 44 (mục trend) chỉ nhắc Afrohemian +220%, Neo Deco, Quiet Luxury — không nhắc FunHaus. **Nhưng** v1 dòng 167 (cluster K — Trend Aesthetics 119–138) đã liệt kê FunHaus trong danh sách mở rộng.
- content-expansion.md dòng 85: K Trend cắt 20 → 4 bài, "1 bài/trend: Quiet Luxury rẻ, Neo Deco touches, Afrohemian textiles, FunHaus" — FunHaus đã có 1 bài thử.
- **Quyết định: khiếu nại đã đóng — FunHaus có 1 bài thử trong 4 bài trend (K 135–138). Không cần sửa gì thêm.**

**C14 — Draft v2 dòng 155 sai tên bài 2–3**
- Draft v2 dòng 155: "Next in this cluster: 'How to Organize a Small Closet for Renters' and 'Small Bedroom Layout Ideas for Renters' — bài 2–3 trong chiến lược 12 tháng."
- Danh sách 40 bài thật (v1 dòng 101–102): bài 2 = "How to Organize a Small Bedroom for Renters (Without Drilling a Single Hole)"; bài 3 = "15 Small Living Room Ideas for Renters Under $200". Không có bài nào tên "How to Organize a Small Closet for Renters" (gần nhất là bài 27 "25 Closet Organization Ideas for Small Rental Closets") hay "Small Bedroom Layout Ideas for Renters" (gần nhất là bài 7 studio layout / bài 12).
- **Quyết định: sửa dòng 155 thành tên thật của bài 2 + bài 3.** (Sửa này làm lúc John duyệt draft v2, cùng lượt với ghi chú dòng 19.)

**C15 — Bảng verdict gói nghiên cứu dùng tiêu đề v1**
- Gói nghiên cứu dòng 216 (bảng verdict 40 bài): bài 1 ghi tiêu đề v1 "21 Small Bedroom Storage Ideas for Renters on a Budget" trong khi verdict của chính gói này là trên bản 19 ý (dòng 45, mục 5). Tương tự các bài khác trong bảng dùng tiêu đề v1 (vd bài 39 dòng 254 ghi tiêu đề cũ "…600 Sq Ft" trong khi verdict là SỬA — bỏ "600 Sq Ft").
- **Quyết định: đây là thiết kế của bảng (tiêu đề đang bị xét, verdict là phán quyết về nó) — không phải lỗi. Nhưng master file phải dùng tiêu đề CUỐI CÙNG (sau khi áp dụng verdict: #34, #39 đổi tiêu đề; #35 chờ đổi — xem C3), không copy nguyên tiêu đề từ bảng verdict.**

**C16 — image-bank: pin A/B/C + ảnh tham chiếu**
- image-bank dòng 25: 11 ảnh tham chiếu license CHƯA xác minh — không tải về đăng lại. Dòng 112–114: pin A/B/C dùng "19" (Pin B: "19 Storage Ideas, Zero Holes, Renter Approved"; video script dòng 123: "See all 19"). Dòng 75/83: prompt AI-01 Quiet Luxury, AI-02 Afrohemian.
- Bộ 12 ảnh AI (commit 159ec59) đã thay thế toàn bộ ảnh tham chiếu; 5 mẫu pin T1–T5 (pin-styles.md) đã thay thế pin A/B/C.
- **Quyết định: ARCHIVE image-bank (xem mục 1, dòng 20). Chỉ giữ spec video (1000×1500, MP4 H.264, <50 MB, nhạc lo-fi, cover = pin số) — spec này vẫn dùng được cho video pin sau này.**

**C17 — Đánh số ý: cũ (v1) vs mới (v2) — ảnh JPG + prompt dùng số cũ**
- JPG + prompt dùng số ý v1: `article-1-idea-01/04/06/08/10/11/12/13/14/16/17` (11 ảnh theo ý cũ). Draft v2 đổi số: ý 8 cũ (over-door) → ý 1 mới; ý 12 cũ (kệ nổi) → ý 17 mới; ý 13 cũ (nightstand) → ý 14 mới; ý 14 cũ (bedside caddy) → BỎ; ý 15 cũ (drawer dividers) → ý 12 mới; ý 16 cũ (rolling cart) → ý 13 mới; ý 17 cũ (baskets) → ý 15 mới; ý 18 cũ (shoe organizer) → ý 16 mới; ý 19 cũ (reset) → ý 18 mới.
- Draft v2 phụ lục (dòng ~158–175) đã có bảng map đầy đủ: ảnh nào → ý mới nào, ảnh ý 14 KHÔNG dùng, ảnh ý 12 giữ trong bài nhưng CHƯA làm pin.
- ai-prompts.md: prompt 09 (dòng 88–90) là prompt cho ý 14 bedside caddy — **đã mồ côi** (ý bị bỏ, ảnh không dùng). Tiêu đề file ghi "19 Small Bedroom Storage Ideas for Renters".
- **Quyết định: KHÔNG đổi tên file JPG (đã lên GitHub commit 159ec59 — đổi tên gây lệch link). Bảng map trong draft v2 phụ lục là chuẩn đối chiếu duy nhất. Sửa ai-prompts.md: tiêu đề → số cuối (18 nếu chốt 18); đánh dấu prompt 09 là "KHÔNG DÙNG — ý đã bỏ" (không xóa prompt, để làm tư liệu).** Khi làm ảnh cho các ý còn thiếu (8 ý — xem mục 4), đặt tên file theo số ý MỚI và ghi rõ trong bảng map.

**C18 — "10-minute reset" vs "2-minute reset"**
- Draft v1 dòng 84 (ý 19): "A 10-minute reset routine". amazon-storage-reviews.md dòng 257 + reddit-renter-insights.md dòng 119/124/184: thói quen reset có bằng chứng mạnh, nhưng người thuê nói **2–5 phút mỗi tối**; "10 phút" là framework của dân tổ chức chuyên nghiệp, không phải lời người dùng.
- Draft v2: ý 18 "A 2-minute reset routine" (10 phút chỉ dành cho buổi tổng vệ sinh tuần). V2 + playbook dùng "2-minute reset".
- **Quyết định: "2-minute reset" là chuẩn. "10-minute reset" chỉ còn trong draft v1 (đã archive) và trong các file nguồn khi họ trích lại nhãn cũ — không phải mâu thuẫn sống.**

**C19 — The Small Apartment "không có Pinterest" (đổi cách ghi để tránh lặp lại lỗi C2)**
- competitors.md dòng 133 + v2 dòng 251: The Small Apartment "**Không có Pinterest**".
- teardown-niche-blogs.md dòng 19 + 59: trang About khẳng định có Pinterest ("You can find more small-space inspiration on Pinterest…"), trong bài có ảnh pin "Save for later" — nhưng 2 lần tìm có chủ đích ngày 19/11 đều **không tìm thấy URL profile**. Suy luận trong file: hoặc profile mới/không index, hoặc họ chưa gắn link ở đâu trên site.
- **Quyết định: đổi cách ghi trong competitors.md + v2 thành "không tìm thấy profile Pinterest (About khẳng định có, nhưng không tìm thấy URL sau 2 lần tìm 19/11)".** Bài học từ C2: "không tìm thấy" ≠ "không có" — The Tidy Renter đã chứng minh cách ghi cũ gây sai.

**C20 — Tiêu đề bài 1 của mình gần giống tiêu đề The Tidy Renter**
- The Tidy Renter: "Small Bedroom Storage Ideas for Renters (No Drilling)" (10 ý, 16/11/2026) — competitors.md dòng 108.
- Bài 1 của mình: "19/18 Small Bedroom Storage Ideas for Renters (No Drilling)" — giống hệt phần sau, chỉ khác số đếm ở đầu.
- **Quyết định: giữ tiêu đề (số đếm phân biệt đủ trên Google + Pinterest; từ khóa chính "small bedroom storage ideas for renters" là từ khóa mạnh nhất, không đổi).** Không phải va chạm y hệt như bài 35 (bài 35 trùng cả số lẫn chữ). Ghi chú trong master để khỏi ai tưởng là trùng lặp cần đổi.

---

## 3. Cấu trúc file master duy nhất — đề xuất

File master = 1 file HTML (phong cách giấy ấm + terracotta như v2/pack/playbook), đọc từ trên xuống dưới là hiểu toàn bộ dự án. Nguyên tắc: **nội dung chuẩn nằm TRONG master; tài liệu gốc chi tiết chỉ LINK tới, không copy nguyên văn.**

| # | Mục (theo thứ tự đọc) | Nội dung | Lấy từ file nào | Ghi chú |
|---|---|---|---|---|
| 0 | Hộp "Đọc trước — trạng thái dự án" | Ngày cập nhật master; số ý bài 1 hiện tại (sau khi John chốt); 3 quyết định còn mở (mục 4); link tới file này (consolidation-spec.md) | — (mới viết) | Cập nhật mỗi lần John quyết xong 1 việc. |
| 1 | Định vị + chân dung người đọc | 1 câu định vị; 3 persona (Maya 27 studio 460 / Jordan 31 1BR 735 / Alex 23 first apartment) + 5 JTBD + nỗi đau/mong muốn chính | Gói nghiên cứu mục 2–4; v2 mục 1 | Dùng số đã sửa (460/735 — xem C7). Không dùng bản phác v1. |
| 2 | Quy tắc nội dung (chuẩn kiểm chứng) | Dateline "Prices checked [tháng/năm]" + Sources + Update log; hộp Renter Audit; "What I'd skip" + review-mining; bảng chịu tải/deposit math; calculator đo-trước-khi-mua; quy trình biên tập con người cho Raptive (5 điểm) | V2 mục "Quy trình biên tập con người"; playbook mục 2 (copy gì); teardown-tidy-renter mục 2–3 | Đây là chuẩn áp cho cả 150 bài, không chỉ bài 1. |
| 3 | Chiến lược nội dung: 40 bài đầu | **Bảng 40 bài duy nhất, tiêu đề CUỐI CÙNG** (sau verdict: #34/#39 đổi tiêu đề, #35 ghi "CHỜ ĐỔI TIÊU ĐỀ", #13/#14/#15/#25 ghi "1 bài thử") + verdict từng bài (GIỮ/SỬA/CHƯA ĐỦ BẰNG CHỨNG) + cụm nào đánh Google / Pinterest / freebie | V1 bảng 40 bài (tiêu đề gốc) + gói nghiên cứu mục 6 (verdict) + v2 mục 2 (tóm tắt verdict) + playbook mục 5 (bản đồ gap) | Đây là bảng hay bị lệch nhất — master chỉ giữ 1 bảng này, mọi file khác link về đây. |
| 4 | Lộ trình mở rộng 40 → 150 | 3 giai đoạn (40 + 50 + 60), cluster mới (S Declutter, I First Apartment/Moving, J Budget/Gift/Printable, F Bathroom, H Entryway, G Closet Depth, K Trend 4 bài), hub/spoke, top-20 ưu tiên | content-expansion.md (toàn bộ) + v2 mục 2 | **Thêm bài lighting GĐ2 vào roadmap** (xem C4) — nếu thêm thì ghi rõ tổng thành 151 hoặc bài nào bị thay. |
| 5 | Bài 1 — trạng thái hiện tại | Tiêu đề cuối + số ý cuối (sau khi John chốt); tóm tắt verdict (giữ 8 / sửa 10 / bỏ 1); thay đổi chính trong draft v2 (ý 8 lên #1, Step 0, JTBD 3, móc dán = rủi ro cọc lớn nhất, kệ nổi xuống cuối, 2-minute reset); link tới draft v2 (file, chưa publish); trạng thái ảnh AI (12 ảnh có / 8 ý thiếu ảnh) | Draft v2 (+ ghi chú duyệt đã sửa) + gói nghiên cứu mục 5 + ai-prompts.md | Mục này thay đổi sau mỗi lần John quyết — ghi ngày cập nhật. |
| 6 | Hệ thống Pinterest | 10 board (board 8 = trend-test only); 5 mẫu pin T1–T5 + spec Canva; quy tắc chữ/màu/kích thước; 3 pin tươi/bài, cách nhau ≥72h; video pin (khi nào làm, spec); quy tắc nhãn AI-Modified | pin-styles.md (toàn bộ) + v2 mục 3 | **Đồng bộ số ý bài 1 trong mọi ví dụ** (xem C5) trước khi đưa vào master. |
| 7 | Đối thủ — bản đồ + nước đi | Bảng 25 đối thủ (tóm tắt); teardown The Tidy Renter + 9 blog ngách + Big 3 (tóm tắt 1 đoạn mỗi nhóm); 5 format copy / 5 sai lầm tránh / 5 khoảng trống chiếm ngay; beat sheet tóm tắt (không copy nguyên bảng 18 bài) | competitors.md + competitor-playbook.html + 3 file teardown | Chi tiết đầy đủ chỉ LINK tới playbook + teardowns, không copy hết vào master. |
| 8 | Plan thực thi 12 tháng | Tháng 11/2026 → 10/2027 từng tháng; SOP tuần; giờ/tuần theo giai đoạn; mốc kiểm tra tháng 3/6/9/12 (giữ/sửa/dừng); chi phí tool (~$270–355/năm + domain/hosting) | V2 mục 5–7 | **Sửa bảng tiền dòng Q4: "113–150 bài, 450–480 pin tươi"** (xem C11). |
| 9 | Tiền — mô hình + mốc | Journey → Raptive + Amazon + printable + email; ngưỡng (Journey 1.000 sessions Tier-1; Raptive 25.000 pageviews); RPM baseline Productive Blogging 2025; tiền theo quý (giữ nguyên v1); cờ đỏ Raptive (xem C9) | V1 mục 8–9 + v2 mục 6 | Ghi rõ mọi doanh thu là ước tính, không phải cam kết. |
| 10 | Giới hạn + chưa kiểm chứng được | Reddit trực tiếp bị chặn (dùng mirror); Google Trends 429; Pinterest Search 403; volume tuyệt đối US chưa có; số Pinterest đối thủ đa số là bằng chứng thứ cấp (trừ @tidyrenter trích JSON trực tiếp); số review Amazon cần kiểm tra lại trước khi đăng | Gói nghiên cứu mục 7–8 + pinterest-search-trends.md + từng file teardown (mục Giới hạn) | Mục này giữ trung thực — không xóa khi hợp nhất. |
| 11 | Phụ lục — link tới tài liệu gốc | Danh sách file nguồn đầy đủ (mục 1 của bản này) + trạng thái từng file; link tới: gói nghiên cứu, 4 file nguồn (reddit/amazon/trends/us-renter-data), competitors.md, pin-styles.md, content-expansion.md, playbook, 3 teardown, draft v2, ai-prompts.md | — (mới viết) | File archive (mục 5) ghi rõ "LỖI THỜI — chỉ tham khảo lịch sử". |

**Quy ước đặt tên trong master (để khỏi lệch nữa):**
- Số ý bài 1: ghi 1 con số duy nhất ở mọi chỗ sau khi John chốt (tiêu đề bài, pin, bảng 40 bài, mục 5). Không ghi "19 (cũ)" hay "21 (v1)" trong nội dung chính — lịch sử số để ở mục 10 hoặc trong bản này.
- Số ý các bài khác: lấy từ tiêu đề cuối trong bảng mục 3; khi viết thật, số trên pin = số thật trong bài (quy tắc pin-styles.md dòng 136).
- Diện tích: "studio ~460 sq ft, 1BR 735 sq ft" (xem C7). Không viết "dưới 600 sq ft" cho 1BR.
- Tiền: ghi kèm "ước tính, không cam kết" ở mọi bảng tiền.
- Ngày kiểm tra: mọi số giá/review ghi kèm ngày kiểm tra (vd "kiểm chứng 19/11/2026").

---

## 4. Quyết định còn mở — chỉ những cái thật sự chưa có đáp án của John

| # | Quyết định | Đang chờ gì | Hệ quả nếu chưa quyết | Ghi chú |
|---|---|---|---|---|
| 1 | **Số ý bài 1: 18 hay 21?** | John bấm 1 trong 2 lựa chọn (widget duyệt draft v2, gửi 10:56 19/11 + widget đính chính số ý, gửi sau đó). Draft v2 đang là 18 ý. | Mọi file còn ghi 19/21 đều chưa đồng bộ được (xem C1, C5). Draft v2 chưa được đưa lên GitHub. 8 ảnh AI còn thiếu chưa làm được (cần biết số ý cuối). | Đề xuất của biên tập: **18** (lý do ở C1). Nếu chọn 21: thêm 3 ý storage thật có kiểm chứng (không lighting, không bedside caddy) + 3 ảnh AI. |
| 2 | **Domain tinynookliving.com — mua hay chưa?** | John chưa trả lời từ 16/11 (widget "Chốt mua tinynookliving.com" / "Để sau đã"). Domain vẫn trống ở lần check thứ 5 (tối 16/11) — phải check lại ở nhà đăng ký ngay trước khi trả tiền (~$10–11/năm Porkbun/Cloudflare). | Draft v2 giữ placeholder `[yourdomain.com]`; không publish được bài 1 lên domain thật; plan thực thi tháng 11 (setup WordPress) bị chặn ở bước domain. | Nằm trong danh sách không hỏi lại dồn dập — chỉ nhắc khi liên quan trực tiếp tới bước publish. Không mua khi chưa có xác nhận rõ ràng của John. |
| 3 | **Bắt đầu thực thi tháng 11?** | Widget "Bắt đầu thực thi tháng 11 (setup + viết lại bài 1)" / "Để anh đọc chiến lược v2 trước đã" (gửi 09:53 19/11) chưa được bấm. Draft v2 chính là nội dung cụ thể đằng sau lựa chọn này (đã gửi 10:56 19/11) — đừng hỏi lại widget như việc riêng. | Chưa có lệnh bắt đầu: chưa upload draft v2 lên GitHub, chưa làm 3 pin bài 1, chưa setup WordPress/Pinterest. | Nếu John bấm "bắt đầu": (a) xác nhận riêng bước mua domain (quyết định 2) trước khi trả tiền; (b) upload draft v2 sau khi chốt số ý (quyết định 1); (c) làm 3 pin T1/T2/T3 cho bài 1. |
| 4 | **Tiêu đề mới cho bài 35** (sau khi quyết đổi — xem C3) | Chưa có tiêu đề mới nào được đề xuất hay chọn. Playbook gợi ý đổi số (vd 27) hoặc đổi góc. | Bài 35 chưa viết được (va chạm với cozycubby.top + smallspacesmadeeasy). Không chặn các bài khác — bài 35 ở GĐ1 nhưng không phải bài đầu. | Có thể để tới lúc viết bài 35 mới chốt, nhưng phải ghi "CHỜ ĐỔI TIÊU ĐỀ" trong bảng 40 bài của master để khỏi ai dùng nhầm tiêu đề cũ. |
| 5 | **Lighting: bài riêng GĐ2 hay 2 ý trong bài 9 + 37?** (xem C4) | Chưa quyết. Playbook ưu tiên bài riêng GĐ2; phương án dự phòng là 2 ý trong bài 9 + 37. | content-expansion.md chưa có chỗ cho lighting — nếu chọn bài riêng thì roadmap 150 thành 151 hoặc phải thay 1 bài park. | Không chặn bài 1 — quyết sau cũng được, nhưng phải quyết trước khi viết tới GĐ2 (02–05/2027). |

**Không còn mở (đừng hỏi lại):** palette terracotta + trắng ấm (+ Olive phụ) đã chốt theo v2; 5 mẫu pin T1–T5 đã chốt; ngách Home Decor — Small Space / Renter đã chốt 11/11; pivot ảnh AI (Nano Banana) đã chốt 19/11; mẫu hero AI đã duyệt 19/11; 40 bài verdict (giữ 23 / sửa 6 / chưa đủ bằng chứng 11) đã có trong gói nghiên cứu; đính chính Pinterest của The Tidy Renter đã xong.

---

## 5. Archive vs Giữ

### 5.1. ARCHIVE — đánh dấu lỗi thời trong file (thêm banner đầu file hoặc đổi tên thư mục thành `archive/`), KHÔNG xóa

| File | Lý do archive | Ghi chú khi archive |
|---|---|---|
| `pinterest-12-month-strategy/pinterest-12-month-strategy.html` (v1) | Đã bị v2 thay thế toàn bộ về nội dung (persona, 40 bài, mở rộng, pin). Còn 3 chỗ sai số đã biết (21 ý bài 1, 1BR dưới 600, Quiet Luxury +412% "vẫn dùng được"). | Thêm banner: "ARCHIVE 19/11/2026 — đã bị chiến lược v2 thay thế. Chỉ tham khảo lịch sử + bảng tiền (v2 giữ nguyên tiền)." |
| `pinterest-article-1-draft/pinterest-article-1-draft.html` (draft v1) | Đã bị draft v2 thay thế (19 ý → 18 ý, bỏ bedside caddy, sửa 10 ý). | Thêm banner: "ARCHIVE 19/11/2026 — đã bị draft v2 thay thế." |
| `pinterest-article-1-image-bank/pinterest-article-1-image-bank.html` | Ảnh tham chiếu license chưa xác minh đã bị bộ ảnh AI thay thế; pin A/B/C đã bị 5 mẫu T1–T5 thay thế; mọi chỗ ghi "19" đã lệch. | Thêm banner: "ARCHIVE 19/11/2026 — ảnh tham chiếu license CHƯA xác minh, TUYỆT ĐỐI không tải về đăng lại. Chỉ spec video còn dùng được." |
| `pinterest-article-1-real-photos.md` | Pivot AI 19/11 đã hủy workflow Unsplash/Pexels. | Thêm banner: "ARCHIVE 19/11/2026 — pivot AI: không dùng ảnh Unsplash/Pexels nữa." |

### 5.2. GIỮ làm tài liệu gốc / chuẩn hiện tại

| Nhóm | File | Vai trò sau khi hợp nhất |
|---|---|---|
| Chiến lược chuẩn | `pinterest-content-strategy-v2.html` | Xương sống của master (sửa 3 lỗi nội bộ ở C11/C5/C1 khi làm master, không sửa file gốc ở đây). |
| Bằng chứng gốc | `customer-research/pinterest-customer-research-pack.html` + `reddit-renter-insights.md` + `amazon-storage-reviews.md` + `pinterest-search-trends.md` + `us-renter-data.md` | Nguồn bằng chứng — master chỉ trích kết quả + link, không copy nguyên văn. |
| Nghiên cứu đối thủ | `customer-research/competitors.md` + `competitor-playbook.html` + `teardown-tidy-renter.md` + `teardown-niche-blogs.md` + `teardown-big3-keyword-gaps.md` | Tài liệu hành động + bằng chứng đối thủ (sửa 1 ô stale ở teardown-big3 dòng 187). |
| Kỹ thuật pin + mở rộng | `customer-research/pin-styles.md` + `customer-research/content-expansion.md` | Spec kỹ thuật (đồng bộ số ý bài 1; bổ sung lighting vào roadmap). |
| Bài 1 | `pinterest-article-1-draft-v2/pinterest-article-1-draft-v2.html` + `ai-photos/article-1-ai-prompts.md` + 12 JPG | Bản nháp + ảnh đang làm (sửa ghi chú dòng 19 + dòng 155 draft v2; sửa tiêu đề + prompt 09 trong prompts file). |
| Bản này | `consolidation-spec.md` | Chuẩn đối chiếu cho file master + ghi lại mọi quyết định. |

---

## 6. Ghi chú cho agent dựng file master (không phải nội dung master)

1. **Đừng copy nguyên văn các file nguồn vào master** — master là tổng hợp + bảng duy nhất; chi tiết nằm ở file gốc, master chỉ link tới.
2. **Thứ tự sửa trước khi dựng master:** (a) chờ John chốt số ý bài 1 (quyết định 1) — đây là biến số chặn nhiều chỗ nhất; (b) sửa các lỗi đã liệt kê ở C2 (1 ô), C5 (ví dụ số pin), C11 (bảng tiền v2 dòng 320), C14 (draft v2 dòng 155) — các sửa này không cần John; (c) ghi "CHỜ ĐỔI TIÊU ĐỀ" cho bài 35 trong bảng 40 bài.
3. **Kiểm tra lại sau khi dựng master:** đối chiếu từng mục master với bảng ở mục 3 của bản này; chạy kiểm tra số ý bài 1 (grep "19 ý" / "21 ý" trong master phải bằng 0 sau khi đồng bộ, trừ khi ghi rõ là lịch sử); kiểm tra mọi link tới file gốc còn đúng đường dẫn.
4. **Những gì bản này KHÔNG rà:** file ngoài thư mục `files/` (vd file trong `source/` trên GitHub — giả định đã đồng bộ với local; nếu master builder thấy lệch thì ghi thêm); nội dung 8 ý bài 1 còn thiếu ảnh AI (chờ quyết định 1); giá/review Amazon tại thời điểm đăng (phải kiểm tra lại — xem C10).
