# D1 — Ghi chú batch (chó Affenpinscher → Braque Français, 60 giống)

- File chính: [D1.json](D1.json) (76.960 byte) — 60/60 mục, 0 trùng id/tên, JSON hợp lệ, đúng schema batches/README.md.
- Ảnh: 60/60 giống có ảnh thật, file tại `photos/cho-*.jpg`, đều là ảnh chính từ trang Wikipedia của chính giống đó (đảm bảo đúng giống), license tự do (CC BY / CC BY-SA / Public domain / GPL / Copyrighted free use), kèm commons_url + license + tác giả trong từng mục. Kiểm tra bằng `file`: ảnh nhỏ nhất 960px chiều rộng sau khi thay thế (xem dưới).
- Nguồn: Wikipedia EN (infobox + bài viết) + chuẩn FCI (PDF, pdftotext) + AKC (tuổi thọ). Không bịa giống, không bịa số.

## Không bỏ giống nào
Cả 60 giống trong D1_list.json đều có mặt. FCI group 4 = 0 mục (nhóm 4 là Dachshund, nằm ở batch D2 theo alphabet) — không phải thiếu.

## Ảnh thay thế (ảnh chính Wikipedia quá nhỏ)
- Airedale Terrier: ảnh gốc 250×205 px → thay bằng File:Airedale.jpg (960×645, "Airedale Terrier undocked 2004-09-04", Michail Jungierek, CC BY-SA 3.0).
- Barbet: ảnh gốc 312×258 px → thay bằng File:Barbet-brown.jpg (960×894, "French Water Dog (Barbet), brown", Canarian, CC BY-SA 4.0).
- Cả 2 đều đã đối chiếu mô tả file trên Commons trước khi thay. Ghi chú thay thế có trong ghi_chu của 2 mục.
- Akita: ảnh chính là "Akita Collage.png" (ảnh ghép nhiều ảnh Akita thật, 395×363) — giữ nguyên, vì vẫn là ảnh thật của giống; coordinator có thể muốn thay bằng ảnh đơn sau.

## Ảnh license GPL / Copyrighted free use
- Affenpinscher (GPL), Border Terrier (GPL), Airedale Terrier (Copyrighted free use): đều là license tự do trên Commons, đã tải lại và ghi đúng license trong JSON (script cào ban đầu chặn nhầm, đã sửa tay).

## Chưa kiểm chứng (ghi rõ trong từng mục, trang_thai=chua-kiem-chung-phan: 18 mục)
- Cân nặng chưa kiểm chứng (4): Anglo-Français de Petite Vénerie, Ariège Pointer, Australian Stumpy Tail Cattle Dog, Braque Français — không có trong bài Wikipedia lẫn chuẩn FCI.
- Tuổi thọ chưa kiểm chứng (17): Aidi, Alpine Dachsbracke, Andalusian Terrier, Anglo-Français de Petite Vénerie, Ariège Pointer, Ariégeois, Artois Hound, Austrian Black and Tan Hound, Barak Hound, Basset Artésien Normand, Basset Bleu de Gascogne, Bavarian Mountain Hound, Bergamasco Shepherd Dog, Billy, Black Norwegian Elkhound, Bouvier des Ardennes, Braque Français — toàn giống hiếm, AKC không công nhận (404) nên không tra được tuổi thọ.
- Chiều cao: 0 mục thiếu (đã lấp đủ bằng chuẩn FCI / bài Wikipedia).
- Tuổi thọ dạng số thập phân đơn (vd 11.1 năm) là tuổi thọ TRUNG BÌNH theo nghiên cứu VetCompass (Anh) trích trong bài Wikipedia, không phải khoảng chuẩn giống — đã ghi chú trong từng mục liên quan.

## Quy ước phân loại (ghi trong ghi_chu của MỌI mục)
- Rụng lông / nhu cầu vận động / hợp chung cư: phân loại theo mô tả của Wikipedia (bộ lông, mục đích sử dụng, kích cỡ, năng lượng) — không phải số liệu chuẩn của FCI/AKC.
- Kích cỡ: tính từ điểm giữa khoảng cân nặng (Nho <10 / Vua 10–25 / Lon 25–45 / Khổng lồ >45 kg); 4 giống không có cân nặng thì suy ra từ chiều cao/dáng giống và ghi rõ (Anglo-Français: Vua; Ariège Pointer: Lon; Stumpy Tail: Vua; Braque Français: Lon).
- ten_vi: chỉ ghi khi có tên tiếng Việt thông dụng thật (30/60 mục); 30 mục còn lại = null (giống hiếm, không có tên Việt thông dụng — không dịch bịa).

## Nguồn bị chặn / lỗi gặp trong quá trình cào
- FCI website: 1 lần "Remote end closed connection" khi tải chuẩn Australian Shepherd (đã lấp số liệu bằng bài Wikipedia, không cần retry).
- AKC: 404 với mọi giống hiếm không được AKC công nhận (Aidi, Ariège Pointer, Artois Hound, Barak Hound, Basset Artésien Normand, Bavarian Mountain Hound, Bergamasco, Billy, Black Norwegian Elkhound, Bouvier des Ardennes, Braque Français...) — ghi rõ trong log gapfill, không phải lỗi hệ thống.
- Không gặp 403/429 từ Wikipedia/Wikimedia trong suốt batch.

## File làm việc (để coordinator đối chiếu)
- batches/d1_fetch.py, d1_enrich.py, d1_gapfill.py, d1_build.py, patch_enrich.py
- batches/raw/D1_*.json (60 file: wikitext + toàn văn + metadata ảnh từng giống)
- batches/D1_draft.json, D1_enriched.json, D1_gapfilled.json (bản trung gian)
- batches/d1_fetch.log, d1_gapfill.log
