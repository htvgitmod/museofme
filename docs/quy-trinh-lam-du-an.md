# Quy trình làm dự án với Muse (bản chốt 25/10/2026)

Tài liệu này là quy trình CHUẨN để Muse và user phối hợp làm một dự án.
Đọc xong làm theo đúng thứ tự, không bỏ bước, không tự chế thêm bước.

## 1. Khi nào áp dụng (bản sửa 25/10: tự nhận diện, không cần user chọn)

- Muse TỰ NHẬN DIỆN và tự áp quy trình này khi công việc là một PROJECT,
  không cần user phải nói "dùng quy trình project".
- Dấu hiệu nhận diện project (gặp 2 dấu hiệu trở lên là áp luôn):
  - Sản phẩm đầu ra là thứ để dùng/lưu lâu dài: web, app, game, kênh,
    hệ thống tự động, bộ nội dung dài hơi.
  - Việc gồm nhiều bước nối tiếp nhau, bước sau phụ thuộc bước trước,
    làm trong nhiều lượt/phiên chứ không xong trong một câu trả lời.
  - Có điểm chất lượng cần chốt rõ ràng (nội dung + layout/thiết kế,
    độ chính xác dữ liệu, trải nghiệm dùng thử).
  - Ví dụ tự áp luôn: dựng web Munger, dựng web Đà Nẵng, làm game,
    làm app, dựng kênh video, làm webapp.
- KHÔNG áp dụng cho việc lẻ tẻ hằng ngày (pack quét, briefing, trả lời nhanh,
  tra cứu nhanh, sửa 1 file, làm 1 ảnh/video đơn) — việc lẻ vẫn làm nhanh
  như cũ, không cần spec, không cần plan.
- Trường hợp MƠ HỒ (không rõ là project hay việc lẻ): Muse hỏi đúng 1 câu
  ngắn trước khi làm: "Cái này làm theo quy trình project nhé?" — user nói
  có thì chạy quy trình, nói không thì làm nhanh như cũ. Không hỏi lại lần 2.
- Mục tiêu của quy trình: user chỉ làm 3 việc — trả lời 1 lượt hỏi chốt,
  duyệt plan và duyệt gói. Mọi việc còn lại Muse tự lo, tự kiểm chứng,
  tự làm lại khi chưa đạt.

## 2. Nguyên tắc nền (bất di bất dịch)

1. **Spec trước, làm sau.** Không có spec 1 trang thì không bắt đầu thực thi.
2. **File plan là source of truth duy nhất.** Mọi tiến độ và quyết định đã chốt
   đều ghi vào file, không nằm trong trí nhớ của đoạn chat.
3. **Mỗi task phải có tiêu chí xong đo được.** Không có tiêu chí = chưa được làm.
4. **Một task một lượt.** Làm xong, kiểm chứng xong mới sang task tiếp theo.
5. **Không giao bản lỗi.** Chưa đạt tiêu chí thì tự sửa, tối đa 3 vòng/task.
   Kẹt quá 3 vòng mới hỏi user.
6. **Không hỏi lại cái đã chốt.** Thay đổi quyết định cũ phải ghi changelog
   kèm lý do.
7. **Nói rõ cái gì đã kiểm chứng, cái gì là ước lượng.** Không tô hồng kết quả.

## 3. Vai trò

**User làm (chỉ 3 việc, không cần chọn quy trình):**
1. Trả lời 1 lượt hỏi chốt ở Giai đoạn 0 (Muse tự nhận diện project rồi hỏi).
2. Duyệt plan tổng ở Giai đoạn 1 (duyệt hoặc đổi).
3. Duyệt từng gói ở Giai đoạn 3 (duyệt hoặc đổi, trả lời dạng "duyệt 1, đổi 2 sang B").
Trường hợp mơ hồ, user chỉ cần trả lời thêm 1 câu "có/không" khi Muse hỏi
"Cái này làm theo quy trình project nhé?"

**Muse làm (mọi việc còn lại):**
- Soạn câu hỏi chốt, soạn spec, bóc plan, thực thi từng task, tự kiểm chứng
  3 lớp, tự sửa khi chưa đạt, ghi tiến độ vào file, soạn gói duyệt, bàn giao
  và lưu trữ.

## 4. Giai đoạn 0 — Hỏi chốt (Discovery): 1 lượt duy nhất

Muse hỏi tối đa MỘT lượt, gom hết các câu hỏi khóa:

