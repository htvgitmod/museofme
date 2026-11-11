# Track 5 — Directory & Glossary, cụm G: Khoa học / Công nghệ / Dữ liệu / Lịch sử

Count: 60 / 100

## Trạng thái (11/11/2026)
- Đã xong 60 thẻ: G3 (20) + G4 (20) + G5 (20) — 30 Directory + 30 Glossary.
- THIẾU 40 thẻ: G1 (Vật lý / Thiên văn / Vũ trụ / Địa chất, 20 thẻ) và G2 (Sinh học / Y sinh / Môi trường / Khoa học thực phẩm, 20 thẻ) — 2 agent phụ trách 2 cụm này lỗi inference proxy 429 (rate limit) ngay khi khởi động, không ghi được file nào. Theo quy tắc hard-stop 429, KHÔNG thử lại / không spawn thay thế trong lượt này — parent cần sắp xếp lại sau khi rate limit hết.
- File staging từng cụm giữ nguyên: track5-directory-glossary-g3.md, -g4.md, -g5.md. Không sửa file đếm hay file continuous nào khác.
- Kiểm tra trùng chéo G3/G4/G5: không trùng tiêu đề/cặp chủ đề × format giữa 3 cụm. G5-D8 (thí nghiệm làm ở nhà) thuộc G5, không trùng G1 (chưa có).
- Caveat kiểm chứng gốc: G4 chỉ kiểm chứng được 4/20 gốc bằng browser.search (lượt search thứ hai bị 429, đã dừng, không retry) — 16 thẻ còn lại ghi rõ "chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng", không bịa URL/số. G3 kiểm chứng 4 gốc, G5 kiểm chứng 4 gốc; các gốc còn lại là homepage tên tuổi lớn, số chưa xác minh ghi "chưa kiểm chứng".

## Làm ngay
**Làm ngay: G3-D2. "AI chạy trên máy mình" — directory model AI chạy local, lọc theo RAM máy bạn (★5).** Lý do: đúng cơn khát AI miễn phí/không tốn token, đúng niche "AI cho marketer" của John, seed 60 model, làm 2 buổi, nối được với G3-G9 và G3-G3 thành cụm AI local. (Làm ngay từng cụm: G4-D3 Directory di sản UNESCO đang gặp nguy hiểm; G5-D2 Số liệu lịch sử Việt Nam qua 100 năm.)


---

# Track 5 — Directory & Glossary, cụm G3: Công nghệ / AI / Phần mềm / Dữ liệu / An ninh mạng

Count: 20 / 20

Phạm vi: chỉ công nghệ, AI, phần mềm, dữ liệu, an ninh mạng, blockchain, chip, internet.
Không lấn sang vật lý, sinh học, lịch sử, toán. Không làm list tĩnh "100 X".
Directory = database tra cứu được (tìm kiếm + lọc, mỗi mục có dữ liệu cấu trúc).
Glossary = tra cứu thuật ngữ (định nghĩa 2 dòng + ví dụ thật + phân biệt thuật ngữ gần giống).
Tránh trùng: D1 (tool AI cho marketer), D2 (tool AI cho giáo viên), D3 (thay thế phần mềm chung),
D10 (prompt tiếng Việt), #1187 (100 thuật ngữ AI chung), #1189 (thuật ngữ tài chính),
#1196 (thuật ngữ y khoa), #1062 (glossary mô hình tư duy), D11 (thiên kiến), D12 (SEO),
D13 (UX/UI), D14 (đàm phán), D15 (cà phê), #1185 (list 100 API miễn phí),
#1186 (list 100 prompt AI), #1191 (list 100 thuật ngữ crypto), #1316 (mật khẩu),
T3 #437/#444/#446 (thẻ lệ phí thi chứng chỉ cloud — đã Không duyệt, không làm dạng tra phí).
Tất cả "Chờ duyệt".

## DIRECTORY (10 thẻ)

