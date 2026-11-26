#!/usr/bin/env python3
"""Merge v2 (16 truong moi + anh_phu + video) vao data/breeds.json.
Doc: batches/v2-*.json (9 file, da duyet) + v2-sample.json (doi chieu 2 giong mau).
Quy tac:
- Giu nguyen toan bo truong v1, chi them truong moi; ten_vi lay theo v1.
- British Shorthair: can_nang -> "duc 4-8 kg, cai 3-5 kg" (Wikipedia, da kiem chung o mau v2).
- Cac de xuat lap cho trong/giai quyet mau thuan khac giu trong ghi_chu_chua_kiem_chung_v2, KHONG sua v1.
- Anh phu/video: file phai ton tai, co commons_url + license; khong trung anh #1.
Usage: python3 merge_v2.py  (exit != 0 neu co loi)
"""
import json, pathlib, sys

BASE = pathlib.Path("/home/hatch/workspace/giong-cho-meo")
V2_FILES = ["v2-DGAP.json", "v2-D1.json", "v2-D2.json", "v2-D3.json", "v2-D4.json",
            "v2-D5.json", "v2-D6.json", "v2-C1.json", "v2-C2.json"]
NEW16 = ["nguon_goc", "ngoai_hinh", "tinh_cach_chi_tiet", "than_thien_tre_em",
         "than_thien_vat_khac", "than_thien_nguoi_la", "muc_do_sua", "huan_luyen",
         "van_dong_phut_ngay", "cham_soc_long", "suc_khoe", "an_uong", "hop_voi_ai",
         "luu_y_viet_nam", "nguon_moi", "trang_thai_moi"]

