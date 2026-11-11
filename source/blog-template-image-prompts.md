# Prompt tạo ảnh kiểu blog template

> Lưu ý quan trọng: prompt GỐC lúc tạo ảnh ngày 10/11/2026 không còn lưu ở đâu
> cả — file JSON trong `imagine_media/` chỉ giữ link ảnh, database tool-call
> trống, transcript chat cũng không ghi prompt. File này là prompt TÁI TẠO từ
> ảnh thật `travel.webp` trong template v9 + spec template đã chốt. Dùng được
> ngay để tạo ảnh cùng phong cách — chỉ cần đổi chủ thể, giữ nguyên đoạn style.

## Ảnh chính trong template v9 (travel.webp)

Ảnh: phố cổ Hội An vẽ màu nước — tường vàng, đèn lồng cam/đỏ treo ngang phố,
cửa chớp gỗ, chậu cây xanh, xe đạp cổ màu xanh cổ vịt có giỏ mây ở góc phải,
đường đá cuội, viền ảnh phai mờ kiểu màu nước trên nền giấy kem. Đây cũng là
nội dung bài mẫu trong template: "Phố vàng, đèn cam và một chiếc xe đạp cũ".

### Prompt chính (copy-paste, tiếng Anh — model ảnh hiểu tốt nhất)

```
Watercolor illustration of a quiet old town street in Hoi An, Vietnam:
ochre-yellow old shophouses with wooden shutters, strings of glowing orange
and red silk lanterns hanging across the narrow cobblestone street, potted
plants on the sidewalks, a vintage teal bicycle with a wicker basket parked
in the right foreground. Loose black ink sketch lines, soft translucent
watercolor washes, pale faded colors, lots of cream paper showing through,
edges dissolving into the paper like a watercolor sketchbook page. Warm,
nostalgic, gentle morning light. No people, no text, no watermark.
```

### Quy tắc style — giữ nguyên khi đổi chủ thể

- Màu: nhạt / phai (faded), nền giấy kem / vàng-cam rất nhạt; điểm nhấn cam
  và đỏ gạch.
- KHÔNG: trắng đen, màu đậm bão hòa, ảnh chụp thật (photorealistic), chữ
  trong ảnh, watermark.
- Khổ ảnh: ngang 3:2 (khổ ảnh trong template). Viền phai mờ vào nền giấy.
- Đổi chủ thể: giữ nguyên toàn bộ đoạn style, chỉ thay phần mô tả cảnh.
  Ví dụ: "a quiet Hanoi street at dawn", "a small Saigon cafe with
  plastic stools", "a Da Lat pine hill with a small church".

## 4 kiểu mẫu đã thử ngày 10/11 (để đối chiếu)

Ngày 10/11 đã sinh 4 ảnh mẫu theo 4 phong cách để John chọn. Prompt dưới đây
cũng là tái tạo từ mô tả từng kiểu lúc đó (file ảnh gốc còn trong
`workspace/imagine_media/`).

1. **Hand-drawn / Sketchbook** — sổ tay vẽ tay.
   ```
   Hand-drawn sketchbook illustration, black ink lines on warm yellow paper,
   wavy underlines, margin doodles, light watercolor touches, nostalgic
   notebook feel. Pale faded colors, no text.
   ```

2. **Bullet Journal** — sổ chấm bi.
   ```
   Bullet journal spread, dotted paper, marker handwriting, hand-drawn boxes,
   washi tape, neat planner layout, warm yellow palette. Clean, organized,
   no photorealism.
   ```

3. **Scrapbook / Zine** — cắt dán.
   ```
   Scrapbook zine collage, cut-and-paste paper pieces, messy handwritten
   notes, squiggly arrows, DIY magazine style, warm colors, playful and
   imperfect.
   ```

4. **Organic Hand-lettered** — tối giản.
   ```
   Minimal organic hand-lettered illustration, pale cream-yellow background,
   delicate handwritten lettering, soft flowing curves like silk ribbons,
   lots of empty space, calm and airy.
   ```

## Spec màu/chữ của template (để ảnh khớp trang)

- Nền trang: 1 màu phẳng vàng-cam rất nhạt (không gradient).
- Ảnh: màu phai, sáng/nhạt, khớp nền; khung vẽ tay; không caption/alt dưới ảnh.
- Font: Dancing Script (tiêu đề, có subset tiếng Việt) + Itim (thân bài).
