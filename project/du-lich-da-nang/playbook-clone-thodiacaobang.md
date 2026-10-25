# Playbook clone mô hình thodiacaobang.com cho tỉnh khác

Ngày soạn: 19/10/2026 · Từ phân tích site thodiacaobang.com trong đoạn chat "Phân tích website Thodịacaobang để nhân bản"

Mục tiêu của file này: bạn làm theo từng bước là có một bản clone chạy được, không phải mò lại từ đầu.

---

## 1. Mô hình của ổng là gì (tóm tắt)

Không phải "gắn link Agoda" đơn thuần. Đó là **hệ sinh thái 5 dòng tiền**:

1. **Affiliate Agoda** — card khách sạn hiển thị giá cào từ Agoda, cron chạy mỗi sáng ~8:35 ("cập nhật 08:35 19/10 · giá có thể thay đổi"). Mỗi card có: giá/đêm, giá gạch + % giảm, số sao, điểm đánh giá + số review, bữa sáng/wifi, hạng phòng mẫu, ngày nhận phòng mẫu (đang để +14 ngày, "Đêm 02/11").
2. **Booking trực tiếp với đối tác địa phương** — đây mới là chỗ ăn dày. Trang /booking/ là hệ thống đặt phòng hoàn chỉnh: chọn hạng phòng, số lượng, hiện tồn kho "Còn X phòng", giá đã VAT. ~6 đối tác: 3 Cốm Homestay (Bản Giốc, Bảo Lạc, Nà Cạn — nhiều khả năng là chuỗi của ổng), KS Minh Anh, KS So Oanh, Xenia House.
3. **Thuê xe máy** — /thue-xe-may-cao-bang/: chọn ngày nhận/trả, 9 mẫu xe (180k–700k/ngày, hiện tồn kho), form đặt + cọc 30%. Dịch vụ của chính ổng.
4. **Cross-sell hệ sinh thái** — trang trải nghiệm camping link sang campingnuithung.id.vn, site riêng của ổng.
5. **Thu lead tư vấn lịch trình** — trang /tu-van-lich-trinh-du-lich-cao-bang-tu-tuc/.

> Lưu ý thật lòng: "ra được hoa hồng" là ổng nói, tôi không kiểm chứng được doanh thu thực của ổng. File này clone được *mô hình*, không đảm bảo *doanh thu*.

## 2. Cấu trúc site (từ sitemap)

Quy mô: ~20 bài blog, ~35 page, 1 custom post type "trải nghiệm". Tech: WordPress + custom post type + theme/plugin tự code cho phần booking, tìm phòng, cào giá. Sitemap kiểu RankMath.

Các loại trang:
- **Trang chủ:** tìm phòng theo ngày + gợi ý + ưu đãi + điểm đến + lịch trình + blog
- **Money page:** /phong-gan-{điểm}/ (gần thác Bản Giốc, Pác Bó, trung tâm...) — đây là trang kiếm tiền chính
- **Trang KS đối tác** đặt trực tiếp
- **Điểm đến** /diem-du-lich/ (lọc theo đơn vị hành chính, loại điểm, cụm điểm)
- **Lịch trình**, **Trải nghiệm** (cưỡi ngựa, chèo SUP, camping)
- **Công cụ:** /tim-kiem-phong/, /phong-giam-gia/

**Tuyến nội dung blog — 5 tuyến, rõ dấu AI viết theo template:**
1. Review chỗ nghỉ: "1. Thông tin chung / 2. Ưu điểm / 3. Phù hợp với ai?" (vd AK Homestay, Mường Thanh, Mế Farmstay...)
2. Money guide: "Phòng gần Thác Bản Giốc – Giá tốt, view đẹp" (7 mục + FAQ), nhúng card giá Agoda ngay đầu bài
3. Listicle kinh nghiệm: "5 lưu ý khi đi thác Bản Giốc", "Đi thác Bản Giốc mặc gì cho đẹp"
4. Lịch trình: "Hà Nội – Cao Bằng 3N2Đ tự túc" (chế từ talkshow)
5. Bài dịch vụ: thuê xe máy (~2000 chữ, nhồi từ khoá)

Nhịp đăng: đợt đầu tháng 6–7/2026 (~15 bài), sau đó ~2–3 bài/tháng.

**Đi link nội bộ:** Blog → money page /phong-gan-X/ → card Agoda. Trang chủ điều hướng tất cả. Bài thuê xe link sang site camping riêng.

## 3. Bí mật đáng tiền nhất: link affiliate bị cloak

Ổng **không gắn link Agoda trực tiếp** lên các card. Tất cả nút "Xem phòng & giá" đều đi qua redirect nội bộ:

```
thodiacaobang.com/wp-admin/admin-post.php?action=cblt_agoda_click&lodging_id=1516&cblt_source=deals
```