### G3-D1. "Bỏ SaaS, tự host lấy" — directory phần mềm mã nguồn mở thay SaaS trả phí, lọc theo tiền tiết kiệm được — ★5 — Chờ duyệt
Mô tả: Gõ tool đang trả tiền (Notion, Slack, Calendly, Mailchimp...) ra bản mã nguồn mở
tự host tương đương, kèm: thay được bao nhiêu $/tháng, chạy bằng 1 lệnh Docker không,
cần VPS bao nhiêu RAM, độ khó cài đặt. Lọc theo việc cần làm, theo giấy phép (MIT/AGPL),
theo "chạy được trên VPS $5/tháng".
Khác D3 (thay thế phần mềm chung, giá VND, vote cộng đồng): đây chỉ làm bản tự host
cho dev/chủ shop tech, có lệnh cài chạy được ngay và cột "tiết kiệm $/tháng".
Gốc: awesome-selfhosted — danh sách phần mềm tự host lớn nhất GitHub, chia theo nhóm
(Analytics, CRM, chat, lưu trữ...), mỗi mục ghi license + ngôn ngữ.
Link: https://github.com/awesome-selfhosted/awesome-selfhosted
(Kiểm chứng 11/11 qua search: bản gist mirror của list ghi rõ "Free Software network
services... hosted locally", kèm license từng mục; Uptime Kuma 93,5k star, Coolify 65,9k star.)
Trục đổi: đổi cách hiển thị (list GitHub dài khô → directory lọc theo "tool đang trả tiền
+ tiền tiết kiệm được") + đổi ngách (dev tự host toàn cầu → chủ shop/dev VN muốn cắt phí SaaS).
SCAMPER: Adapt (thêm cột "VPS $5/tháng chạy được không" + lệnh Docker copy-paste) +
Eliminate (bỏ hàng nghìn mục, chỉ giữ ~150 bản thay thế SaaS phổ biến nhất).
TRIZ: phân đoạn (chia theo SaaS đang trả tiền) + tự phục vụ (người dùng tự cài, không cần mình vận hành).
Tiền: ads + affiliate VPS (DigitalOcean/Vultr — hoa hồng giới thiệu) + gói "bộ tự host cho shop"
(PDF hướng dẫn cài 5 tool) 49k.
Làm: 2–3 buổi (seed 150 mục, mỗi mục có lệnh Docker + mức tiết kiệm).

### G3-D2. "AI chạy trên máy mình" — directory model AI chạy local, lọc theo RAM máy bạn — ★5 — Chờ duyệt
Mô tả: Chọn RAM máy (8GB/16GB/32GB) + việc cần làm (chat, viết code, tóm tắt tài liệu)
ra model chạy offline được, kèm: dung lượng tải về, tốc độ, chất lượng so với bản cloud,
lệnh chạy 1 dòng. Không cần API key, không tốn tiền token, dữ liệu không rời khỏi máy.
Khác D1 (tool AI cho marketer, đa số cloud): đây chỉ model chạy local/offline cho dev
và người cần riêng tư.
Gốc: Ollama Library — thư viện model mở (Llama, Gemma, Mistral, Qwen-Coder...), chạy
bằng 1 lệnh `ollama run`, có bản 1–3B chạy trên laptop CPU tới 70B+ cần GPU mạnh.
Link: https://ollama.com/library
(Kiểm chứng 11/11 qua search: Ollama là runtime mã nguồn mở, model 8B ~4,7GB, cần tối thiểu
8GB RAM; chạy qua API local tại localhost:11434.)
Trục đổi: đổi cách hiển thị (thư viện model theo tên → tra cứu theo "RAM máy tôi + việc tôi cần")
+ đổi ngách (dev quốc tế → dev/người dùng VN máy yếu, sợ tốn tiền API).
SCAMPER: Substitute (thay "chọn model theo benchmark" bằng "chọn model theo RAM máy bạn") +
Combine (directory + lệnh chạy copy-paste + bảng so sánh chất lượng/tốc độ).
TRIZ: phân đoạn (chia theo RAM) + sao chép (bản local rẻ của model cloud đắt).
Tiền: ads + affiliate laptop/VPS GPU + gói "bộ model local cho dev" (cấu hình mẫu + prompt) 39k.
Làm: 2 buổi (seed 60 model, test RAM yêu cầu theo tài liệu chính thức).

### G3-D3. "Dataset để luyện AI" — directory dataset huấn luyện/fine-tune model, lọc theo task + giấy phép — ★4 — Chờ duyệt
Mô tả: Chọn task (phân loại văn bản, hỏi-đáp, nhận diện ảnh, giọng nói...) + ngôn ngữ
(có tiếng Việt không) + giấy phép dùng thương mại được không, ra dataset kèm: kích thước,
số mẫu, 1 đoạn code load dataset chạy được ngay, và 1 notebook mẫu. Lọc thêm theo
"dataset nhỏ, laptop chạy được" cho người mới.
Khác D6 (dataset về thị trường VN): đây là dataset luyện model AI, tệp dev/AI toàn cầu + VN.
Gốc: Hugging Face Datasets Hub — kho dataset ML lớn (SQuAD hỏi-đáp, IMDb cảm xúc, MNIST ảnh
chữ viết tay, Common Voice giọng nói...), mỗi dataset có Dataset Card ghi task/license.
Link: https://huggingface.co/datasets
(Kiểm chứng 11/11 qua search: Hub được mô tả có hơn 1,5 triệu dataset (nguồn thứ cấp, chưa kiểm
chứng độc lập); load bằng 1 dòng `load_dataset(...)`; SQuAD/IMDb/MNIST là dataset chuẩn.)
Trục đổi: đổi cách hiển thị (kho dataset khổng lồ khó tìm → tra cứu theo task + "laptop chạy được")
+ đổi ngách (nhà nghiên cứu → dev VN tự học AI, sinh viên làm đồ án).
SCAMPER: Adapt (thêm cột "có tiếng Việt không" + code mẫu tiếng Việt) + Eliminate
(bỏ dataset hàng TB, chỉ giữ dataset dưới 1GB cho người mới).
TRIZ: phân đoạn (chia theo task) + đa năng (1 dataset dùng cho nhiều bài học).
Tiền: ads + affiliate khóa học AI + gói dataset "đã làm sạch + notebook mẫu" Pro 49k/tháng.
Làm: 2–3 buổi (seed 80 dataset, mỗi dataset có code load + notebook mẫu).

### G3-D4. "Extension VS Code theo việc" — directory extension theo việc cần làm, không theo tên — ★4 — Chờ duyệt
Mô tả: Gõ việc đang làm ("format code Python", "so sánh 2 file", "viết commit message bằng AI")
ra extension phù hợp, kèm: miễn phí hay trả phí, sao/lượt tải, có chậm máy không,
có xung đột với extension phổ biến không. Lọc theo ngôn ngữ lập trình + theo việc.
Khác D1/D3: tệp hẹp là dev dùng VS Code, tiêu chí chọn là "việc cần làm" chứ không phải tên tool.
Gốc: Visual Studio Code Marketplace — chợ extension chính thức của VS Code, tìm/lọc theo
danh mục, lượt tải, đánh giá.
Link: https://marketplace.visualstudio.com
Trục đổi: đổi cách hiển thị (chợ extension theo tên/danh mục → tra cứu theo việc cần làm) +
đổi ngách (dev toàn cầu → dev VN mới học code, không biết tên extension).
SCAMPER: Substitute (thay xếp hạng lượt tải bằng "giải quyết được việc gì") + Combine
(directory + bộ extension gợi ý theo nghề: "bộ cho dev web", "bộ cho dev Python").
TRIZ: phân đoạn (chia theo việc) + gộp (nhiều extension thành 1 bộ cài).
Tiền: ads + affiliate khóa học lập trình + gói "bộ extension theo nghề" (file settings.json
cài 1 lần) 29k.
Làm: 1–2 buổi (seed 100 extension, test xung đột với các extension phổ biến).

### G3-D5. "Trợ lý code AI nào hợp tôi" — directory tool AI viết/review code, lọc theo IDE + ngôn ngữ — ★4 — Chờ duyệt
Mô tả: Chọn IDE đang dùng (VS Code, JetBrains, Neovim) + ngôn ngữ chính (Python, JS, Go...)
+ ngân sách (miễn phí / dưới $20/tháng) ra tool AI code phù hợp, kèm: mạnh ở viết code mới
hay sửa bug hay review, có chạy offline không, có đọc được cả repo không. Có bảng so sánh
đặt cạnh nhau 3 tool.
Khác D1 (tool AI cho marketer): tệp dev, tiêu chí IDE/ngôn ngữ. Khác G3-D2 (model chạy local):
đây là sản phẩm trợ lý code hoàn chỉnh, cả cloud lẫn local.
Gốc: Product Hunt — nơi các trợ lý code AI (Cursor, Copilot, Codeium/Windsurf...) ra mắt
và được dev bình chọn, kèm review thật.
Link: https://www.producthunt.com
Trục đổi: đổi cách hiển thị (feed ra mắt rời rạc → directory so sánh theo IDE + ngôn ngữ) +
đổi ngách (dev toàn cầu → dev VN, thêm cột "thanh toán được không / có free tier thật không").
SCAMPER: Adapt (thêm cột thanh toán VN + free tier thật) + Combine (directory + bảng so sánh
3 tool cạnh nhau).
TRIZ: phân đoạn (chia theo IDE/ngôn ngữ) + thay đổi cách hiển thị (bảng so sánh thay vì list).
Tiền: ads + affiliate tool AI code (hoa hồng đăng ký) + phí đăng tool nổi bật.
Làm: 2 buổi (seed 40 tool, bảng so sánh theo 6 tiêu chí).

### G3-D6. "Web tôi có bị hack được không" — directory tool quét bảo mật web miễn phí, lọc theo loại lỗ hổng — ★5 — Chờ duyệt
Mô tả: Chọn loại cần kiểm tra (tiêu đề bảo mật, TLS/HTTPS, SQL injection, XSS, mật khẩu lộ...)
ra tool quét miễn phí phù hợp, kèm: quét thụ động (an toàn, quét web đang chạy) hay quét
chủ động (chỉ quét web staging của mình), cần cài đặt hay chạy online, báo cáo đọc thế nào.
Có checklist "quét xong sửa cái gì trước" theo OWASP Top 10. Chỉ quét web của chính mình.
Khác T3 #832 (tool kiểm tra shop lộ dữ liệu — form nhập cách lưu dữ liệu → checklist):
đây là directory tool quét thật (chạy được), không phải form hỏi-đáp.
Gốc: OWASP — danh sách công cụ quét lỗ hổng web (ZAP miễn phí mã nguồn mở, Burp Suite
Community, Mozilla Observatory, SecurityHeaders.com...), phân loại DAST/SAST/SCA.
Link: https://community.owasp.org/Vulnerability_Scanning_Tools
(Kiểm chứng 11/11 qua search: OWASP liệt kê tool theo bảng gồm license/nền tảng; ZAP là scanner
miễn phí phổ biến nhất, chạy được qua Docker và tích hợp CI/CD; chỉ quét hệ thống mình có quyền.)
Trục đổi: đổi cách hiển thị (bảng tool dài khô → tra cứu theo "tôi sợ bị hack kiểu gì") +
đổi ngách (chuyên gia bảo mật → chủ shop/dev VN không rành bảo mật).
SCAMPER: Adapt (thêm hướng dẫn đọc báo cáo bằng tiếng Việt + checklist sửa theo thứ tự) +
Eliminate (bỏ tool trả phí, chỉ giữ tool miễn phí).
TRIZ: phân đoạn (chia theo loại lỗ hổng OWASP Top 10) + tự phục vụ (chủ web tự quét, tự sửa).
Tiền: ads + affiliate dịch vụ audit bảo mật + gói "báo cáo quét + hướng dẫn sửa" 99k/lần.
Làm: 2 buổi (seed 40 tool, test 5 tool miễn phí chạy online trên web demo).

### G3-D7. "Học code miễn phí theo lộ trình" — directory khóa/lộ trình lập trình miễn phí, lọc theo nghề + thời gian — ★4 — Chờ duyệt
Mô tả: Chọn nghề muốn làm (web frontend, backend, data, mobile...) + thời gian có
(dưới 5 giờ/tuần, 3 tháng đổi nghề...) ra lộ trình học miễn phí từng bước, kèm: học cái gì
trước, bài tập thực hành nào, học xong làm được dự án gì, có chứng chỉ không. Lọc theo
ngôn ngữ (Python/JS...) và "có tiếng Việt không".
Khác D8 (khóa học miễn phí có chứng chỉ, theo nghề chung): đây chỉ lập trình, có lộ trình
từng bước + dự án cuối, không phải list khóa rời.
Gốc: roadmap.sh — bản đồ lộ trình dev (frontend, backend, DevOps, AI...) từng bước, kèm
tài nguyên miễn phí từng chặng; freeCodeCamp — khóa lập trình miễn phí có chứng chỉ.
Link: https://roadmap.sh
Trục đổi: đổi cách hiển thị (bản đồ lộ trình chung → tra cứu theo "nghề + thời gian tôi có") +
đổi ngách (dev toàn cầu → người VN muốn đổi nghề sang IT, cần biết học bao lâu thì đi làm được).
SCAMPER: Adapt (thêm cột "học xong làm được dự án gì" + "mất bao lâu thì xin được việc") +
Combine (lộ trình + khóa miễn phí + dự án thực hành từng chặng).
TRIZ: phân đoạn (chia lộ trình thành chặng 2 tuần) + thay đổi cách hiển thị (timeline thay vì list).
Tiền: ads + affiliate khóa học trả phí/bootcamp + gói "lộ trình + mentor check dự án" 199k.
Làm: 2 buổi (seed 30 lộ trình theo nghề, mỗi lộ trình 5–8 chặng).

### G3-D8. "Chọn database nào" — directory cơ sở dữ liệu theo use case, so sánh đặt cạnh nhau — ★4 — Chờ duyệt
Mô tả: Chọn use case (web bán hàng, chat realtime, tìm kiếm, AI/vector, phân tích dữ liệu...)
+ quy mô (vài nghìn hay vài triệu bản ghi) + ngân sách, ra database phù hợp kèm bảng so sánh:
mạnh/yếu ở đâu, khó học không, host ở đâu rẻ, khi nào thì đổi sang loại khác. Có cây quyết định
"trả lời 3 câu hỏi → ra database".
Khác D6 (dataset VN): đây là chọn hệ quản trị database, tệp dev/backend.
Gốc: DB-Engines Ranking — bảng xếp hạng độ phổ biến của hệ database (PostgreSQL, MySQL,
MongoDB, Redis, vector DB...), có mô tả từng hệ + xu hướng theo tháng.
Link: https://db-engines.com/en/ranking
Trục đổi: đổi cách hiển thị (bảng xếp hạng độ phổ biến → tra cứu theo use case + cây quyết định) +
đổi ngách (kiến trúc sư hệ thống → dev VN làm side project, cần chọn nhanh không học thừa).
SCAMPER: Substitute (thay "phổ biến nhất" bằng "hợp use case của bạn nhất") + Combine
(directory + cây quyết định 3 câu hỏi + bảng so sánh).
TRIZ: phân đoạn (chia theo use case) + đảo ngược (hỏi nhu cầu trước, gợi ý database sau).
Tiền: ads + affiliate cloud/hosting database + gói "thiết kế schema mẫu theo use case" 49k.
Làm: 2 buổi (seed 40 database, cây quyết định + bảng so sánh 6 tiêu chí).

### G3-D9. "Khởi đầu project trong 5 phút" — directory boilerplate/starter template theo stack — ★4 — Chờ duyệt
Mô tả: Chọn stack (Next.js, Laravel, Flutter, Django...) + tính năng cần sẵn (đăng nhập,
thanh toán, gửi mail, admin...) ra starter template kèm: có sẵn tính năng gì, cần bao nhiêu
phút để chạy, giấy phép, còn được cập nhật không. Lọc theo "có auth + payment sẵn" cho
người làm side project bán hàng.
Gốc: Vercel Templates — kho template deploy 1 click (Next.js, AI, thương mại điện tử...),
mỗi template ghi stack + tính năng + nút deploy.
Link: https://vercel.com/templates
Trục đổi: đổi cách hiển thị (kho template theo framework → tra cứu theo "tính năng tôi cần sẵn") +
đổi ngách (dev toàn cầu → dev VN làm side project, cần auth + thanh toán VN).
SCAMPER: Adapt (thêm cột "gắn thanh toán VN được không" + "deploy miễn phí ở đâu") +
Eliminate (bỏ template không còn cập nhật trên 1 năm).
TRIZ: phân đoạn (chia theo tính năng cần sẵn) + sao chép (dùng lại khung có sẵn thay vì code từ đầu).
Tiền: ads + affiliate hosting/deploy + phí đăng template nổi bật (tác giả trả để lên top).
Làm: 1–2 buổi (seed 80 template, kiểm tra ngày cập nhật gần nhất).

### G3-D10. "Làm app không cần biết code" — directory tool no-code/low-code theo việc cần làm — ★4 — Chờ duyệt
Mô tả: Gõ việc cần làm ("làm web bán hàng", "làm app đặt lịch", "tự động hóa nhập liệu...")
ra tool no-code phù hợp, kèm: làm được tới đâu thì đụng trần (giới hạn bản miễn phí),
giá khi vượt trần, có xuất dữ liệu ra được không (tránh bị khóa), có cộng đồng VN không.
Lọc theo việc + ngân sách.
Khác T3 (webapp form→AI→file cho tệp VN cụ thể): đây là directory chọn tool no-code,
không phải 1 tool giải 1 pain.
Gốc: NoCode.tech — directory tool no-code (Bubble, Webflow, Glide, Airtable...), chia theo
loại tool + tutorial kèm theo.
Link: https://www.nocode.tech
Trục đổi: đổi cách hiển thị (directory theo loại tool → tra cứu theo việc cần làm + "đụng trần ở đâu")
+ đổi ngách (maker toàn cầu → chủ shop/người không rành tech ở VN).
SCAMPER: Adapt (thêm cột "đụng trần bản miễn phí ở đâu" + "xuất dữ liệu ra được không") +
Combine (directory + tutorial tiếng Việt ngắn cho từng tool).
TRIZ: tách ra (chỉ lấy phần "chọn tool", không dạy dùng tool) + thay đổi cách hiển thị (theo việc).
Tiền: ads + affiliate tool no-code + gói "bộ tool no-code cho shop" (hướng dẫn setup) 49k.
Làm: 2 buổi (seed 60 tool, ghi rõ giới hạn bản miễn phí từng tool).

## GLOSSARY (10 thẻ)

### G3-G1. Glossary an ninh mạng A–Z — mỗi thuật ngữ 1 vụ tấn công thật + cách phòng — ★5 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ bảo mật (CVE, zero-day, phishing, ransomware, SQL injection, XSS,
CSRF, DDoS, MITM...): định nghĩa 2 dòng + 1 vụ tấn công thật đã xảy ra + "phòng bằng cách nào
trong 5 phút" + phân biệt với thuật ngữ gần giống (ví dụ: XSS khác SQL injection ở đâu,
phishing khác smishing ở đâu). Tìm kiếm + lọc theo tình huống (chủ web, dev, người dùng thường).
Khác #1316 (mật khẩu — chỉ 1 chủ đề mật khẩu, dạng list): đây là glossary tra cứu đầy đủ
an ninh mạng, có vụ thật + cách phòng.
Gốc: OWASP Top 10 — 10 rủi ro bảo mật web lớn nhất, mỗi rủi ro có mô tả + ví dụ tấn công +
cách phòng; CVE MITRE — kho lỗ hổng chuẩn thế giới.
Link: https://owasp.org/www-project-top-ten/
Trục đổi: đổi cách hiển thị (tài liệu OWASP học thuật → glossary có vụ thật + cách phòng 5 phút) +
đổi ngách (chuyên gia bảo mật → dev/chủ shop VN).
SCAMPER: Adapt (ví dụ tấn công quốc tế → thêm vụ ở VN khi có) + Combine (glossary + checklist
phòng 5 phút + phân biệt thuật ngữ gần giống).
TRIZ: phân đoạn (chia theo OWASP Top 10) + đa năng (1 thuật ngữ phục vụ cả dev lẫn chủ web).
Tiền: ads + affiliate tool bảo mật (trình quét, password manager) + poster "10 lỗ hổng web"
bản in 49k.
Làm: 2–3 buổi (seed 100 thuật ngữ, mỗi thuật ngữ có vụ thật + cách phòng).

### G3-G2. Glossary blockchain/Web3 A–Z — mỗi thuật ngữ 1 ví dụ giao dịch thật + phân biệt — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ blockchain (smart contract, gas fee, PoW/PoS, NFT, DAO, bridge,
layer 2, wallet nóng/lạnh...): định nghĩa 2 dòng + ví dụ giao dịch thật + phân biệt cặp
dễ nhầm (coin khác token ở đâu, PoW khác PoS ở đâu, ví nóng khác ví lạnh ở đâu). Tìm kiếm +
lọc theo "người mới / dev / nhà đầu tư".
Khác #1191 (list 100 thuật ngữ crypto — list tĩnh, giải thích không dùng từ khó): đây là
glossary tra cứu có ví dụ giao dịch thật + phân biệt cặp nhầm + lọc theo đối tượng.
Gốc: Ethereum.org Developer Docs — tài liệu chuẩn về smart contract, gas, PoS, layer 2,
viết cho dev, có ví dụ code.
Link: https://ethereum.org/en/developers/docs/
Trục đổi: đổi cách hiển thị (tài liệu dev khô → glossary có ví dụ giao dịch thật + phân biệt) +
đổi topic (chỉ định nghĩa → định nghĩa + ví dụ + phân biệt).
SCAMPER: Adapt (ví dụ dev → ví dụ giao dịch ai cũng hiểu) + Combine (glossary + mục "cặp dễ nhầm").
TRIZ: phân đoạn (chia theo đối tượng: mới/dev/đầu tư) + thay đổi cách hiển thị (cặp đối chiếu).
Tiền: ads + affiliate sàn/ví (hoa hồng giới thiệu) + gói "checklist trước khi giao dịch" 29k.
Làm: 2 buổi (seed 80 thuật ngữ, mỗi thuật ngữ có ví dụ + phân biệt).
Lưu ý: chỉ giải thích thuật ngữ, không tư vấn đầu tư, không gợi ý mua coin nào.

### G3-G3. Glossary LLM engineering cho dev — RAG, fine-tune, token, embedding... kèm đoạn code ví dụ — ★5 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ làm việc với LLM (RAG, fine-tuning, prompt, token, context window,
embedding, vector DB, hallucination, agent, temperature...): định nghĩa 2 dòng + 1 đoạn code
hoặc ví dụ chạy thật + phân biệt cặp dễ nhầm (RAG khác fine-tuning ở đâu, embedding khác
keyword search ở đâu, agent khác chatbot ở đâu). Lọc theo "đang làm chatbot / tìm kiếm / agent".
Khác #1187 (100 thuật ngữ AI chung cho người mới — list tĩnh): đây là glossary cho dev,
mỗi thuật ngữ có code ví dụ + phân biệt kỹ thuật, đổi hẳn tệp và format.
Gốc: Hugging Face LLM Course — khóa học LLM miễn phí, giải thích RAG/fine-tuning/embedding
kèm code chạy được.
Link: https://huggingface.co/learn/llm-course
Trục đổi: đổi ngách (người mới tìm hiểu AI → dev đang build sản phẩm LLM) + đổi cách hiển thị
(list thuật ngữ → glossary có code ví dụ + phân biệt cặp nhầm).
SCAMPER: Adapt (bài học dài → tra cứu từng thuật ngữ kèm code) + Combine (glossary + code mẫu
chạy được + bảng "khi nào dùng RAG, khi nào fine-tune").
TRIZ: phân đoạn (chia theo việc đang làm: chatbot/tìm kiếm/agent) + đa năng (1 thuật ngữ
dùng cho nhiều bài toán).
Tiền: ads + affiliate API LLM/khóa học AI + gói "mẫu code RAG + fine-tune" 49k.
Làm: 2–3 buổi (seed 80 thuật ngữ, mỗi thuật ngữ có code ví dụ ngắn).