def load_list(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    return d if isinstance(d, list) else d["giong"]

def main():
    errors, warns = [], []
    v1 = json.loads((BASE / "data" / "breeds.json").read_text(encoding="utf-8"))
    v1_by_id = {b["id"]: b for b in v1}
    print(f"v1: {len(v1)} giong")

    # --- load v2 ---
    v2 = {}
    for fn in V2_FILES:
        d = load_list(BASE / "batches" / fn)
        print(f"{fn}: {len(d)} giong")
        for x in d:
            if x["id"] in v2:
                errors.append(f"trung id v2 {x['id']} ({fn})")
            v2[x["id"]] = x

    # --- doi chieu mau v2 ---
    sample = json.loads((BASE / "v2-sample.json").read_text(encoding="utf-8"))["giong"]
    for s in sample:
        b = v2.get(s["id"])
        if not b:
            errors.append(f"mau {s['id']} khong co trong batch")
            continue
        for k in NEW16:
            if b.get(k) != s.get(k):
                warns.append(f"mau {s['id']}: truong {k} khac mau (lay ban batch)")

    # --- bao phu ---
    missing = set(v1_by_id) - set(v2)
    extra = set(v2) - set(v1_by_id)
    if missing: errors.append(f"thieu v2: {sorted(missing)}")
    if extra: errors.append(f"thua v2: {sorted(extra)}")
    print(f"v2: {len(v2)} id duy nhat; bao phu v1: {len(v1_by_id)-len(missing)}/{len(v1_by_id)}")

    # --- validate tung muc v2 ---
    n_photo_extra = 0
    n_video = 0
    for bid, x in v2.items():
        miss = [k for k in NEW16 if k not in x]
        if miss: errors.append(f"{bid}: thieu truong moi {miss}")
        if "anh_phu" not in x: errors.append(f"{bid}: thieu anh_phu")
        if "video" not in x: errors.append(f"{bid}: thieu video")
        main_file = v1_by_id.get(bid, {}).get("anh", {}).get("file") if v1_by_id.get(bid, {}).get("anh") else None
        for ph in x.get("anh_phu", []):
            n_photo_extra += 1
            f = BASE / ph["file"]
            if not f.exists(): errors.append(f"{bid}: anh phu khong ton tai {ph['file']}")
            elif f.stat().st_size < 3000: errors.append(f"{bid}: anh phu qua nho {ph['file']}")
            if not ph.get("license") or not ph.get("commons_url"):
                errors.append(f"{bid}: anh phu thieu license/commons_url {ph.get('file')}")
            if ph["file"] == main_file: errors.append(f"{bid}: anh phu trung anh #1 {ph['file']}")
        v = x.get("video")
        if v:
            n_video += 1
            f = BASE / v["file"]
            if not f.exists(): errors.append(f"{bid}: video khong ton tai {v['file']}")
            elif f.stat().st_size < 10000: errors.append(f"{bid}: video qua nho {v['file']}")
            if not v.get("license") or not v.get("commons_url"):
                errors.append(f"{bid}: video thieu license/commons_url")
    print(f"anh phu moi: {n_photo_extra} | video: {n_video}")

    if errors:
        print(f"LOI ({len(errors)}):")
        for e in errors[:60]: print(" -", e)
        sys.exit(1)
    for w in warns: print("CANH BAO:", w)

    # --- merge ---
    for b in v1:
        x = v2[b["id"]]
        for k in NEW16:
            b[k] = x[k]
        b["anh_phu"] = x.get("anh_phu", [])
        b["video"] = x.get("video")
        b["ghi_chu_chua_kiem_chung_v2"] = x.get("ghi_chu_chua_kiem_chung", "")
        # ten_vi: giu v1 (v2 co the chua ten tam da sua ve null o C1, nhung van uu tien v1)

    # British Shorthair: can nang da kiem chung (Wikipedia) theo mau v2
    bsh = v1_by_id["meo-british-shorthair"]
    bsh["can_nang"] = "đực 4–8 kg, cái 3–5 kg"
    note = bsh.get("ghi_chu_chua_kiem_chung", "")
    note = note.replace("Cân nặng chưa kiểm chứng. ", "").replace("cân nặng chưa kiểm chứng", "cân nặng đã kiểm chứng ở v2")
    bsh["ghi_chu_chua_kiem_chung"] = note
    print("British Shorthair can_nang ->", bsh["can_nang"])

    v1.sort(key=lambda x: (x["loai"], x["ten_en"].lower()))
    out = BASE / "data" / "breeds.json"
    out.write_text(json.dumps(v1, ensure_ascii=False, indent=1), encoding="utf-8")

    dogs = [x for x in v1 if x["loai"] == "cho"]
    cats = [x for x in v1 if x["loai"] == "meo"]
    with_photo = sum(1 for x in v1 if x.get("anh") or x.get("anh_phu"))
    total_photos = sum((1 if x.get("anh") else 0) + len(x.get("anh_phu", [])) for x in v1)
    no_photo = [x["id"] for x in v1 if not x.get("anh") and not x.get("anh_phu")]
    md = ["# Giống chó và mèo — dữ liệu master (v2)\n",
          f"- Tổng: **{len(v1)}** giống (chó {len(dogs)}, mèo {len(cats)}), có ảnh thật {with_photo}/{len(v1)}.\n",
          f"- Tổng ảnh thật: **{total_photos}** (ảnh chính + ảnh phụ 3–5/giống); video: **{n_video}** giống có video.\n",
          f"- Không có ảnh nào: {len(no_photo)} giống ({', '.join(no_photo) if no_photo else 'không có'}).\n",
          f"- Chưa kiểm chứng một phần (v1): {sum(1 for x in v1 if x['trang_thai'] != 'da-kiem-chung')} mục; v2: tất cả 458 mục đều chua-kiem-chung-phan (chủ yếu vì luu_y_viet_nam là suy luận, chưa có nguồn riêng về VN).\n",
          "- Nguồn: Wikipedia EN + FCI + AKC + CFA/TICA + PetMD/VCA; ảnh/video Wikimedia Commons (PD/CC), ghi license + tác giả từng file trong JSON.\n",
          "- File HTML: giong-cho-meo.html (cùng thư mục), ảnh/video tại photos/.\n"]
    (BASE / "data" / "breeds.md").write_text("\n".join(md), encoding="utf-8")
    print("OK ->", out, f"({out.stat().st_size} byte)")
    print("OK -> data/breeds.md")
    print(f"TONG KET: {len(v1)} giong | anh {total_photos} | video {n_video} | 0 anh: {len(no_photo)}")

if __name__ == "__main__":
    main()