Click → server của ổng nhận → mới gắn mã affiliate rồi đá sang Agoda. 3 lợi ích:
1. **Giấu mã affiliate** — đối thủ view-source không thấy, không cướp được
2. **Đếm click theo nguồn** — `cblt_source=deals` vs `lodging_card` cho biết đơn đến từ trang ưu đãi hay card trang chủ, để biết chỗ nào convert tốt
3. **Đổi link đích một chỗ** — mai muốn chuyển sang Booking.com hay Travelpayouts chỉ sửa server, không sửa từng bài

Mã affiliate thật của ổng lộ ở badge "Đặt phòng Agoda" dưới chân trang: `cid=1931110`.

**Bài học cho bản clone:** đừng gắn link affiliate trần vào bài. Làm redirect nội bộ kiểu `/go/agoda/<id-khach-san>` vừa cloak vừa tracking được nguồn click. Code mẫu ở Phụ lục A — 1 dev làm trong buổi là xong.

## 4. Affiliate Agoda — số liệu đã kiểm chứng (19/10/2026)

- **Hoa hồng (chương trình trực tiếp partners.agoda.com):** 4% → 7% theo bậc — 0–49 booking/tháng: 4%; 50–299: 4.5%; 300–999: 5%; 1000+: 7%. Tính trên giá booking sau thuế/phí.
- **Cookie: 1 ngày.** Khách phải đặt trong 24h sau click thì bạn mới được tính. → Bắt buộc đánh đúng người đang có ý định đặt *ngay* (search intent "đặt phòng", "giá phòng"), không phải người đọc chơi.
- **Trả tiền trên booking đã "departed"** — chỉ khi khách đã ở xong và trả phòng. Thanh toán hàng tháng, **min payout $200** (chưa đủ thì cộng dồn).
- **Đăng ký:** https://partners.agoda.com/en-us/ — duyệt mất vài ngày, cần có website.
- **Đường tắt cho người mới VN:** Travelpayouts (mức cố định ~6%, cookie 1 ngày, thanh toán linh hoạt hơn) hoặc Ecomobi Passio (Agoda ~4.8%, duyệt dễ hơn cho creator VN).
- **Cấm:** chạy quảng cáo trả tiền dùng thương hiệu Agoda (paid search/SEM với từ khoá Agoda) — đọc kỹ điều khoản trước khi chạy ads.

Nguồn kiểm chứng: creator-hero.com, uppromote.com, travelpayouts.com, ecomobi.com (truy cập 19/10/2026).

## 5. Playbook từng bước

### Bước 0 — Chọn cách bắt đầu: lean hay full
- **Lean (không cần dev):** WP + đăng bài tay + gắn link affiliate tay qua redirect nội bộ. Có đơn đầu tiên rồi mới đầu tư automation.
- **Full (cần dev hoặc bạn học làm):** thêm pipeline cào giá + hệ thống booking trực tiếp như của ổng.
- Khuyên: bắt đầu lean. Phần khó nhất không phải content AI mà là pipeline data + booking.

### Bước 1 — Chọn tỉnh
Tiêu chí: (a) du lịch tự túc phát triển tốt; (b) có search demand ("khách sạn gần X", "thuê xe máy Y"); (c) cạnh tranh SEO thấp — né Đà Lạt, Phú Quốc, Đà Nẵng lúc đầu; (d) có homestay/đối tác địa phương để sau này đàm phán deal trực tiếp; (e) bạn hiểu hoặc có kết nối ở đó càng tốt.
Gợi ý khởi điểm: Hà Giang, Mộc Châu, Phú Yên, Côn Đảo. (Chưa chốt — cần check search volume trước khi quyết.)

### Bước 2 — Đăng ký affiliate NGAY
Đăng ký partners.agoda.com (và/hoặc Travelpayouts, Ecomobi) ngay từ bây giờ vì duyệt mất vài ngày. Có mã affiliate rồi mới test được link.

### Bước 3 — Domain + web
- Domain theo công thức `thodia{tinh}.com` (vd thodiahagiang.com). Branding "thổ địa" tạo cảm giác chuyên gia địa phương.
- WordPress + theme nhẹ + custom post type: Khách sạn / Điểm đến / Trải nghiệm / Lịch trình. RankMath cho sitemap.
- Hosting: bắt đầu shared hosting VN là đủ.

### Bước 4 — Redirect cloak (làm ngay từ đầu)
Đừng bao giờ gắn link affiliate trần. Dựng `/go/agoda/<id>` theo mẫu Phụ lục A, gắn tracking nguồn click (`?src=deals`, `?src=card-home`...).