### G3-G4. Glossary cơ sở dữ liệu A–Z — mỗi thuật ngữ 1 câu truy vấn ví dụ + phân biệt — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ database (index, transaction, ACID, sharding, replication, JOIN,
normalization, deadlock...): định nghĩa 2 dòng + 1 câu SQL ví dụ thật + "sai lầm thường gặp"
+ phân biệt cặp dễ nhầm (index khác primary key ở đâu, SQL khác NoSQL ở đâu, sharding khác
replication ở đâu). Lọc theo "đang học / đang làm backend / đang tối ưu tốc độ".
Gốc: PostgreSQL Documentation — tài liệu chuẩn về transaction, index, replication...,
có ví dụ SQL chạy được.
Link: https://www.postgresql.org/docs/
Trục đổi: đổi cách hiển thị (tài liệu tham khảo khô → glossary có câu SQL ví dụ + sai lầm) +
đổi ngách (DBA chuyên nghiệp → dev VN tự học backend).
SCAMPER: Adapt (ví dụ tài liệu → ví dụ trên dữ liệu shop/order ai cũng hiểu) + Combine
(glossary + mục "sai lầm thường gặp" + câu SQL chạy được).
TRIZ: phân đoạn (chia theo tình huống: học/làm/tối ưu) + thay đổi cách hiển thị (cặp đối chiếu).
Tiền: ads + affiliate hosting database/khóa backend + gói "50 câu SQL mẫu theo tình huống" 29k.
Làm: 2 buổi (seed 80 thuật ngữ, mỗi thuật ngữ có câu SQL ví dụ).

### G3-G5. Glossary mạng & Internet A–Z — mỗi thuật ngữ 1 ví dụ "khi web chậm thì do cái nào" — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ mạng (DNS, CDN, TCP/UDP, latency, bandwidth, SSL/TLS, HTTP/HTTPS,
IP, VPN, firewall...): định nghĩa 2 dòng + ví dụ đời thường ("web chậm là do DNS hay do
server?") + phân biệt cặp dễ nhầm (latency khác bandwidth ở đâu, HTTP khác HTTPS ở đâu,
TCP khác UDP ở đâu). Lọc theo "web chậm / không vào được web / sợ bị nghe lén".
Gốc: MDN Web Docs — tài liệu web chuẩn (HTTP, DNS, TLS...), viết cho dev, có sơ đồ luồng
request.
Link: https://developer.mozilla.org/en-US/docs/Web
Trục đổi: đổi cách hiển thị (tài liệu kỹ thuật → glossary gắn với triệu chứng "web chậm,
không vào được") + đổi ngách (dev web → dev mới + chủ shop tự quản web).
SCAMPER: Adapt (định nghĩa kỹ thuật → ví dụ "web chậm thì do cái nào") + Combine
(glossary + cây chẩn đoán "web chậm → kiểm tra cái nào trước").
TRIZ: đảo ngược (hỏi triệu chứng trước, tra thuật ngữ sau) + phân đoạn (chia theo triệu chứng).
Tiền: ads + affiliate hosting/CDN + gói "checklist web chậm" 29k.
Làm: 2 buổi (seed 70 thuật ngữ, mỗi thuật ngữ có ví dụ triệu chứng + phân biệt).

### G3-G6. Glossary DevOps/Cloud A–Z — mỗi thuật ngữ 1 lệnh ví dụ + phân biệt — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ DevOps/Cloud (CI/CD, container, Kubernetes, Docker, pipeline,
deploy, rollback, monitoring, IaC...): định nghĩa 2 dòng + 1 lệnh hoặc file cấu hình ví dụ
thật + phân biệt cặp dễ nhầm (Docker khác Kubernetes ở đâu, CI khác CD ở đâu, deploy khác
release ở đâu). Lọc theo "mới deploy lần đầu / đang bị sập / muốn tự động hóa".
Gốc: Kubernetes Documentation — tài liệu chuẩn về container/orchestration, có ví dụ
file YAML chạy được.
Link: https://kubernetes.io/docs/
Trục đổi: đổi cách hiển thị (tài liệu nền tảng khô → glossary có lệnh ví dụ + phân biệt) +
đổi ngách (kỹ sư DevOps → dev VN tự deploy side project).
SCAMPER: Adapt (ví dụ hệ thống lớn → ví dụ deploy 1 web nhỏ trên VPS) + Combine
(glossary + lệnh copy-paste + mục "khi nào cần, khi nào chưa cần").
TRIZ: phân đoạn (chia theo tình huống deploy) + tách ra (chỉ lấy phần "hiểu để deploy được",
bỏ lý thuyết sâu).
Tiền: ads + affiliate VPS/cloud + gói "file deploy mẫu cho 5 stack" 39k.
Làm: 2 buổi (seed 70 thuật ngữ, mỗi thuật ngữ có lệnh/file ví dụ).

### G3-G7. Glossary Git & version control A–Z — mỗi thuật ngữ 1 lệnh ví dụ + "lỡ tay thì sửa sao" — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ Git (branch, merge, rebase, conflict, stash, cherry-pick, pull request,
fork, HEAD...): định nghĩa 2 dòng + 1 lệnh ví dụ thật + mục "lỡ tay thì sửa sao"
(commit nhầm, push nhầm branch, merge conflict) + phân biệt cặp dễ nhầm (merge khác rebase
ở đâu, fetch khác pull ở đâu, fork khác clone ở đâu). Lọc theo "mới học / đang bị lỗi".
Khác các thẻ Git lẻ trong T1/T3 (nếu có, dạng bài distill/tool): đây là glossary tra cứu
đầy đủ kèm "cứu hộ lỡ tay".
Gốc: Git Documentation — tài liệu Git chính thức, có ví dụ lệnh từng thao tác.
Link: https://git-scm.com/doc
Trục đổi: đổi cách hiển thị (tài liệu lệnh khô → glossary có mục "lỡ tay thì sửa sao") +
đổi ngách (dev chuyên nghiệp → dev mới/sinh viên VN hay commit nhầm).
SCAMPER: Adapt (thêm mục cứu hộ lỡ tay — nỗi đau thật của dev mới) + Combine (glossary +
bảng "lỗi thường gặp → lệnh sửa").
TRIZ: đảo ngược (tra cứu từ lỗi gặp phải, không phải từ tên lệnh) + tự phục vụ (tự sửa, không cần hỏi senior).
Tiền: ads + affiliate khóa Git/khóa lập trình + gói "cheat sheet Git in 1 trang" 19k.
Làm: 1–2 buổi (seed 60 thuật ngữ, mỗi thuật ngữ có lệnh + cách sửa lỡ tay).

### G3-G8. Glossary thuật toán & cấu trúc dữ liệu A–Z — mỗi thuật ngữ 1 ví dụ code + độ phức tạp — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật toán/cấu trúc dữ liệu (Big-O, hash map, cây, đồ thị, sort, binary search,
recursion, dynamic programming...): định nghĩa 2 dòng + 1 đoạn code ví dụ ngắn + độ phức tạp
(O(n), O(log n)...) + "dùng khi nào" + phân biệt cặp dễ nhầm (array khác linked list ở đâu,
BFS khác DFS ở đâu, sort nào nhanh khi nào). Lọc theo "phỏng vấn / tối ưu code chậm".
Gốc: VisuAlgo — trực quan hóa thuật toán/cấu trúc dữ liệu (sort, graph, tree...), xem từng
bước chạy, chuẩn giảng dạy đại học.
Link: https://visualgo.net/en
Trục đổi: đổi cách hiển thị (trang trực quan hóa từng thuật toán → glossary tra cứu có code +
độ phức tạp + "dùng khi nào") + đổi ngách (sinh viên CS → dev VN ôn phỏng vấn/tối ưu code).
SCAMPER: Adapt (thêm cột "dùng khi nào trong code thật" + độ phức tạp) + Combine
(glossary + link xem trực quan từng bước + code mẫu).
TRIZ: phân đoạn (chia theo tình huống: phỏng vấn/tối ưu) + thay đổi cách hiển thị
(chữ + hình động minh họa).
Tiền: ads + affiliate khóa phỏng vấn/khóa thuật toán + gói "50 câu phỏng vấn + đáp án" 49k.
Làm: 2–3 buổi (seed 70 thuật ngữ, mỗi thuật ngữ có code + độ phức tạp).

### G3-G9. Glossary chip & phần cứng A–Z — mỗi thuật ngữ 1 ví dụ "mua máy thì nhìn số nào" — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ chip/phần cứng (node 3nm, transistor, CPU/GPU/TPU, RAM, VRAM,
SSD NVMe, bus, TDP, benchmark...): định nghĩa 2 dòng + ví dụ mua sắm thật ("mua laptop
code AI thì nhìn RAM hay GPU?", "SSD NVMe khác SATA ở đâu khi mở máy") + phân biệt cặp
dễ nhầm (CPU khác GPU ở đâu, RAM khác VRAM ở đâu, node nhỏ có phải luôn nhanh hơn không).
Lọc theo "mua laptop / build PC / chạy AI local".
Gốc: Wikipedia — Glossary of computer hardware terms (danh sách chuẩn thuật ngữ phần cứng).
Link: https://en.wikipedia.org/wiki/Glossary_of_computer_hardware_terms
Trục đổi: đổi cách hiển thị (glossary Wikipedia khô → glossary gắn quyết định mua máy) +
đổi ngách (kỹ sư phần cứng → người VN mua laptop/PC, dev chạy AI local).
SCAMPER: Adapt (thêm cột "mua máy thì nhìn số nào" + ví dụ giá VN) + Combine
(glossary + bảng "máy nào chạy được model AI nào" nối G3-D2).
TRIZ: đảo ngược (hỏi "mua máy để làm gì" trước, tra thuật ngữ sau) + đa năng (1 thuật ngữ
dùng cho cả mua máy lẫn chạy AI).
Tiền: ads + affiliate laptop/linh kiện + gói "bảng chọn máy theo việc" 29k.
Làm: 2 buổi (seed 70 thuật ngữ, mỗi thuật ngữ có ví dụ mua sắm + phân biệt).

### G3-G10. Glossary lừa đảo online cho người dùng phổ thông — mỗi chiêu 1 tin nhắn thật + cách nhận biết — ★5 — Chờ duyệt
Mô tả: Tra cứu chiêu lừa online (phishing, smishing, vishing, giả shipper, giả công an,
lừa việc nhẹ lương cao, link trúng thưởng, mã QR lạ, deepfake gọi video...): định nghĩa
2 dòng + 1 tin nhắn/cuộc gọi lừa thật (đã che thông tin) + "nhận biết trong 10 giây bằng
dấu hiệu nào" + phân biệt cặp dễ nhầm (phishing khác smishing ở đâu, giả shipper khác
giả ngân hàng ở đâu). Tìm kiếm + lọc theo kênh (SMS/Zalo/Facebook/cuộc gọi).
Khác G3-G1 (glossary an ninh mạng cho dev/chủ web, thuật ngữ kỹ thuật CVE/XSS...): đây là
glossary cho người dùng phổ thông, mỗi chiêu có tin nhắn thật + dấu hiệu nhận biết, tệp
người lớn tuổi/chủ shop/người ít rành tech.
Gốc: FTC Consumer Advice — trang chống lừa đảo của Ủy ban Thương mại Liên bang Mỹ,
phân loại chiêu lừa theo kênh + dấu hiệu nhận biết.
Link: https://consumer.ftc.gov
Trục đổi: đổi ngách (người dùng Mỹ → người VN, tin nhắn lừa kiểu VN: giả shipper, giả công an,
việc nhẹ lương cao) + đổi cách hiển thị (bài cảnh báo dài → glossary tra cứu theo tin nhắn vừa nhận).
SCAMPER: Adapt (chiêu Mỹ → chiêu VN thật) + Reverse (tra cứu từ tin nhắn vừa nhận được,
không phải từ tên chiêu).
TRIZ: đảo ngược (nhập tin nhắn nghi ngờ → tra ra chiêu lừa) + tự phục vụ (tự nhận biết, không cần hỏi ai).
Tiền: ads + gói "bộ 30 tin nhắn lừa mẫu để dạy người nhà" 29k + hợp tác ngân hàng/shop
trả phí để gắn cảnh báo.
Làm: 2 buổi (seed 60 chiêu, mỗi chiêu có tin nhắn thật đã che + dấu hiệu nhận biết).

## Làm ngay

**Làm ngay: G3-D2. "AI chạy trên máy mình" — directory model AI chạy local, lọc theo RAM máy bạn.**
Lý do: đúng cơn khát "AI miễn phí, không tốn tiền token, dữ liệu không rời máy" của dev VN;
gốc Ollama đã kiểm chứng, seed chỉ 60 model, làm được trong 2 buổi, ra tiền rõ
(ads + affiliate VPS GPU + gói cấu hình mẫu). Nối được với G3-G9 (chọn máy chạy AI) và
G3-G3 (glossary LLM cho dev) thành cụm AI local hoàn chỉnh.

---

# Track 5 — Directory & Glossary, cụm G4: Lịch sử thế giới / Chiến tranh / Đế chế / Khảo cổ / Địa lý lịch sử

Count: 20 / 20

