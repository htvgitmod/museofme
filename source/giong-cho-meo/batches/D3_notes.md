# Batch D3 — Ghi chú (English Springer Spaniel → Istrian Coarse-haired Hound, 60 giống chó)

## Kết quả
- 60/60 giống hoàn thành, 0 giống bỏ. File: `batches/D3.json` (71.520 byte).
- Ảnh: 60/60 giống có ảnh thật đã tải về `photos/` (tổng 11,72 MB), 0 giống "chưa có ảnh".
- Đã kiểm chứng đầy đủ (`da-kiem-chung`): 35/60. Chưa kiểm chứng một phần: 25/60.
- Không có nguồn nào bị chặn 403/429 trong batch này (Wikipedia API, FCI, AKC đều trả 200).

## Nguồn số liệu (theo thứ tự ưu tiên)
1. **Chuẩn FCI (PDF, fci.be)** — chiều cao/cân nặng cho 30 giống thiếu số trên Wikipedia (đã tải 30 PDF vào `batches/fci_pdfs/`, trích bằng pdftotext). FCI thường KHÔNG ghi cân nặng với chó săn mùi và KHÔNG ghi tuổi thọ với mọi giống.
2. **Wikipedia EN** — tóm tắt, tính cách, chiều cao/cân nặng khi có trong bài (trích từ full wikitext, `batches/D3_full_wikitext.json`).
3. **AKC (akc.org)** — tuổi thọ + cân nặng (pounds → kg) cho 36/44 giống thử; 8 giống AKC không có trang: English Toy Terrier, Estonian Hound, Fila Brasileiro, Finnish Hound, Galgo Español, German Roughhaired Pointer, German Spaniel, Greenland Dog.

## Chưa kiểm chứng (ghi trong từng mục, `trang_thai=chua-kiem-chung-phan`)
- Tuổi thọ: 24/60 chưa có số (chủ yếu chó săn mùi hiếm châu Âu: Estonian Hound, Fila Brasileiro, Finnish Hound, Galgo, Gascon, German Hound, German Roughhaired Pointer, German Spaniel, Gończy Polski, 3 giống Grand Anglo-Français, Grand Bleu, Grand Griffon Vendéen, Greek Harehound, Greenland Dog, Griffon Bleu, Griffon Fauve, Griffon Nivernais, Halden, Hanover, Hygen, Istrian + English Toy Terrier). FCI không công bố tuổi thọ; AKC không có trang; The Kennel Club thử 1 URL cũng 404 nên dừng, không đoán số.
- Cân nặng: 18/60 chưa có số (FCI không ghi cân nặng với đa số chó săn mùi nhóm 6). Kích cỡ của các giống này suy từ chiều cao và đã ghi rõ trong `ghi_chu_chua_kiem_chung`.
- Tuổi thọ mâu thuẫn giữa AKC và nghiên cứu Anh trên Wikipedia (đã ghi cả hai trong ghi chú, lấy số AKC làm số chính): Flat-coated Retriever (AKC 8-10 vs Wiki 11), Irish Wolfhound (AKC 6-8 vs Wiki 9), Irish Setter (AKC 12-15 vs Wiki 11-12), Irish Water Spaniel (AKC 12-13 vs Wiki 10), English Springer Spaniel (AKC 12-14 vs Wiki 11), Golden Retriever (AKC 10-12 vs Wiki 10 và nghiên cứu khác 13), Gordon Setter (AKC 12-13 vs Wiki 10-15), Great Dane (AKC 7-10 vs Wiki 10).

## Ảnh — trường hợp đặc biệt
- **German Spitz**: ảnh chính trên Wikipedia (`Goldilocks.gif`, giấy phép FAL) là tranh minh họa cũ, KHÔNG phải ảnh chó thật → đã thay bằng ảnh thật `Un chien Spitz allemand.jpg` (CC BY-SA 3.0, tác giả Teuteul, French Wikipedia) lấy từ chính bài viết, đã xem trực tiếp và xác nhận đúng giống spitz trắng đuôi cuộn. Ghi rõ trong mục.
- Các ảnh còn lại đều là ảnh infobox/pageimage từ chính trang Wikipedia của giống đó (đảm bảo đúng giống), giấy phép PD/CC-BY/CC-BY-SA, đã ghi license + tác giả + link Commons từng ảnh trong JSON.
- Đã kiểm tra bằng PIL: cả 60 file đều là ảnh hợp lệ, không file nào hỏng/rỗng; kích thước nhỏ nhất vẫn ≥200px (German Hound 18 KB là ảnh lịch sử 1915).

## FCI group
- Ghi từ mã chuẩn trong URL fcistd (`NNNgGG-en.pdf`) và đối chiếu bài viết. 6 giống có fcistd dạng cũ (.doc/nomenclature HTML) vẫn xác định được nhóm 6 (chó săn mùi): Gascon Saintongeois (FCI 021), German Hound (299, bài viết ghi rõ Group 6), Griffon Bleu de Gascogne (032), Halden Hound (267), Hygen Hound (266), Istrian Coarse-haired Hound (152).
- Batch này không có giống nhóm 4 (Dachshund) — đúng theo phạm vi alphabet, không phải thiếu sót.

## Tên tiếng Việt
- Chỉ ghi 4 tên thông dụng thật: German Shepherd "Chó Becgie Đức", Golden Retriever "Chó Golden Retriever", French Bulldog "Chó Bull Pháp", Great Dane "Chó Great Dane". 56 giống còn lại để null (không dịch bịa).

## File làm việc trong batch
- `batches/D3.json` (đầu ra chính), `batches/D3_raw.json` (dữ liệu thô Wikipedia + ảnh), `batches/D3_full_wikitext.json` (full wikitext 60 bài), `batches/D3_fci_extract.json` + `batches/D3_fci_hw.json` (trích chuẩn FCI), `batches/D3_akc.json` (tuổi thọ/cân nặng AKC), `batches/fci_pdfs/` (30 PDF chuẩn FCI), `batches/fetch_D3.py` + `batches/build_D3.py` (script cào/build, chạy lại được).