1. Mục tiêu cuối cùng là gì? Thành công trông như thế nào?
2. Làm cho ai? (đối tượng sử dụng/xem)
3. Phạm vi: gồm cái gì, và KHÔNG gồm cái gì?
4. Chuẩn chất lượng: có ví dụ mẫu nào bạn thích không? Mức tối thiểu chấp
   nhận được là gì?
5. Ràng buộc: thời gian, tiền, công cụ, tài khoản sẵn có?
6. Cái gì tuyệt đối không làm / không dùng?

Quy tắc:
- Câu nào user không trả lời được, Muse tự đề xuất phương án mặc định và ghi
  rõ: "nếu bạn không sửa thì lấy phương án này".
- Không hỏi rải rác thêm sau đó, trừ 4 trường hợp ở Mục 8.
- Output: file `SPEC.md` (1 trang) trong thư mục của project.

## 5. Giai đoạn 1 — Plan tổng

Muse bóc project thành chặng, rồi thành task. Mỗi task ghi đủ 5 dòng:

- Mã task (T1, T2...) và mô tả ngắn.
- Đầu ra cụ thể (file nào, link nào, demo nào).
- Tiêu chí xong ĐO ĐƯỢC (acceptance criteria). Ví dụ: "dataset 223 record,
  đủ 12 môn, không trùng tên, trường practice chỉ còn 1 dạng".
- Task này phụ thuộc vào task nào (nếu có).
- Trạng thái: chưa làm / đang làm / đã xong / kẹt.

Plan lưu thành 2 file trong thư mục project:
- `PLAN.md` — plan tổng + trạng thái từng task (source of truth).
- `PROGRESS.md` — nhật ký: mỗi task xong ghi 2-3 dòng (đã làm gì, lưu ý gì
  cho lượt sau).

User duyệt plan: trả lời "duyệt" hoặc "đổi task X thành Y". Chốt plan rồi mới
sang Giai đoạn 2. Plan chỉ đổi khi user yêu cầu, hoặc khi phát hiện mâu thuẫn
với spec — đổi thì ghi changelog trong `PLAN.md`.

## 6. Giai đoạn 2 — Thực thi theo vòng lặp (kiểu Ralph)

Mỗi task chạy đúng 6 bước, không bỏ bước nào:

1. **Đọc `PLAN.md`**, chọn 1 task chưa xong, theo đúng thứ tự phụ thuộc.
   Chỉ làm task đó, không làm lan sang task khác.
2. **Làm task.**
3. **Tự kiểm chứng 3 lớp:**
   - a. Kiểm tra chéo: đếm số lượng, đối chiếu nguồn, soi tính nhất quán
     (ví dụ: đủ số record, đủ số môn, không trùng, không thiếu trường).
   - b. Phản biện: đóng vai người khó tính, tìm lỗi, tìm trường hợp biên,
     tìm chỗ yếu nhất của bản vừa làm.
   - c. Chạy thử thật: demo mở được, link bấm được, nút bấm chạy được,
     file đọc được. Không chấp nhận "chắc là chạy được".
4. **Chưa đạt → tự sửa, quay lại bước 3.** Tối đa 3 vòng.
5. **Đạt → đánh dấu xong trong `PLAN.md`**, ghi progress vào `PROGRESS.md`.
6. **Sang task tiếp theo.**

Quy tắc thêm:
- Kẹt quá 3 vòng ở 1 task: dừng, báo user đúng chỗ kẹt + 2 phương án gỡ,
  không tự đoán mò tiếp.
- Tiến độ nằm trong file nên phiên làm việc có bị ngắt cũng nối tiếp được,
  không làm lại từ đầu.
- Không giao cho user bất kỳ bản trung gian nào chưa qua đủ 3 lớp kiểm chứng.

## 7. Giai đoạn 3 — Gói duyệt (kiểu pstack: kiểm chứng rồi mới báo xong)

Khi xong 1 chặng (hoặc xong toàn project), Muse giao ĐÚNG 1 gói duy nhất gồm:

1. **Demo chạy thật** — đúng định dạng user đã chốt cho loại sản phẩm đó
   (mockup web = ảnh, dashboard = HTML, video = file video, tài liệu = file).
2. **Báo cáo kiểm chứng** — đã check cái gì, số liệu bao nhiêu, còn cái gì
   chưa check được và vì sao.
3. **Tối đa 3 quyết định đánh số**, mỗi quyết định kèm:
   - Phương án Muse khuyên chọn + lý do 1-2 câu.
   - "Nếu bạn không chọn thì mặc định là gì".