Phạm vi: CHỈ lịch sử thế giới, chiến tranh, đế chế, khảo cổ, địa lý lịch sử, bảo tàng/di tích thế giới. KHÔNG lấn lịch sử Việt Nam, khoa học tự nhiên, AI, toán.
Quy tắc: DIRECTORY = database tra cứu được (tìm kiếm + lọc theo tiêu chí, mỗi mục có dữ liệu cấu trúc), KHÔNG phải list tĩnh "100 X". GLOSSARY = tra cứu thuật ngữ (định nghĩa 2 dòng + ví dụ thật + phân biệt với thuật ngữ gần giống).
Kiểm chứng: 4 gốc đã kiểm chứng bằng browser.search ngày 11/11/2026 (UNESCO Danger List 58 di sản; Wikipedia List of largest empires — Anh 35,5 triệu km² năm 1920, Mông Cổ 24,0 triệu km²; British Museum Collection Online ~5 triệu hiện vật; Pantheon MIT Media Lab). Các gốc còn lại ghi tên nguồn uy tín + "link cần đối chiếu" — KHÔNG bịa URL, KHÔNG bịa số.
Chống trùng: đã grep KHO.md + track1-4-*.md. Ghi chú "khác thẻ …" ở những thẻ gần idea cũ. Tránh trùng #1062 (glossary mô hình tư duy), #1187 (thuật ngữ AI), #1189 (thuật ngữ tài chính), #1196 (thuật ngữ y khoa), D11 (thiên kiến), D12 (SEO), D13 (UX/UI), D14 (đàm phán), D15 (cà phê).
Tất cả status "Chờ duyệt". Ngôn ngữ giao diện tiếng Việt, nội dung lịch sử thế giới, tóm tắt bằng lời mình từ nguồn public domain / nguồn mở — không chép nguyên văn sách còn bản quyền.

## DIRECTORY (10 thẻ)

### G4-D1. Directory các trận chiến lớn trong lịch sử — tra theo thời đại, bên tham chiến, quy mô — ★5 — Chờ duyệt
Mô tả: Gõ tên trận, hoặc lọc theo thời đại (cổ đại / trung cổ / cận đại / thế chiến), khu vực, bên tham chiến, quy mô thương vong. Mỗi trận 1 dòng dữ liệu cấu trúc: năm, địa điểm, hai bên, chỉ huy, kết quả, vì sao trận này đổi cục diện — kèm bản đồ vị trí.
Khác thẻ #1243 (data viz "chiến tranh chết ít đi" — biểu đồ xu hướng 200 năm): đây là database tra cứu từng trận, không phải biểu đồ xu hướng.
Gốc: Wikipedia — List of battles (danh sách trận chiến theo thời kỳ) + Britannica (tóm tắt từng trận). Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi cách hiển thị (danh sách Wikipedia khô theo năm → database lọc đa tiêu chí + bản đồ) + đổi ngách (độc giả tiếng Anh → người Việt mê lịch sử quân sự, học sinh ôn thi).
SCAMPER: Adapt (thêm cột "vì sao đổi cục diện" + bản đồ) + Modify (lọc theo quy mô thương vong thay vì chỉ theo năm). TRIZ: phân đoạn (chia theo thời đại/khu vực).
Tiền: ads + affiliate sách lịch sử quân sự (Amazon) + gói premium "bản đồ trận chiến in được" 29k.
Làm: 2–3 buổi (seed 100 trận nổi tiếng nhất).

### G4-D2. Directory các đế chế lớn nhất lịch sử — so sánh diện tích, dân số, tuổi thọ — ★5 — Chờ duyệt
Mô tả: Bảng so sánh đế chế: lọc theo châu lục, thời kỳ, tôn giáo/ngôn ngữ chính. Mỗi đế chế: diện tích cực đại + năm đạt đỉnh, dân số ước tính, tồn tại bao lâu, thủ đô, vì sao sụp đổ. Có chế độ "đấu tay đôi": chọn 2 đế chế để so sánh trực diện.
Gốc: Wikipedia — List of largest empires. Link: https://en.m.wikipedia.org/wiki/List_of_largest_empires (Kiểm chứng 11/11: Đế quốc Anh 35,5 triệu km², 26,35% đất liền thế giới, đỉnh năm 1920; Mông Cổ 24,0 triệu km²; Nga 22,8 triệu km²; nhà Thanh 14,7 triệu km².)
Trục đổi: đổi cách hiển thị (bảng Wikipedia tĩnh → database so sánh + chế độ đấu tay đôi) + đổi ngách (độc giả học thuật → người Việt mê lịch sử, fan game chiến thuật).
SCAMPER: Combine (directory + tool so sánh trực diện) + Modify (thêm "tuổi thọ đế chế" làm tiêu chí xếp hạng). TRIZ: thay đổi cách hiển thị (bảng → so sánh trực quan).
Tiền: ads + affiliate sách/game chiến thuật (Age of Empires, Total War) + poster "bản đồ đế chế" bản số 29k.
Làm: 2 buổi (seed ~60 đế chế, dữ liệu diện tích/dân số đã có sẵn từ gốc).

### G4-D3. Directory di sản UNESCO đang gặp nguy hiểm — lọc theo mối đe dọa, xem di sản nào đã được cứu — ★5 — Chờ duyệt
Mô tả: Chỉ 58 di sản trong danh sách nguy hiểm của UNESCO (không phải toàn bộ 1.248 di sản): lọc theo loại đe dọa (chiến tranh, thiên tai, đô thị hóa, biến đổi khí hậu), theo châu lục, theo năm đưa vào danh sách. Mỗi di sản: vì sao gặp nguy, đang được cứu ra sao, và mục riêng "đã ra khỏi danh sách nguy hiểm" (câu chuyện cứu thành công).
Khác thẻ #1147 (1.223 di sản UNESCO × bản đồ + lọc theo nước — toàn bộ danh sách): đây chỉ làm nhóm nguy hiểm + góc "cứu hộ", dữ liệu cập nhật theo quyết định hằng năm của Ủy ban Di sản.
Gốc: UNESCO World Heritage Centre — List of World Heritage in Danger. Link: https://whc.unesco.org/en/list/?va&danger=1&mode=table (Kiểm chứng 11/11: 58 di sản trong danh sách nguy hiểm; 3 di sản vừa ra khỏi danh sách tháng 7/2025: Abu Mena — Ai Cập, Old Town of Ghadamès — Libya, Rainforests of the Atsinanana — Madagascar.)
Trục đổi: đổi topic (toàn bộ di sản → chỉ nhóm nguy hiểm) + đổi cách hiển thị (bảng UNESCO → lọc theo mối đe dọa + mục "đã được cứu").
SCAMPER: Eliminate (bỏ 1.190 di sản an toàn, chỉ giữ 58 ca khẩn) + Adapt (thêm timeline "vào/ra khỏi danh sách"). TRIZ: tách ra (chỉ lấy phần hay nhất — nhóm nguy hiểm).
Tiền: ads + affiliate tour du lịch di sản + donate (nút ủng hộ quỹ bảo tồn, hoa hồng giới thiệu) + bản premium "báo cáo cập nhật hằng năm".
Làm: 1–2 buổi (seed 58 di sản, dữ liệu có sẵn từ UNESCO).

### G4-D4. Directory bộ sưu tập cổ vật online miễn phí của các bảo tàng lớn — lọc theo nền văn minh, xem được ảnh độ phân giải cao — ★4 — Chờ duyệt
Mô tả: Không xếp hạng bảo tàng theo lượt thăm. Người dùng chọn nền văn minh (Ai Cập, La Mã, Hy Lạp, Maya, Trung Hoa...) → ra bảo tàng nào có bộ sưu tập online về nền văn minh đó, có ảnh độ phân giải cao/tour 3D không, có miễn phí dùng ảnh không (license CC). Mỗi bảo tàng kèm 3 hiện vật "xem trước" nổi bật nhất.
Khác thẻ #1184 (100 bảo tàng được thăm nhiều nhất — xếp hạng lượt thăm) và #1169 (lịch sử qua 100 đồ vật — kể chuyện theo đồ vật): đây là directory tra cứu theo nền văn minh + điều kiện dùng ảnh.
Gốc: British Museum — Collection Online. Link: https://www.britishmuseum.org/blog/how-explore-british-museum-home (Kiểm chứng 11/11: Collection Online cho truy cập gần 5 triệu hiện vật, hơn 1,9 triệu ảnh, đa số ảnh dùng miễn phí phi thương mại theo CC BY-NC-SA 4.0; 7.000+ hiện vật trên Google Arts & Culture.)
Trục đổi: đổi cách hiển thị (trang từng bảo tàng rời rạc → 1 directory gom theo nền văn minh) + đổi ngách (khách du lịch → người làm nội dung/giáo viên cần ảnh cổ vật miễn phí có license rõ ràng).
SCAMPER: Combine (directory bảo tàng + bộ lọc license ảnh) + Adapt (thêm "3 hiện vật xem trước" mỗi bảo tàng). TRIZ: gộp (nhiều bảo tàng vào 1 chỗ tra cứu).
Tiền: ads + affiliate sách lịch sử/bảo tàng + gói "pack ảnh cổ vật CC dùng làm slide" 29k.
Làm: 2 buổi (seed 30 bảo tàng lớn, mỗi bảo tàng 3 hiện vật).

### G4-D5. Directory di chỉ khảo cổ lớn thế giới — lọc theo thời kỳ, nền văn minh, có mở cửa tham quan không — ★4 — Chờ duyệt
Mô tả: Tra cứu di chỉ khảo cổ (Pompeii, Machu Picchu, Angkor, Petra, Terracotta...): lọc theo thời kỳ (đồ đá / đồ đồng / cổ đại / trung cổ), nền văn minh, tình trạng khai quật (đang đào / đã xong / đóng cửa). Mỗi di chỉ: phát hiện quan trọng nhất, niên đại bằng phương pháp nào, mở cửa tham quan không, vé bao nhiêu (ghi "chưa kiểm chứng" nếu không xác minh được giá).
Gốc: World History Encyclopedia (bài + bản đồ di chỉ theo nền văn minh) + UNESCO World Heritage List. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi cách hiển thị (bài viết rời rạc → database lọc theo thời kỳ + tình trạng khai quật) + đổi ngách (độc giả học thuật → người mê khảo cổ + người lên kế hoạch du lịch di tích).
SCAMPER: Adapt (thêm cột "mở cửa tham quan không" cho người đi du lịch) + Combine (directory + "phát hiện quan trọng nhất" mỗi di chỉ). TRIZ: phân đoạn (chia theo thời kỳ/nền văn minh).
Tiền: ads + affiliate tour di tích/sách khảo cổ + gói premium "lộ trình 7 ngày theo dấu di chỉ" (PDF).
Làm: 2 buổi (seed 60 di chỉ nổi tiếng nhất).

### G4-D6. Directory hiệp ước hòa bình lịch sử — tra theo cuộc chiến, điều khoản chính, bên ký — ★4 — Chờ duyệt
Mô tả: Gõ tên cuộc chiến (Thế chiến I, Chiến tranh Trăm Năm...) ra hiệp ước kết thúc nó; hoặc lọc theo thế kỷ, khu vực, loại điều khoản (nhượng đất / bồi thường / giới hạn quân đội). Mỗi hiệp ước: bên ký, năm, 3 điều khoản quan trọng nhất bằng lời dễ hiểu, và "hậu quả không ngờ" (ví dụ điều khoản nào vô tình châm ngòi cho cuộc chiến sau).
Gốc: Yale Law School — Avalon Project (kho văn bản hiệp ước, tuyên ngôn lịch sử) + Wikipedia — List of treaties. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi cách hiển thị (văn bản hiệp ước dài khô khan → mỗi hiệp ước 3 điều khoản + 1 hậu quả) + đổi topic (chiến tranh → hòa bình sau chiến tranh).
SCAMPER: Eliminate (bỏ toàn văn, chỉ giữ 3 điều khoản chính) + Reverse (thay vì kể chiến tranh, kể cái kết của chiến tranh). TRIZ: tách ra (chỉ lấy phần hay nhất của văn bản).
Tiền: ads + affiliate sách lịch sử ngoại giao + gói "tóm tắt hiệp ước theo chủ đề" cho giáo viên 49k.
Làm: 2–3 buổi (seed 60 hiệp ước nổi tiếng nhất; tóm tắt bằng lời mình, không chép nguyên văn).

### G4-D7. Directory tàu đắm & di sản khảo cổ dưới nước — lọc theo thời kỳ, vùng biển, đã trục vớt chưa — ★4 — Chờ duyệt
Mô tả: Tra cứu xác tàu đắm nổi tiếng (Titanic, Vasa, Mary Rose, tàu buôn cổ...): lọc theo thời kỳ, vùng biển, nguyên nhân chìm, tình trạng (đã trục vớt / còn dưới đáy / đang trưng bày ở bảo tàng nào). Mỗi tàu: câu chuyện chìm trong 3 dòng, hiện vật vớt được quan trọng nhất, xem được ở đâu.
Gốc: UNESCO — Underwater Cultural Heritage (Công ước 2001 về bảo vệ di sản văn hóa dưới nước) + Wikipedia — List of shipwrecks. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (khảo cổ trên cạn → khảo cổ dưới nước) + đổi ngách (độc giả lịch sử → fan "kho báu đắm tàu" + người mê lặn biển).
SCAMPER: Adapt (thêm cột "xem được ở bảo tàng nào") + Combine (directory tàu đắm + bản đồ vùng biển). TRIZ: đổi ngách hiển thị (danh sách → bản đồ biển).
Tiền: ads + affiliate sách/documentary về tàu đắm + affiliate tour bảo tàng hàng hải.
Làm: 2 buổi (seed 50 tàu đắm nổi tiếng nhất).

