# Batch D6 — Ghi chú (57 giống chó, Shetland Sheepdog → Šarplaninac)

## Kết quả
- **57/57 giống hoàn thành, không bỏ giống nào, không trùng id/tên.**
- **57/57 ảnh thật đã tải về** (`photos/cho-*.jpg`, tổng 10,69 MB), tất cả lấy từ ảnh chính (pageimage) của chính trang Wikipedia EN của giống đó → đúng giống theo construction. Giấy phép toàn bộ là tự do: CC BY / CC BY-SA (2.0/3.0/4.0), CC0, Public domain. Tác giả + URL Commons ghi trong từng mục (`anh.license`, `anh.tac_gia`, `anh.commons_url`).
- **38 mục `da-kiem-chung`, 19 mục `chua-kiem-chung-phan`** (xem danh sách dưới).
- File chính: `batches/D6.json` (JSON hợp lệ, đúng schema, enum đúng, FCI 1–10 đủ cả 57).
- File trung gian: `D6_raw.json` (summary + infobox + ảnh), `D6_enriched.json` (infobox parse + temperament + lifespan Wiki), `D6_gaps.json` (AKC + lifespan Wiki lần 2), script `scrape_d6.py`, `enrich_d6.py`, `fill_gaps_d6.py`, `fill_akc_d6.py`, `assemble_d6.py`.

## Nguồn số liệu (theo thứ tự ưu tiên)
1. Wikipedia EN — infobox của từng giống (cân nặng/chiều cao, hợp nhất khoảng đực + cái) + mục Temperament/Health trong bài.
2. AKC (akc.org/dog-breeds/<slug>/) — Life Expectancy / Height / Weight, dùng khi Wikipedia thiếu. Truy cập được 43/55 giống thử (200 OK).
3. FCI (fci.be) — nhóm FCI từ URL tiêu chuẩn (`Standards/<số>g<nhóm>-en.pdf`) hoặc trang nomenclature; đã đối chiếu trực tiếp 7 nhóm còn thiếu (xem dưới).
4. Tuổi thọ: ưu tiên khoảng AKC; nếu AKC không có thì dùng giá trị nghiên cứu trên Wikipedia (ghi rõ trong ghi chú khi hai nguồn lệch nhau, vd Tibetan Terrier Wiki 13,8 năm vs AKC 15–16 năm).

## AKC 404 (12 giống, không có trang AKC — dùng Wikipedia/FCI)
Slovak Cuvac, Slovak Rough-haired Pointer, Smaland Hound, South Russian Ovcharka, Styrian Coarse-haired Hound, Tatra Hound, Tatra Shepherd Dog, Thai Bangkaew Dog, Tyrolean Hound, West Siberian Laika, Westphalian Dachsbracke, White Swiss Shepherd Dog. + 2 giống không thử AKC: Český Fousek, Šarplaninac.
Không có nguồn nào bị chặn 403/429 trong batch này (Wikipedia + AKC + FCI đều truy cập được).

## Nhóm FCI — 7 giống phải xác minh riêng (đã xong)
- Whippet = 10 (fci.be: Sighthounds), Tosa = 2 (fci.be: n°2 Pinscher/Molossoid), West Siberian Laika = 5 (n°5 Spitz), Westphalian Dachsbracke = 6 (n°6 Scent hounds), Smaland Hound = 6 (SMALANDSSTOVARE-129, n°6), White Swiss Shepherd Dog = 1 (tiêu chuẩn 347g01), Tibetan Spaniel = 9 (TIBETAN-SPANIEL-231, n°9 Companion and Toy Dogs).
- Slovak Cuvac = 1: theo danh mục FCI (chó chăn gia súc, tiêu chuẩn số 142); trang chi tiết FCI chuyển hướng (302) nên chưa đối chiếu trực tiếp → mục này đánh `chua-kiem-chung-phan`, ghi rõ trong ghi chú.

## 19 mục "chưa kiểm chứng phần" — chi tiết
| Giống | Chưa kiểm chứng |
|---|---|
| Slovak Cuvac | Tuổi thọ |
| Slovak Rough-haired Pointer | Cân nặng, chiều cao, tuổi thọ |
| Smaland Hound | Cân nặng, tuổi thọ |
| Smooth Fox Terrier | Chiều cao |
| South Russian Ovcharka | Tuổi thọ; cân nặng/chiều cao chỉ có mức tối thiểu trong tiêu chuẩn FCI (ghi "từ … trở lên") |
| Styrian Coarse-haired Hound | Cân nặng, chiều cao, tuổi thọ |
| Tatra Hound | Cân nặng, tuổi thọ |
| Tatra Shepherd Dog | Cân nặng, chiều cao, tuổi thọ |
| Thai Bangkaew Dog | Tuổi thọ |
| Tosa | Chiều cao |
| Tyrolean Hound | Cân nặng, chiều cao, tuổi thọ |
| West Siberian Laika | Cân nặng, chiều cao, tuổi thọ |
| Westphalian Dachsbracke | Cân nặng, chiều cao, tuổi thọ |
| Wetterhoun | Tuổi thọ (AKC không liệt kê) |
| White Swiss Shepherd Dog | Tuổi thọ |
| Wire Fox Terrier | Chiều cao |
| Xoloitzcuintle | Cân nặng, chiều cao (giống có 3 cỡ; AKC chỉ liệt kê cỡ miniature/toy nên không dùng làm số liệu chung) |
| Český Fousek | Cân nặng, chiều cao, tuổi thọ |
| Šarplaninac | Tuổi thọ; chiều cao chỉ có mức tối thiểu trong tiêu chuẩn (ghi "từ 58 cm trở lên") |

## Lưu ý khác
- `rung_long` / `van_dong` / `hop_chung_cu` là suy luận từ loại lông, mục đích giống và tính cách trong bài Wikipedia (không phải số liệu đo trực tiếp) — đã ghi rõ trong `ghi_chu_chua_kiem_chung` của mọi mục.
- `ten_vi` chỉ ghi cho 12 giống có tên tiếng Việt thông dụng thật (Shiba, Husky Siberia, Shih Tzu, Yorkshire, St. Bernard, ngao Tây Tạng, chó xoáy Thái, Xolo…); các giống còn lại để `null`, không dịch bịa.
- Kích cỡ: tính từ điểm giữa khoảng cân nặng (Nho <10 / Vua 10–25 / Lon 25–45 / Khổng lồ >45 kg); giống chưa có cân nặng thì suy luận từ mô tả giống và ghi rõ (Xolo: Vua theo cỡ standard; South Russian Ovcharka: Khổng lồ).
- Ảnh độ phân giải thấp (ảnh gốc trên Commons vốn nhỏ, vẫn là ảnh đúng giống): Shikoku 296×223 (14,6 KB), South Russian Ovcharka, Staffordshire Bull Terrier (<20 KB). Các ảnh còn lại ≥426 px chiều ngang.
- 2 lỗi script đã gặp và đã sửa trong quá trình làm: (1) parser infobox không nhận template `Infobox Dogbreed` / `infobox dog breed` (khác hoa/thường, khác khoảng trắng) — đã sửa regex; (2) `fill_gaps_d6.py` truyền nhầm dict UA vào header `User-Agent` làm AKC fail toàn bộ — đã sửa và chạy lại thành `fill_akc_d6.py` (43/55 thành công).
- Không có giống nào bị trùng tên, redirect hay tuyệt chủng trong danh sách D6.