User chỉ cần trả lời dạng: "duyệt 1, đổi 2 sang B". Không cần đọc lại toàn bộ
để tìm lỗi — tìm lỗi là việc của Muse ở Giai đoạn 2.

Quyết định đã duyệt được ghi ngay vào `PLAN.md`, không hỏi lại ở chặng sau.

## 8. Khi nào Muse PHẢI dừng và hỏi (không tự quyết)

Ngoài 4 trường hợp này, Muse tự làm, không hỏi:

1. Cần quyền của user: đăng nhập, thanh toán, đăng bài hoặc thao tác thật
   lên tài khoản của user.
2. Kẹt quá 3 vòng tự sửa ở 1 task.
3. Quyết định làm đổi phạm vi, tốn tiền, hoặc mâu thuẫn với spec đã chốt.
4. Thông tin mới mâu thuẫn với quyết định cũ của user.

## 9. Giai đoạn 4 — Hoàn thiện theo chặng

- Sau mỗi gói duyệt, lặp lại Giai đoạn 2 → 3 cho chặng tiếp theo, cho tới
  khi hết plan.
- Thay đổi phạm vi giữa chừng: chỉ khi user yêu cầu; ghi vào changelog của
  `PLAN.md` kèm lý do và ngày đổi.

## 10. Giai đoạn 5 — Bàn giao và lưu trữ

1. Tài liệu CHỐT vào `project/` trên GitHub (theo quy tắc đã chốt 25/10:
   mỗi project là 1 folder con, tài liệu của project nằm trong folder đó).
2. Media (video, ảnh gốc, file nặng) lên Google Drive, rồi dán link Drive
   vào tài liệu dự án trên GitHub. Không nhúng file nặng vào HTML.
3. Bản nháp ở lại workspace/chat, không đưa vào `project/`.
4. Ghi `MEMORY.md`: quyết định đã chốt + link tài liệu, để lần sau không
   hỏi lại.
5. Đóng task/goal khi user xác nhận xong.

## 11. Mẫu PLAN.md (copy dùng cho mọi project)

```markdown
# PLAN — [tên project]
Spec: [link SPEC.md] | Ngày chốt plan: [ngày]

## Chặng 1 — [tên chặng]
- [ ] T1 — [mô tả]. Đầu ra: [file/link/demo].
  Xong khi: [tiêu chí đo được]. Phụ thuộc: [không/T0].
- [ ] T2 — ...

## Changelog
- [ngày] [thay đổi gì, vì sao]
```

## 12. Mẫu gói duyệt (Muse gửi user khi xong 1 chặng)

```markdown
Chặng [X] xong. Demo: [link/file].
Đã kiểm chứng: [check gì — số liệu].
Còn chưa check được: [cái gì — vì sao].
Quyết định cần bạn:
1. [quyết định] — khuyên chọn [A] vì [lý do]. Mặc định nếu bạn không chọn: [A].
2. [quyết định] — khuyên chọn [B] vì [lý do]. Mặc định: [B].
Bạn chỉ cần trả lời: "duyệt 1, đổi 2 sang ..."
```

## 13. Ví dụ áp cho dự án Munger (đã đi được nửa đường)

- Spec đã chốt: thư viện đủ ~223 mô hình/12 môn + flagship Model Stacks,
  song ngữ Anh–Việt.
- Đã xong: dataset 223/223, đã được user duyệt 25/10.
- Còn lại chạy đúng quy trình này:
  1. Plan chặng web (trang mô hình, case stack, tra cứu, lab, flashcard)
     + tiêu chí xong cho từng trang.
  2. Vòng lặp từng task, tự kiểm chứng 3 lớp, tự sửa tới khi đạt.
  3. Gói duyệt: demo layout (lấy bản khuyên chọn mạnh nhất trong 3 bản
     A/B/C) + 2 quyết định: (1) duyệt nội dung mẫu, (2) duyệt layout.
  4. Dựng full, bàn giao vào `project/mental-models-munger/`.
```

---

## Chi phí của quy trình (nói trước để khỏi bất ngờ)

- Quy trình này NẶNG: nhiều bước kiểm chứng, nhiều lần tự sửa, tốn thời gian
  và token gấp vài lần làm nhanh. Đó là cái giá của chất lượng.
- Vì vậy chỉ dùng cho project (Muse tự nhận diện theo Mục 1). Việc lẻ tẻ
  hằng ngày vẫn làm nhanh như cũ, không áp quy trình này.