### G4-D8. Directory nhân vật lịch sử theo độ nổi tiếng toàn cầu — lọc theo thời đại, lĩnh vực, quê hương — ★5 — Chờ duyệt
Mô tả: Dựa trên dữ liệu đo "độ nổi tiếng xuyên ngôn ngữ" (một người có bài Wikipedia ở bao nhiêu thứ tiếng): lọc theo thời đại (trước Công nguyên / trung cổ / cận đại), lĩnh vực (triết học, quân sự, khoa học, nghệ thuật, chính trị), quê hương. Mỗi nhân vật: 3 mốc đời quan trọng nhất, vì sao nổi tiếng toàn cầu, 1 hiểu lầm phổ biến về họ.
Khác thẻ #1400 (Brain lịch sử × graph sự kiện/nhân vật link theo nhân–quả): đây là directory tra cứu + lọc theo chỉ số nổi tiếng, không phải graph nhân quả.
Gốc: Pantheon — MIT Media Lab (dataset nhân vật lịch sử xếp theo Historical Popularity Index, ~11.000 nhân vật có bài ở ≥25 ngôn ngữ Wikipedia). Link tham khảo: http://www.thinkinghumanity.com/2014/09/the-10-most-famous-personalities-of-last-6000-years.html (bài giải thích Pantheon; kiểm chứng 11/11: top 10 bản 2014: Aristotle, Plato, Jesus, Socrates, Alexander Đại đế, Leonardo da Vinci, Khổng Tử, Julius Caesar, Homer, Pythagoras — 8/10 sống trước Công nguyên, 7 người Hy Lạp/Macedonia, 0 phụ nữ; lưu ý thiên lệch nguồn Wikipedia trong thẻ.)
Trục đổi: đổi cách hiển thị (dataset học thuật khô → directory lọc theo thời đại/lĩnh vực + "1 hiểu lầm phổ biến") + đổi ngách (nhà nghiên cứu → người Việt mê lịch sử, học sinh).
SCAMPER: Adapt (thêm mục "hiểu lầm phổ biến" + cảnh báo thiên lệch dữ liệu) + Modify (xếp hạng theo độ nổi tiếng xuyên ngôn ngữ thay vì theo năm sinh). TRIZ: thay đổi cách hiển thị (dataset → tra cứu trực quan).
Tiền: ads + affiliate sách tiểu sử + gói quiz "đoán nhân vật theo 3 mốc đời" premium.
Làm: 2–3 buổi (seed 200 nhân vật đầu bảng, dữ liệu Pantheon là nguồn mở).

### G4-D9. Directory bản đồ lịch sử — kéo thanh thời gian xem biên giới thay đổi — ★4 — Chờ duyệt
Mô tả: Chọn khu vực (châu Âu, Trung Đông, Đông Á...) + kéo thanh trượt năm (vd. 1500 → 1900) → xem biên giới các nước/đế chế thay đổi qua từng mốc. Mỗi bản đồ kèm 2 dòng "năm này có gì đổi" (chiến tranh nào, hiệp ước nào vẽ lại biên giới). Lọc theo bộ sưu tập bản đồ cổ đã hết bản quyền.
Khác thẻ #1120 (5.000 năm lịch sử thế giới × 1 trang kéo ngang — timeline sự kiện): đây là bản đồ địa lý thay đổi theo thời gian, không phải timeline sự kiện.
Gốc: David Rumsey Map Collection (bộ sưu tập bản đồ lịch sử số hóa, lưu trữ tại Stanford) + Library of Congress — Geography & Map Division. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng. Chỉ dùng bản đồ đã hết bản quyền (public domain).
Trục đổi: đổi cách hiển thị (xem từng bản đồ tĩnh → thanh trượt thời gian so sánh biên giới) + đổi topic (sự kiện lịch sử → địa lý lịch sử).
SCAMPER: Modify (thêm thanh trượt thời gian) + Combine (bản đồ + 2 dòng giải thích mỗi mốc). TRIZ: linh hoạt (đổi theo ngữ cảnh năm/khu vực người dùng chọn).
Tiền: ads + bán bản in bản đồ cổ (print-on-demand qua affiliate) + gói premium "bản đồ so sánh 2 năm bất kỳ".
Làm: 2–3 buổi (seed 20 khu vực × 5 mốc thời gian, dùng ảnh bản đồ public domain).

### G4-D10. Directory các cuộc cách mạng & nổi dậy lớn — lọc theo nguyên nhân, kết quả, bài học — ★4 — Chờ duyệt
Mô tả: Tra cứu cuộc cách mạng/nổi dậy (Pháp 1789, Mỹ 1776, Nga 1917, công nghiệp...): lọc theo nguyên nhân chính (thuế, đói, độc lập, công nghệ), theo kết quả (đổi chế độ / thất bại / lan sang nước khác), theo thời gian kéo dài. Mỗi cuộc: 3 nguyên nhân, 3 hệ quả, 1 bài học "vì sao thành / vì sao bại".
Gốc: Wikipedia — List of revolutions and rebellions + Britannica (tóm tắt từng cuộc cách mạng). Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi cách hiển thị (bài viết dài từng cuộc → database lọc theo nguyên nhân/kết quả) + đổi ngách (độc giả học thuật → người mê lịch sử chính trị + học sinh ôn thi).
SCAMPER: Adapt (thêm bộ lọc "nguyên nhân → kết quả" để so sánh các cuộc cách mạng) + Eliminate (chỉ giữ 3 nguyên nhân + 3 hệ quả mỗi cuộc). TRIZ: phân đoạn (chia theo nguyên nhân/kết quả).
Tiền: ads + affiliate sách lịch sử chính trị + gói "so sánh 2 cuộc cách mạng" premium cho giáo viên.
Làm: 2 buổi (seed 50 cuộc cách mạng/nổi dậy lớn nhất).

## GLOSSARY (10 thẻ)

### G4-G1. Glossary thuật ngữ chiến tranh & quân sự — định nghĩa + ví dụ trận thật + phân biệt cặp dễ nhầm — ★5 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ (blitzkrieg, chiến tranh tiêu hao, bao vây, phục kích, chiến tranh du kích, tổng lực...): định nghĩa 2 dòng tiếng Việt, ví dụ 1 trận thật đã dùng chiến thuật đó, và mục "dễ nhầm với" (vd. bao vây vs phong tỏa, du kích vs khủng bố — phân biệt rạch ròi).
Khác #1187 (thuật ngữ AI) và #1189 (thuật ngữ tài chính): cùng format glossary nhưng ngành khác hẳn.
Gốc: Britannica — Military history / US Department of Defense Dictionary of Military Terms. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ AI/tài chính đã có → thuật ngữ quân sự) + đổi cách hiển thị (định nghĩa khô → định nghĩa + ví dụ trận thật + phân biệt cặp nhầm).
SCAMPER: Adapt (ví dụ phương Tây → trận nổi tiếng thế giới ai cũng biết) + Combine (glossary + mục phân biệt). TRIZ: đa năng (1 glossary dùng cho cả đọc sử, xem phim chiến tranh, chơi game chiến thuật).
Tiền: ads + affiliate sách/film chiến tranh + PDF "100 thuật ngữ quân sự" 29k.
Làm: 2 buổi (seed 100 thuật ngữ).

### G4-G2. Glossary thuật ngữ đế chế & chính thể — thuộc địa khác gì bảo hộ, đế chế khác gì bá quyền — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ chính thể (đế chế, thuộc địa, bảo hộ, đô hộ, chư hầu, liên bang, bá quyền, phiên thuộc...): định nghĩa 2 dòng + ví dụ đế chế thật + mục "phân biệt" là linh hồn của thẻ này (thuộc địa vs bảo hộ vs lãnh thổ ủy trị — 3 khái niệm hay bị gộp làm một).
Gốc: Britannica — Government & political systems + Wikipedia — Glossary of political terms. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ quân sự → thuật ngữ chính thể) + đổi cách hiển thị (định nghĩa đơn → định nghĩa + bảng phân biệt 3 khái niệm gần giống).
SCAMPER: Modify (nhấn mạnh mục phân biệt thành trường bắt buộc mỗi thuật ngữ) + Adapt (ví dụ bằng đế chế ai cũng biết: La Mã, Anh, Ottoman). TRIZ: tách ra (tách riêng cụm "3 khái niệm dễ nhầm" thành tính năng tra cứu riêng).
Tiền: ads + affiliate sách lịch sử chính trị + PDF "bảng phân biệt chính thể" 29k.
Làm: 2 buổi (seed 60 thuật ngữ).

### G4-G3. Glossary thuật ngữ khảo cổ — định nghĩa + ví dụ phát hiện thật + cách nhà khảo cổ dùng nó — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ khảo cổ (địa tầng, định tuổi carbon-14, gò rác bếp, mộ gò, hiện vật, di chỉ, phục dựng...): định nghĩa 2 dòng + ví dụ 1 phát hiện thật (vd. địa tầng giải thích sao biết lớp nào cổ hơn ở Pompeii) + "nhà khảo cổ dùng nó để làm gì".
Gốc: Society for American Archaeology — glossary / Archaeological Institute of America. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ quân sự/chính thể → thuật ngữ khảo cổ) + đổi ngách (sinh viên khảo cổ → người mê khảo cổ xem documentary, fan Indiana Jones muốn hiểu thật).
SCAMPER: Adapt (thêm "dùng để làm gì" — biến định nghĩa thành câu chuyện nghề) + Combine (glossary + ví dụ phát hiện thật). TRIZ: tự phục vụ (người đọc tự tra cứu khi xem phim tài liệu, không cần ai giảng).
Tiền: ads + affiliate sách khảo cổ/documentary + PDF "thuật ngữ khảo cổ cho người xem documentary" 29k.
Làm: 2 buổi (seed 80 thuật ngữ).

### G4-G4. Glossary thuật ngữ kiến trúc & nghệ thuật cổ — vòm, tranh tường, khảm, kim tự tháp... kèm ảnh thật — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ kiến trúc/nghệ thuật cổ (vòm cuốn, mái vòm, tranh tường fresco, khảm mosaic, cột Doric/Ionic/Corinthian, ziggurat, phù điêu...): định nghĩa 2 dòng + ảnh thật 1 công trình tiêu biểu + "nhìn ở đâu để nhận ra" (mẹo nhận diện khi đi du lịch di tích).
Gốc: The Met — Heilbrunn Timeline of Art History (thuật ngữ + ảnh hiện vật) + Smarthistory (glossary nghệ thuật). Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng. Ảnh dùng ảnh public domain / CC.
Trục đổi: đổi cách hiển thị (glossary chữ → chữ + ảnh thật + mẹo nhận diện tại chỗ) + đổi ngách (sinh viên kiến trúc → khách du lịch di tích muốn "nhìn là hiểu").
SCAMPER: Combine (glossary + cẩm nang nhận diện tại di tích) + Adapt (mẹo "nhìn ở đâu" cho người đi du lịch, không phải thi cử). TRIZ: thay đổi cách hiển thị (chữ → chữ + ảnh).
Tiền: ads + affiliate sách kiến trúc/tour di tích + PDF "nhận diện kiến trúc cổ khi du lịch" 29k.
Làm: 2 buổi (seed 80 thuật ngữ, ảnh public domain/CC).

### G4-G5. Glossary các thời kỳ lịch sử — Đồ Đồng, Trung Cổ, Phục Hưng... và những cách gọi gây nhầm — ★5 — Chờ duyệt
Mô tả: Tra cứu tên thời kỳ (Đồ Đá, Đồ Đồng, Đồ Sắt, Cổ đại, Trung Cổ, Phục Hưng, Khai sáng, Cách mạng Công nghiệp...): định nghĩa 2 dòng + khoảng năm + khu vực áp dụng + mục "gây nhầm ở chỗ" (vd. "Trung Cổ tăm tối" là cách gọi gây tranh cãi; "Phục Hưng" không diễn ra cùng lúc ở mọi nước; "thời kỳ đồ đá" ở châu Âu khác châu Mỹ).
Gốc: World History Encyclopedia — Periods / Britannica — Historical periods. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ sự vật → tên thời kỳ) + đổi cách hiển thị (danh sách thời kỳ theo năm → mỗi thời kỳ kèm "gây nhầm ở chỗ" + bản đồ khu vực áp dụng).
SCAMPER: Modify (thêm trường "gây nhầm" làm điểm khác biệt chính) + Adapt (ghi rõ thời kỳ này đúng ở khu vực nào, tránh dạy sai). TRIZ: đảo ngược (thay vì hỏi "thời kỳ này là khi nào", trả lời "cách gọi này sai ở đâu").
Tiền: ads + affiliate sách lịch sử thế giới + PDF "timeline các thời kỳ theo khu vực" 29k.
Làm: 1–2 buổi (seed 60 thời kỳ).

### G4-G6. Glossary thuật ngữ ngoại giao & hiệp ước — đình chiến khác gì ngừng bắn, hòa hoãn là gì — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ ngoại giao (đình chiến, ngừng bắn, hiệp ước, hòa hoãn/détente, xoa dịu/appeasement, tối hậu thư, trung lập, trừng phạt...): định nghĩa 2 dòng + ví dụ hiệp ước/sự kiện thật + phân biệt cặp nhầm (đình chiến vs ngừng bắn vs hòa ước — 3 mức khác nhau, báo chí hay dùng lẫn).
Khác G4-D6 (directory hiệp ước — tra cứu từng hiệp ước cụ thể): đây là glossary tra cứu khái niệm, không phải database hiệp ước.
Gốc: Britannica — Diplomacy / US Department of State — Diplomatic terms. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ quân sự → thuật ngữ ngoại giao) + đổi cách hiển thị (định nghĩa → định nghĩa + ví dụ sự kiện thật + phân biệt 3 mức).
SCAMPER: Combine (glossary + ví dụ hiệp ước thật) + Adapt (phân biệt các từ báo chí hay dùng lẫn). TRIZ: tách ra (tách cụm "3 mức ngừng chiến" thành tra cứu riêng).
Tiền: ads + affiliate sách ngoại giao/lịch sử + PDF "thuật ngữ ngoại giao cho người đọc tin quốc tế" 29k.
Làm: 2 buổi (seed 60 thuật ngữ).