### Bước 5 — Content đợt 1 (15 bài đầu)
Theo đúng 5 tuyến ở mục 2, AI viết + bạn biên tập. **Tuyệt đối không copy bài của ổng** — dính bản quyền, Google phạt trùng lặp là chết SEO.
Template bài review chỗ nghỉ: 1. Thông tin chung / 2. Ưu điểm / 3. Phù hợp với ai? + nút "Book X" (link cloak) + FAQ.

### Bước 6 — Money pages
Làm /phong-gan-{landmark}/ cho từng điểm hot của tỉnh đó. Đây là trang convert chính: card giá Agoda ngay đầu bài + blog đổ link nội bộ về đây.

### Bước 7 — Pipeline giá tự động (khi đã có traffic)
Cron mỗi sáng cào/cập nhật giá. **Chú ý ToS và rate limit** — Agoda có data feed/API cho affiliate, dùng đường chính thức, đừng scrape lậu.

### Bước 8 — Đàm phán đối tác địa phương (chỗ tiền to)
Khi có traffic, liên hệ 10 homestay/KS ở tỉnh đó: đề xuất đặt phòng trực tiếp qua web bạn (bạn ăn chênh lệch hoặc hoa hồng cao hơn Agoda nhiều). Thêm dịch vụ của chính bạn: thuê xe, tour, camping — như ổng làm.

### Bước 9 — Đo lường
Tracking click theo nguồn (như `cblt_source` của ổng) để biết trang nào convert tốt, dồn content vào đó.

## 6. Checklist 30–60–90 ngày

**30 ngày:** affiliate được duyệt · WP lên + redirect cloak chạy · 15 bài đầu live · 3 money pages · Search Console submit sitemap
**60 ngày:** 30 bài · check query nào có impression, sửa/bổ sung content theo đó · test click → booking đầu tiên
**90 ngày:** pipeline giá tự động · liên hệ 10 homestay đàm phán deal trực tiếp · đánh giá: traffic và click có đủ để đi tiếp không

## 7. Ước tính chi phí

- **Lean:** domain ~300k/năm + hosting share ~100k/tháng + WP miễn phí → **dưới 2 triệu để bắt đầu**.
- **Full:** thêm VPS + thuê dev làm plugin booking/pipeline giá (chi phí dev tính riêng khi tới bước đó).

## 8. Rủi ro & lưu ý thật lòng

1. Cookie 1 ngày + payout sau khi khách trả phòng + min $200 → dòng tiền chậm 1–2 tháng đầu, đừng kỳ vọng tiền về ngay.
2. SEO cần 3–6 tháng mới có traffic đáng kể. Đây là hướng **trung–dài hạn**, không phải tiền sinh tồn trong 2–4 tuần.
3. Không copy content của ổng (bản quyền + Google phạt duplicate).
4. Cào giá phải đúng ToS; Agoda cấm chạy paid search dùng brand của họ.
5. Kết nối với mục tiêu của bạn: pipeline content AI + cron cập nhật giá này chính là thứ bạn có thể tái dùng cho mục tiêu tự động hoá page 90% — làm một lần, dùng hai nơi.

---

## Phụ lục A — Code mẫu redirect cloak (WordPress)

```php
// Cho vào functions.php của child theme hoặc plugin nhỏ
add_action('admin_post_cblt_agoda_click', 'my_agoda_click');
add_action('admin_post_nopriv_cblt_agoda_click', 'my_agoda_click');

function my_agoda_click() {
    $lodging_id = isset($_GET['lodging_id']) ? intval($_GET['lodging_id']) : 0;
    $source = isset($_GET['cblt_source']) ? sanitize_key($_GET['cblt_source']) : 'unknown';

    // TODO: ghi log vào DB: lodging_id, source, thời gian, IP — để biết nguồn nào convert tốt

    // Link affiliate gắn theo từng khách sạn (lưu trong custom field)
    $agoda_url = get_post_meta($lodging_id, 'agoda_affiliate_url', true);
    if (!$agoda_url) {
        wp_redirect(home_url('/'));
        exit;
    }
    wp_redirect($agoda_url, 302);
    exit;
}
```

Dùng: `https://thodiahagiang.com/wp-admin/admin-post.php?action=cblt_agoda_click&lodging_id=123&cblt_source=deals`
Muốn URL đẹp hơn (`/go/agoda/123`) thì thêm rewrite rule — dev làm trong buổi.

## Phụ lục B — Mẫu cấu trúc URL

- `/phong-gan-{landmark}/` — money page (vd /phong-gan-ma-pi-leng/)
- `/phong-giam-gia/` — trang ưu đãi
- `/thue-xe-may-{tinh}/` — trang dịch vụ
- `/diem-du-lich/` — lọc theo huyện/loại điểm/cụm điểm
- `/tu-van-lich-trinh-du-lich-{tinh}-tu-tuc/` — thu lead