### G4-G7. Glossary thuật ngữ tôn giáo cổ & thần thoại — đền thờ, sấm truyền, tín ngưỡng... phân biệt thần thoại với tôn giáo — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ (đa thần, độc thần, đền thờ/pantheon, sấm truyền/oracle, nghi lễ, hiến tế, tín ngưỡng vật linh/animism, thần thoại sáng thế...): định nghĩa 2 dòng + ví dụ nền văn minh thật (Hy Lạp, Ai Cập, Maya, Bắc Âu) + mục "thần thoại khác tôn giáo ở chỗ nào" cho các cặp hay nhầm.
Gốc: World History Encyclopedia — Religion & mythology / Britannica — Ancient religions. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ chính trị/quân sự → thuật ngữ tôn giáo cổ) + đổi ngách (độc giả học thuật → fan thần thoại, game thủ (God of War), người xem phim cổ trang muốn hiểu bối cảnh).
SCAMPER: Adapt (ví dụ bằng thần thoại các nền văn minh nổi tiếng, gắn với game/phim người ta đã biết) + Combine (glossary + bảng so sánh thần thoại 4 nền văn minh). TRIZ: đa năng (1 glossary dùng cho cả đọc sử, chơi game, xem phim).
Tiền: ads + affiliate sách thần thoại/game/phim cổ trang + PDF "thần thoại 4 nền văn minh so sánh" 29k.
Làm: 2 buổi (seed 80 thuật ngữ).

### G4-G8. Glossary thuật ngữ địa lý lịch sử — vùng đệm, đất tách rời, bá quyền biển... — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ địa lý lịch sử (vùng đệm/buffer state, đất tách rời/exclave, đất bao quanh/enclave, bá quyền biển/thalassocracy, vùng đất chưa biết/terra incognita, biên giới tự nhiên, hành lang...): định nghĩa 2 dòng + ví dụ bản đồ thật (vd. vùng đệm giữa 2 đế chế, đất tách rời nổi tiếng) + "nhìn trên bản đồ ra sao".
Khác G4-D9 (directory bản đồ — xem biên giới thay đổi): đây là glossary tra cứu khái niệm địa lý, mỗi thuật ngữ kèm 1 ví dụ bản đồ.
Gốc: Britannica — Historical geography / National Geographic — Geography glossary. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ chính trị → thuật ngữ địa lý) + đổi cách hiển thị (định nghĩa → định nghĩa + ví dụ bản đồ thật).
SCAMPER: Combine (glossary + ví dụ bản đồ) + Adapt (thêm "nhìn trên bản đồ ra sao" cho người học bản đồ). TRIZ: thay đổi cách hiển thị (chữ → chữ + bản đồ minh họa).
Tiền: ads + affiliate sách/atlas lịch sử + PDF "thuật ngữ địa lý lịch sử kèm bản đồ" 29k.
Làm: 2 buổi (seed 60 thuật ngữ, bản đồ public domain).

### G4-G9. Glossary thuật ngữ kinh tế lịch sử — cống nạp, phong kiến khác gì trang viên, trọng thương... — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ kinh tế thời xưa (cống nạp/tribute, phong kiến/feudalism, trang viên/manorialism, trọng thương/mercantilism, phường hội/guild, thuế thập phân/tithe, tiền hàng hóa...): định nghĩa 2 dòng + ví dụ đế chế/vương quốc thật + phân biệt cặp nhầm (phong kiến vs trang viên — 2 khái niệm hay bị dạy gộp làm một).
Khác #1189 (100 thuật ngữ tài chính hiện đại): đây là kinh tế thời tiền-hiện đại, gắn với đế chế và xã hội cổ/trung cổ.
Gốc: Britannica — Economic history / EH.net (Economic History Association). Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (tài chính hiện đại → kinh tế lịch sử) + đổi cách hiển thị (định nghĩa → định nghĩa + ví dụ đế chế thật + phân biệt cặp nhầm).
SCAMPER: Adapt (ví dụ bằng đế chế/vương quốc cụ thể thay vì lý thuyết khô) + Modify (nhấn mạnh phân biệt phong kiến vs trang viên). TRIZ: tách ra (tách riêng cụm "kinh tế thời xưa" khỏi tài chính hiện đại).
Tiền: ads + affiliate sách kinh tế lịch sử + PDF "kinh tế thời xưa giải thích bằng ví dụ" 29k.
Làm: 2 buổi (seed 60 thuật ngữ).

### G4-G10. Glossary thuật ngữ hàng hải & hải quân cổ — thuyền 3 tầng chèo, tàu buồm, cướp biển khác gì tư nhân được cấp phép — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ hàng hải cổ (thuyền 3 tầng chèo/trireme, thuyền buồm caravel, thuyền galley, tàu chiến tuyến/ship of the line, cướp biển/pirate vs tư nhân được cấp phép/privateer, hải tặc...): định nghĩa 2 dòng + ví dụ trận hải chiến/tàu thật + phân biệt (privateer có giấy phép của vua, pirate thì không — cùng cướp biển nhưng địa vị pháp lý khác hẳn).
Khác G4-D7 (directory tàu đắm — tra cứu từng con tàu): đây là glossary tra cứu khái niệm/loại tàu, không phải database tàu đắm.
Gốc: Britannica — Naval history / National Maritime Museum (Greenwich) — glossary. Link: chưa kiểm chứng link chi tiết — cần đối chiếu trước khi đăng.
Trục đổi: đổi topic (thuật ngữ quân sự trên bộ → thuật ngữ hàng hải) + đổi ngách (độc giả sử học → fan hải tặc, game thủ (Assassin's Creed Black Flag), người mê Age of Sail).
SCAMPER: Adapt (gắn ví dụ với trận hải chiến/game/phim nổi tiếng) + Combine (glossary + phân biệt pháp lý pirate vs privateer). TRIZ: đa năng (1 glossary dùng cho cả đọc sử, chơi game hải tặc, xem phim).
Tiền: ads + affiliate sách/game/phim hải tặc + PDF "thuật ngữ hàng hải cổ" 29k.
Làm: 1–2 buổi (seed 60 thuật ngữ).

## Làm ngay

**G4-D3. Directory di sản UNESCO đang gặp nguy hiểm — lọc theo mối đe dọa, xem di sản nào đã được cứu — ★5.**
Lý do: seed chỉ 58 di sản, dữ liệu có sẵn và đã kiểm chứng trực tiếp từ UNESCO (58 di sản, 3 ca ra khỏi danh sách tháng 7/2025); khác rõ thẻ #1147 (toàn bộ di sản); góc "nguy hiểm + đã được cứu" có cảm xúc, dễ chia sẻ, làm xong trong 1–2 buổi, ra tiền bằng ads + affiliate tour di sản.

---

# Track 5 — Directory & Glossary, cụm G5: Lịch sử Việt Nam / Toán / Thống kê / Khoa học dữ liệu / Lịch sử khoa học (phát minh & nhà khoa học)

Count: 20 / 20

Quy tắc lô: chỉ DIRECTORY (database tra cứu được: tìm kiếm + lọc theo tiêu chí, mỗi mục có dữ liệu cấu trúc) và GLOSSARY (tra cứu thuật ngữ: định nghĩa 2 dòng + ví dụ thật + phân biệt với thuật ngữ gần giống). KHÔNG làm list tĩnh "100 X". Mỗi thẻ remix từ 1 gốc nước ngoài có thật, ghi link gốc + trục đổi + phép SCAMPER/TRIZ. Phạm vi chỉ G5 — không lấn lịch sử thế giới, vật lý/thiên văn, sinh học, AI (cụm khác). Tránh trùng: #1062 glossary mô hình tư duy, #1187 thuật ngữ AI, #1189 thuật ngữ tài chính, #1196 thuật ngữ y khoa, D11 thiên kiến, D12 SEO, D13 UX/UI, D14 đàm phán, D15 cà phê, D6 directory dataset VN (Kaggle + notebook). Tất cả "Chờ duyệt".

## DIRECTORY (10 thẻ)

### G5-D1. Directory di tích & bảo tàng lịch sử Việt Nam — tìm theo triều đại, tỉnh, loại hình — ★5 — Chờ duyệt
Mô tả: Gõ triều đại ("nhà Trần", "nhà Nguyễn") hoặc tỉnh ra di tích/bảo tàng tương ứng, lọc theo loại hình (đền, chùa, thành cổ, bảo tàng, chiến trường), mỗi mục có: niên đại, triều đại, địa chỉ, giờ mở cửa, giá vé (nếu có), 1 câu "vì sao chỗ này quan trọng". Người dùng lên lịch tham quan theo tuyến triều đại thay vì lướt list rời rạc.
Gốc: Metropolitan Museum — Heilbrunn Timeline of Art History, timeline nghệ thuật tra cứu theo thời kỳ + khu vực + chủ đề. Link: https://www.metmuseum.org/toah
(Kiểm chứng 11/11: Met Timeline là timeline tra cứu chuẩn của bảo tàng lớn nhất Mỹ.)
Trục đổi: đổi ngách (nghệ thuật thế giới → di tích lịch sử VN) + đổi cách hiển thị (timeline theo thời kỳ → database lọc theo triều đại + tỉnh + loại hình).
SCAMPER: Adapt (mượn khung timeline theo thời kỳ sang lịch sử VN) + Combine (directory + tuyến tham quan gợi ý). TRIZ: phân đoạn (chia theo triều đại).
Tiền: ads + listing trả phí cho bảo tàng/di tích tư nhân + affiliate tour/đặt vé + bản PDF "tuyến 3 ngày theo triều đại" 29k.
Làm: 2–3 buổi (seed 150 di tích/bảo tàng, form cộng đồng gửi thêm).

### G5-D2. Số liệu lịch sử Việt Nam qua 100 năm — dân số, GDP, xuất khẩu, kéo thanh trượt xem thay đổi — ★5 — Chờ duyệt
Mô tả: Chọn 1 chỉ số (dân số, GDP bình quân đầu người, xuất khẩu gạo, tỷ lệ biết chữ...) rồi kéo thanh trượt theo năm (1920→nay) xem số liệu + biểu đồ thay đổi; so sánh VN với 2 nước tự chọn cùng giai đoạn. Mỗi chỉ số ghi rõ nguồn số liệu gốc. Học sinh, giáo viên, người làm nội dung tra 1 chỗ thay vì mò nhiều nguồn.
Gốc: Our World in Data — Data Explorer, tra cứu hàng nghìn chỉ số theo quốc gia + thời gian, có biểu đồ so sánh. Link: https://ourworldindata.org
(Kiểm chứng 11/11: OWID có Data Explorer với các mục Population & Demography, GDP per capita (Maddison Project Database), Poverty — tra cứu theo quốc gia và năm.)
Trục đổi: đổi ngách (số liệu toàn cầu → chỉ VN, tiếng Việt, giải thích bằng bối cảnh lịch sử VN) + đổi cách hiển thị (explorer khô → kéo thanh trượt theo năm + so sánh 3 nước).
SCAMPER: Modify (thu hẹp từ toàn cầu xuống 1 nước nhưng sâu theo thời gian) + Adapt (thêm chú thích sự kiện lịch sử tại điểm gãy của biểu đồ). TRIZ: thay đổi cách hiển thị (số liệu → timeline kéo được).
Tiền: ads + bản Pro tải dữ liệu CSV + gói "biểu đồ làm sẵn cho giáo viên" 49k/tháng + affiliate sách lịch sử.
Làm: 2–3 buổi (seed 30 chỉ số, dữ liệu từ OWID/World Bank/Tổng cục Thống kê — ghi rõ nguồn từng chỉ số).

### G5-D3. Directory phát minh theo dòng thời gian — "năm 1876 có gì mới?" — ★4 — Chờ duyệt
Mô tả: Chọn 1 năm bất kỳ (hoặc kéo timeline) ra các phát minh ra đời năm đó, lọc theo lĩnh vực (y tế, giao thông, truyền thông, nông nghiệp), mỗi phát minh có: ai phát minh, vấn đề nó giải quyết, phát minh nào trước đó làm nền cho nó. Học sinh tra cứu làm bài, người tò mò khám phá theo kiểu "hôm nay trong lịch sử phát minh".
Gốc: Lemelson-MIT — Invention Dimension, kho lưu trữ nhà phát minh tra cứu được theo tên phát minh và theo người, kèm Inventor's Handbook. Link: https://lemelson.mit.edu
(Kiểm chứng 11/11: Lemelson-MIT Program (MIT, từ 1994) có archive tra cứu theo phát minh/người phát minh; trang hiện tại lemelson.mit.edu.)
Trục đổi: đổi cách hiển thị (archive theo tên → timeline theo năm + lọc theo lĩnh vực) + đổi topic (chỉ nhà phát minh Mỹ → phát minh toàn cầu, có mục riêng "phát minh của người Việt").
SCAMPER: Reverse (thay vì tìm phát minh theo tên, tìm theo năm) + Combine (directory + chuỗi "phát minh này đứng trên vai phát minh nào").
Tiền: ads + bản PDF timeline phát minh in treo lớp học 29k + affiliate sách/khóa STEM.
Làm: 2 buổi (seed 200 phát minh, 1800→nay).

### G5-D4. Directory nhà khoa học Việt Nam & thế giới — lọc theo lĩnh vực, thời đại, nữ khoa học gia — ★4 — Chờ duyệt
Mô tả: Tìm nhà khoa học theo lĩnh vực (toán, y, nông nghiệp...), thời đại, quốc gia, giới tính; mỗi người 1 hồ sơ ngắn: đóng góp lớn nhất là gì (1 câu dễ hiểu), 1 giai thoại, 1 câu nói/trích dẫn, sách/bài nên đọc thêm. Có mục riêng "nhà khoa học Việt Nam" (từ Lương Định Của, Tôn Thất Tùng tới các nhà khoa học trẻ) và mục "nữ khoa học gia".
Gốc: Nobel Prize — cơ sở dữ liệu người đoạt giải Nobel, tra cứu theo giải, năm, quốc gia. Link: https://www.nobelprize.org
Trục đổi: đổi ngách (chỉ người đoạt Nobel → mọi nhà khoa học, trọng tâm VN) + đổi topic (hồ sơ giải thưởng → hồ sơ "đóng góp + giai thoại + nên đọc gì").
SCAMPER: Adapt (mượn khung lọc theo giải/năm/quốc gia của Nobel sang lĩnh vực/thời đại/giới tính) + Combine (directory + mục nữ khoa học gia + mục nhà khoa học Việt).
Tiền: ads + bản poster "100 nhà khoa học" 49k + affiliate sách tiểu sử khoa học.
Làm: 2 buổi (seed 150 hồ sơ, 50 người Việt).

### G5-D5. Directory công thức toán tra cứu theo dạng bài — "bài này dùng công thức nào?" — ★5 — Chờ duyệt
Mô tả: Học sinh gõ dạng bài ("tìm giá trị lớn nhất", "xác suất 2 xúc xắc", "diện tích hình phẳng") ra công thức cần dùng + 1 ví dụ giải mẫu từng bước + lỗi sai hay gặp. Lọc theo cấp (THCS/THPT/đại học) và chủ đề (đại số, hình học, giải tích, xác suất). Khác web công thức list dài: đây là tra cứu ngược từ dạng bài tới công thức.
Gốc: Wolfram MathWorld — bách khoa toán học tra cứu theo chủ đề, mỗi mục có định nghĩa + công thức + ví dụ. Link: https://mathworld.wolfram.com
Trục đổi: đổi cách hiển thị (tra cứu theo tên công thức → tra cứu ngược từ dạng bài) + đổi ngách (độc giả tiếng Anh → học sinh VN, ví dụ theo đề thi VN).
SCAMPER: Reverse (đảo hướng tra cứu: từ bài → công thức thay vì từ công thức → bài) + Adapt (ví dụ theo đề THPT Việt Nam). TRIZ: tự phục vụ (học sinh tự tìm, không cần gia sư).
Tiền: ads + gói Pro (lời giải chi tiết từng bước, 29k/tháng) + affiliate khóa học toán/sách tham khảo.
Làm: 2–3 buổi (seed 200 dạng bài, 4 cấp/chủ đề).

### G5-D6. Directory chỉ số thống kê thế giới & Việt Nam — so sánh VN với bất kỳ nước nào, 1 cú nhấp — ★4 — Chờ duyệt
Mô tả: Chọn 1 chỉ số (tỷ lệ thất nghiệp, tuổi thọ, chi tiêu y tế, tỷ lệ biết chữ...) + chọn VN và 1–3 nước so sánh, ra biểu đồ + bảng số theo năm + 1 câu "VN đang ở đâu so với nhóm". Dữ liệu lấy từ World Bank, ghi rõ nguồn và năm cập nhật từng chỉ số. Người làm nội dung, sinh viên kinh tế tra cứu nhanh thay vì tải file World Bank về tự vẽ.
Khác thẻ D6 (directory dataset VN trên Kaggle + notebook mẫu): thẻ này là database chỉ số có sẵn biểu đồ so sánh quốc gia, không cần tải dataset hay chạy code.
Gốc: World Bank DataBank — database chỉ số phát triển tra cứu theo quốc gia + chỉ số + năm. Link: https://data.worldbank.org
Trục đổi: đổi ngách (database cho nhà nghiên cứu → cho người Việt không rành data) + đổi cách hiển thị (bảng số khô → so sánh 1 cú nhấp + 1 câu kết luận).
SCAMPER: Eliminate (bỏ hàng nghìn chỉ số ít dùng, chỉ giữ ~150 chỉ số người VN hay tra) + Modify (thêm câu kết luận "VN đang ở đâu"). TRIZ: phân đoạn (chia chỉ số theo chủ đề đời sống).
Tiền: ads + bản Pro xuất biểu đồ đẹp (PNG/SVG) 29k/tháng + affiliate khóa data.
Làm: 2 buổi (seed 150 chỉ số, dữ liệu World Bank — ghi rõ nguồn).

### G5-D7. Directory nhà toán học & định lý — ai chứng minh cái gì, mất bao lâu — ★4 — Chờ duyệt
Mô tả: Tìm nhà toán học theo thời đại hoặc định lý theo tên, mỗi mục có: định lý nói gì bằng 1 câu dễ hiểu, ai chứng minh, chứng minh mất bao lâu (vài ngày hay 358 năm như Định lý cuối Fermat), và định lý đó dùng vào việc gì hôm nay. Có mục "định lý nổi tiếng chưa ai chứng minh được" và "nhà toán học Việt Nam".
Gốc: MacTutor History of Mathematics Archive (Đại học St Andrews) — hơn 3.200 tiểu sử nhà toán học + hơn 2.000 bài viết/chủ đề, tra cứu theo bảng chữ cái và theo thời gian. Link: https://mathshistory.st-andrews.ac.uk
(Kiểm chứng 11/11: MacTutor có 3.200+ tiểu sử, 2.000+ bài viết; O'Connor & Robertson nhận giải Hirst Prize 2015 của London Mathematical Society.)
Trục đổi: đổi cách hiển thị (tiểu sử dài → hồ sơ ngắn "định lý + mất bao lâu + dùng vào việc gì") + đổi ngách (học thuật → người tò mò/học sinh, thêm nhà toán học Việt).
SCAMPER: Combine (directory tiểu sử + directory định lý trong 1 chỗ) + Modify (thêm trục "chứng minh mất bao lâu" làm điểm lạ). TRIZ: sao chép (làm lại bản nhẹ, dễ đọc của kho học thuật nặng).
Tiền: ads + bản PDF "50 định lý thay đổi thế giới" 29k + affiliate sách toán phổ thông.
Làm: 2 buổi (seed 120 nhà toán học + 80 định lý).

### G5-D8. Directory thí nghiệm khoa học nổi tiếng làm được ở nhà/lớp học — lọc theo vật liệu có sẵn — ★4 — Chờ duyệt
Mô tả: Giáo viên/phụ huynh lọc thí nghiệm theo vật liệu đang có sẵn (nước, giấm, bóng đèn...), độ tuổi, thời gian (5 phút/30 phút), mỗi thí nghiệm có: hiện tượng gì, giải thích khoa học 3 dòng, video demo, cảnh báo an toàn. Thí nghiệm nào cũng gắn với 1 nhà khoa học/phát minh trong lịch sử (làm lại thí nghiệm của Archimedes, Galileo... bằng đồ nhà bếp).
Gốc: Exploratorium (San Francisco) — kho hoạt động/thí nghiệm khoa học tương tác cho giáo viên và gia đình, tra cứu theo chủ đề. Link: https://www.exploratorium.edu
Trục đổi: đổi ngách (thí nghiệm bảo tàng Mỹ → vật liệu có sẵn ở nhà/lớp học VN) + đổi topic (thí nghiệm đơn lẻ → thí nghiệm gắn với nhân vật lịch sử khoa học).
SCAMPER: Combine (directory thí nghiệm + lịch sử nhà khoa học) + Adapt (vật liệu phòng lab → đồ nhà bếp VN). TRIZ: đa năng (1 thí nghiệm dùng cho nhiều độ tuổi, đổi độ khó theo tuổi).
Tiền: ads + gói "bộ thí nghiệm tuần" cho giáo viên 49k/tháng + affiliate dụng cụ thí nghiệm.
Làm: 2 buổi (seed 80 thí nghiệm, lọc an toàn cho trẻ em).

### G5-D9. Directory bản đồ lịch sử Việt Nam — xem biên giới VN thay đổi qua từng thời kỳ — ★4 — Chờ duyệt
Mô tả: Chọn 1 thời kỳ (Lý, Trần, Lê, Nguyễn, 1945, 1975...) ra bản đồ VN thời đó: biên giới ở đâu, thủ đô ở đâu, các địa danh quan trọng; kéo thanh trượt xem biên giới mở rộng/thu hẹp qua thời gian. Mỗi bản đồ kèm 2–3 dòng "chuyện gì xảy ra thời này khiến biên giới đổi". Học sinh học sử bằng mắt thay vì học thuộc tên triều đại.
Gốc: David Rumsey Map Collection — bộ sưu tập bản đồ lịch sử tra cứu được, xem bản đồ cổ theo thời gian + khu vực. Link: https://www.davidrumsey.com
Trục đổi: đổi ngách (bản đồ cổ toàn cầu → chỉ bản đồ lịch sử VN) + đổi cách hiển thị (xem từng bản đồ rời → thanh trượt thời gian xem biên giới thay đổi).
SCAMPER: Modify (biến bộ sưu tập tĩnh thành timeline kéo được) + Adapt (thêm chú thích sự kiện khiến biên giới đổi). TRIZ: thay đổi cách hiển thị (chữ → bản đồ động).
Tiền: ads + bản in poster bản đồ theo thời kỳ 49k + affiliate sách lịch sử/atlas.
Làm: 2–3 buổi (seed 30 bản đồ theo thời kỳ, nguồn bản đồ công cộng — ghi rõ nguồn từng bản đồ).

### G5-D10. Directory đề thi & cuộc thi toán — tra đề cũ theo năm, cấp, dạng bài — ★4 — Chờ duyệt
Mô tả: Tìm đề thi toán cũ theo năm, cấp (lớp 9, THPT, Olympic), dạng bài (số học, hình học, tổ hợp...), mỗi đề có: file đề, đáp án/lời giải, độ khó (dựa trên tỷ lệ làm được — ghi "chưa kiểm chứng" nếu không có số liệu), và đề tương tự để luyện thêm. Học sinh luyện thi tra 1 chỗ thay vì xin đề rải rác trong group.
Gốc: Art of Problem Solving (AoPS) — kho đề thi và cộng đồng toán, tra cứu đề theo cuộc thi + năm. Link: https://artofproblemsolving.com
Trục đổi: đổi ngách (đề thi Mỹ/quốc tế → đề thi VN: THPT quốc gia, HSG, Olympic VN) + đổi cách hiển thị (theo cuộc thi → theo năm + cấp + dạng bài).
SCAMPER: Adapt (khung kho đề AoPS sang đề VN) + Combine (directory đề + gợi ý đề tương tự). TRIZ: phân đoạn (chia đề theo dạng bài thay vì theo năm).
Tiền: ads + gói Pro (lời giải chi tiết + đề luyện tương tự, 29k/tháng) + affiliate sách luyện thi.
Làm: 2–3 buổi (seed 200 đề, chỉ dùng đề đã công khai — không đăng đề lậu/bản quyền).

## GLOSSARY (10 thẻ)

### G5-G1. Glossary thuật ngữ toán học A–Z — định nghĩa 2 dòng + ví dụ đề thi thật + phân biệt thuật ngữ dễ nhầm — ★5 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ toán (hàm số, đạo hàm, tích phân, ma trận...): định nghĩa tiếng Việt 2 dòng, 1 ví dụ lấy từ đề thi VN thật, và mục "đừng nhầm với X" (ví dụ: hàm số vs phương trình; đạo hàm vs vi phân). Tìm kiếm + lọc theo chủ đề và cấp học.
Khác thẻ #1062 (glossary mô hình tư duy) và D11 (thiên kiến): đây là thuật ngữ toán học thuần túy.
Gốc: Khan Academy — thư viện bài học + thuật ngữ toán có định nghĩa và ví dụ minh họa. Link: https://www.khanacademy.org/math
Trục đổi: đổi ngách (toán tiếng Anh → toán chương trình VN) + đổi cách hiển thị (định nghĩa khô → định nghĩa + ví dụ đề thi thật + phân biệt dễ nhầm).
SCAMPER: Adapt (ví dụ Khan → đề thi VN) + Combine (glossary + mục "đừng nhầm với X").
Tiền: ads + bản PDF glossary in được 29k + affiliate sách tham khảo toán.
Làm: 2 buổi (seed 150 thuật ngữ).

### G5-G2. Glossary thuật ngữ thống kê & xác suất — mỗi thuật ngữ 1 ví dụ đời thường + 1 biểu đồ minh họa — ★5 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ thống kê (p-value, khoảng tin cậy, hồi quy, độ lệch chuẩn, sai lầm loại I/II...): định nghĩa 2 dòng, ví dụ đời thường ở VN ("khảo sát 100 người thì sai số bao nhiêu"), 1 biểu đồ minh họa, và mục phân biệt (tương quan vs nhân quả; trung bình vs trung vị). Sinh viên, marketer đọc báo cáo không còn sợ số liệu.
Gốc: Seeing Theory (Đại học Brown) — glossary + explainer thống kê tương tác, có ví dụ và mô phỏng trực quan. Link: https://seeingtheory.brown.edu
Trục đổi: đổi cách hiển thị (explainer tương tác dài → glossary tra cứu nhanh có biểu đồ) + đổi ngách (sinh viên Mỹ → người Việt đọc báo cáo/số liệu).
SCAMPER: Adapt (ví dụ phương Tây → ví dụ VN) + Modify (thêm mục phân biệt cặp dễ nhầm). TRIZ: thay đổi cách hiển thị (công thức → biểu đồ + ví dụ).
Tiền: ads + gói "đọc hiểu báo cáo thống kê" cho marketer 49k + affiliate khóa thống kê.
Làm: 2 buổi (seed 100 thuật ngữ).

### G5-G3. Glossary thuật ngữ khoa học dữ liệu — từ thu thập dữ liệu tới trình bày kết quả, kèm ví dụ dataset thật — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ data (EDA, làm sạch dữ liệu, feature, overfitting, dashboard...): định nghĩa 2 dòng, ví dụ trên 1 dataset thật (giá nhà, thời tiết...), phân biệt với thuật ngữ gần giống (data science vs data analytics vs BI). Lọc theo giai đoạn pipeline (thu thập → làm sạch → phân tích → trình bày). Người mới học data tra 1 chỗ thay vì đọc 10 bài blog rời.
Khác thẻ #1187 (200 thuật ngữ AI — list thuật ngữ AI): thẻ này chỉ thuật ngữ khoa học dữ liệu theo pipeline, có ví dụ dataset thật và phân biệt data vs AI.
Gốc: DataCamp Glossary — glossary thuật ngữ data science có định nghĩa + ví dụ. Link: https://www.datacamp.com/glossary
Trục đổi: đổi cách hiển thị (glossary theo bảng chữ cái → theo pipeline dữ liệu) + đổi ngách (học viên DataCamp → người Việt tự học data, ví dụ dataset VN).
SCAMPER: Adapt (ví dụ dataset Tây → dataset VN) + Combine (glossary + pipeline trực quan).
Tiền: ads + affiliate khóa data (DataCamp, Coursera) + gói "dataset mẫu + notebook" 49k.
Làm: 2 buổi (seed 120 thuật ngữ).

### G5-G4. Glossary thuật ngữ lịch sử Việt Nam — triều đại, chức quan, đơn vị hành chính xưa — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ sử Việt (vua, quan, khoa cử, đơn vị hành chính xưa như phủ/huyện/tổng, các chế độ ruộng đất...): định nghĩa 2 dòng, ví dụ trong 1 sự kiện thật ("chức quan này xuất hiện trong vụ án nào"), phân biệt thuật ngữ dễ nhầm (quan văn vs quan võ, phủ vs huyện). Học sinh đọc sách sử không còn vấp từ lạ.
Gốc (format nước ngoài): BBC Bitesize — History Glossary, glossary lịch sử có định nghĩa ngắn + ví dụ cho học sinh. Link: https://www.bbc.co.uk/bitesize
Trục đổi: đổi ngách (lịch sử Anh cho học sinh Anh → lịch sử VN cho học sinh VN) + đổi topic (định nghĩa khô → định nghĩa + sự kiện thật gắn với thuật ngữ).
SCAMPER: Adapt (mượn format glossary sử của BBC Bitesize sang sử Việt) + Combine (glossary + timeline sự kiện gắn với từng thuật ngữ).
Tiền: ads + bản PDF glossary sử in được 29k + affiliate sách lịch sử.
Làm: 2 buổi (seed 150 thuật ngữ, đối chiếu SGK + nguồn sử liệu công khai).

### G5-G5. Glossary thuật ngữ phát minh & sáng chế — patent, prior art, utility model tra cứu được — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ sáng chế (bằng sáng chế, giải pháp hữu ích, prior art, claims, PCT...): định nghĩa 2 dòng bằng tiếng Việt dễ hiểu, ví dụ thật (1 phát minh VN đã đăng ký), phân biệt cặp dễ nhầm (phát minh vs sáng chế vs kiểu dáng công nghiệp; patent vs utility model). Người có ý tưởng sáng chế tra trước khi nộp đơn, đỡ mất tiền tư vấn oan.
Gốc: WIPO — Patent Glossary (eTISC) và Glossary of terms concerning industrial property, định nghĩa chuẩn quốc tế về patent, applicant, claims, IPC, term of patent (thường 20 năm). Link: https://etisc.wipo.int/forums/patent-search-and-analysis/help-us-develop-patent-glossary
(Kiểm chứng 11/11: WIPO eTISC có Patent Glossary với các mục Abstract, Applicant, Claims, Description, IPC, Term of Patent; nguồn ghi EPO + WIPO PCT Glossary.)
Trục đổi: đổi ngách (thuật ngữ patent quốc tế khô → tiếng Việt + ví dụ phát minh VN) + đổi cách hiển thị (glossary pháp lý → glossary cho người có ý tưởng, kèm "nộp đơn ở đâu").
SCAMPER: Adapt (định nghĩa WIPO → tiếng Việt + ví dụ VN) + Combine (glossary + checklist trước khi nộp đơn). TRIZ: tự phục vụ (tự tra trước, không cần tư vấn ngay).
Tiền: ads + affiliate dịch vụ tư vấn sở hữu trí tuệ (chỉ giới thiệu, ghi rõ không thay tư vấn pháp lý) + bản PDF checklist nộp đơn 29k.
Làm: 2 buổi (seed 80 thuật ngữ, đối chiếu luật SHTT VN — ghi rõ chỉ tham khảo).

### G5-G6. Glossary ký hiệu toán học — tra cứu theo hình ký hiệu, không cần biết tên — ★4 — Chờ duyệt
Mô tả: Người dùng vẽ/chọn hình ký hiệu (∑, ∫, ∈, ∀, √...) hoặc gõ mô tả ("ký hiệu giống chữ E ngược") ra tên ký hiệu + đọc là gì + dùng khi nào + 1 ví dụ. Lọc theo chủ đề (đại số, logic, giải tích, xác suất). Học sinh gặp ký hiệu lạ trong sách tra 1 cú nhấp thay vì hỏi thầy.
Khác thẻ G5-G1 (glossary thuật ngữ toán theo tên): thẻ này tra cứu theo HÌNH ký hiệu, cho người không biết tên ký hiệu là gì.
Gốc: Wikipedia — List of mathematical symbols, danh sách ký hiệu toán chuẩn theo chủ đề. Link: https://en.wikipedia.org/wiki/List_of_mathematical_symbols
Trục đổi: đổi cách hiển thị (list theo tên → tra cứu theo hình ký hiệu/mô tả) + đổi ngách (độc giả tiếng Anh → học sinh VN, ví dụ theo SGK).
SCAMPER: Reverse (thay vì tra theo tên, tra theo hình — vì người tra vốn không biết tên) + Adapt (ví dụ theo SGK VN).
Tiền: ads + bản poster ký hiệu toán treo lớp 29k + affiliate sách tham khảo.
Làm: 1–2 buổi (seed 100 ký hiệu).

### G5-G7. Glossary thuật ngữ lịch sử khoa học — phương pháp khoa học, paradigm, peer review... — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ về cách khoa học vận hành (giả thuyết, thực nghiệm, falsifiability, paradigm, peer review, reproducibility...): định nghĩa 2 dòng, 1 câu chuyện thật trong lịch sử khoa học (ví dụ: 1 phát hiện bị peer review bác rồi sau đó đúng), phân biệt cặp dễ nhầm (giả thuyết vs lý thuyết; tương quan vs nhân quả trong khoa học). Người đọc tin khoa học phân biệt được "nghiên cứu thật" với "tin giật gân".
Gốc: Stanford Encyclopedia of Philosophy — mục Scientific Method và các mục triết học khoa học, định nghĩa chuẩn về phương pháp khoa học. Link: https://plato.stanford.edu
Trục đổi: đổi ngách (triết học khoa học học thuật → glossary cho người đọc tin khoa học hằng ngày) + đổi cách hiển thị (bài luận dài → thuật ngữ tra cứu + câu chuyện thật).
SCAMPER: Adapt (mượn khung khái niệm của Stanford Encyclopedia sang ví dụ đời thường) + Combine (glossary + mục "tin này có đáng tin không" — checklist kiểm tra nghiên cứu).
Tiền: ads + bản PDF "đọc tin khoa học không bị lừa" 29k + affiliate sách lịch sử khoa học.
Làm: 2 buổi (seed 80 thuật ngữ).

### G5-G8. Glossary thuật ngữ đọc biểu đồ & số liệu trên báo — bẫy biểu đồ, base rate, cherry-picking — ★5 — Chờ duyệt
Mô tả: Tra cứu các bẫy số liệu hay gặp trên báo/mạng (trục y bắt đầu từ 50, cherry-picking, base rate, Simpson's paradox, survivorship bias...): định nghĩa 2 dòng, 1 biểu đồ thật bị bóp méo (vẽ lại minh họa, không lấy ảnh báo), và cách nhận ra trong 10 giây. Đọc xong nhìn biểu đồ nào cũng biết "chỗ này có vấn đề".
Khác thẻ D11 (glossary thiên kiến nhận thức — thiên kiến tâm lý chung): thẻ này chỉ bẫy trong biểu đồ/số liệu, có hình minh họa.
Gốc: Seeing Theory (Đại học Brown) — phần về hiểu sai thống kê + mô phỏng trực quan. Link: https://seeingtheory.brown.edu
(Khác thẻ G5-G2 cùng gốc Seeing Theory: G2 là thuật ngữ thống kê cơ bản; G8 chỉ bẫy/bóp méo biểu đồ và số liệu trên báo.)
Trục đổi: đổi topic (thuật ngữ thống kê → bẫy biểu đồ trên báo) + đổi cách hiển thị (mô phỏng tương tác → glossary tra cứu có biểu đồ minh họa bóp méo).
SCAMPER: Adapt (ví dụ thống kê Mỹ → ví dụ báo/mạng VN) + Modify (thêm "cách nhận ra trong 10 giây").
Tiền: ads + bản PDF "10 bẫy biểu đồ" 29k + gói cho giáo viên dạy đọc số liệu 49k/tháng.
Làm: 2 buổi (seed 60 bẫy/biểu đồ minh họa tự vẽ).

### G5-G9. Glossary đơn vị đo lường cổ Việt Nam — mẫu, sào, thước, cân, đấu đổi ra metric — ★4 — Chờ duyệt
Mô tả: Tra cứu đơn vị đo cổ VN (mẫu, sào, thước, tấc, cân, lạng, đấu, thăng...): định nghĩa 2 dòng, đổi ra đơn vị hiện đại (1 mẫu = 3.600 m² — ghi rõ con số này thay đổi theo thời kỳ/vùng, cần đối chiếu), ví dụ trong văn bản/sách sử thật ("ruộng 5 mẫu nghĩa là bao nhiêu"), phân biệt đơn vị dễ nhầm (thước ta vs thước tây, cân ta vs cân tây). Đọc sử, đọc truyện cổ không còn mù số đo.
Gốc (format nước ngoài): Wikipedia — Vietnamese units of measurement, danh sách đơn vị đo cổ VN có quy đổi. Link: https://en.wikipedia.org/wiki/Vietnamese_units_of_measurement
Trục đổi: đổi cách hiển thị (bảng quy đổi khô trên Wikipedia → glossary tra cứu có ví dụ văn bản thật + cảnh báo "số này đổi theo thời kỳ") + đổi ngách (độc giả tiếng Anh → người Việt đọc sử/văn cổ).
SCAMPER: Adapt (bảng Wikipedia → glossary có ví dụ + cảnh báo) + Combine (glossary + máy tính đổi đơn vị cổ → metric). TRIZ: thay đổi cách hiển thị (bảng → tra cứu + máy đổi).
Tiền: ads + bản PDF bảng đổi đơn vị cổ in được 19k + affiliate sách lịch sử/văn học cổ.
Làm: 1–2 buổi (seed 60 đơn vị, ghi rõ "con số quy đổi theo thời kỳ/vùng — đối chiếu nguồn").

### G5-G10. Glossary thuật ngữ trực quan hóa dữ liệu — choropleth, Sankey, heatmap... kèm mẫu biểu đồ — ★4 — Chờ duyệt
Mô tả: Tra cứu thuật ngữ trực quan hóa dữ liệu (choropleth, Sankey, treemap, heatmap, bullet chart...): định nghĩa 2 dòng, 1 mẫu biểu đồ minh họa, "dùng khi nào / đừng dùng khi nào" (ví dụ: pie chart đừng dùng khi quá 5 lát), và dữ liệu nào hợp với biểu đồ nào. Người làm báo cáo/slide chọn đúng biểu đồ trong 1 phút.
Khác thẻ G5-G3 (thuật ngữ khoa học dữ liệu theo pipeline): thẻ này chỉ thuật ngữ về CHỌN VÀ VẼ biểu đồ, có mẫu minh họa.
Gốc: The Data Visualisation Catalogue — catalogue các loại biểu đồ, mỗi loại có mô tả + ví dụ + khi nào dùng. Link: https://datavizcatalogue.com
Trục đổi: đổi ngách (catalogue tiếng Anh cho designer → glossary tiếng Việt cho người làm báo cáo/slide) + đổi cách hiển thị (catalogue theo loại → tra cứu theo "tôi có dữ liệu dạng này, vẽ biểu đồ nào").
SCAMPER: Reverse (tra ngược từ dạng dữ liệu tới biểu đồ) + Adapt (ví dụ dữ liệu VN).
Tiền: ads + gói template biểu đồ (Excel/Google Sheets) 49k + affiliate tool trực quan hóa dữ liệu.
Làm: 2 buổi (seed 60 loại biểu đồ, mẫu tự vẽ từ dữ liệu công khai).

## Làm ngay

**G5-D2. Số liệu lịch sử Việt Nam qua 100 năm — dân số, GDP, xuất khẩu, kéo thanh trượt xem thay đổi — ★5.** Lý do: đúng format OWID đã kiểm chứng (Data Explorer có sẵn dữ liệu VN theo năm), làm nhanh 2–3 buổi từ dữ liệu công khai, tệp rộng (học sinh, giáo viên, người làm nội dung sử/kinh tế), và chưa có thẻ nào trong kho làm số liệu lịch sử VN dạng kéo timeline — khác hẳn D6 (dataset Kaggle) và G5-D6 (so sánh quốc gia).
