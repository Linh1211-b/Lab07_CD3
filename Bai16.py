import pandas as pd
import numpy as np

# ================== 1. ĐỌC DỮ LIỆU ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH & XẾP LOẠI ==================
df["DiemGK"] = df["DiemThi"]
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

def xep_loai(diem):
    if diem >= 8.5:
        return "A"
    elif diem >= 7.0:
        return "B"
    elif diem >= 5.5:
        return "C"
    elif diem >= 4.0:
        return "D"
    else:
        return "F"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print("Dữ liệu đã xử lý xong!\n")
print("\n" + "="*70)
print("=== BÀI 16: BÁO CÁO TỔNG HỢP THEO LỚP (thay cho Chuyên ngành) ===")
print("="*70)

# Vì file không có cột ChuyenNganh, dùng cột Lop thay thế
tong_hop = df.groupby("Lop").agg(
    SoSinhVien=("MaSV", "count"),
    DiemTrungBinh=("DiemTB", "mean")
).round(2)

# Tính số và tỷ lệ đạt A hoặc B
dat_ab = df[df["XepLoai"].isin(["A", "B"])].groupby("Lop")["MaSV"].count()
tong_hop["SoDatAB"] = dat_ab
tong_hop["SoDatAB"] = tong_hop["SoDatAB"].fillna(0).astype(int)

tong_hop["TyLeDatAB"] = (tong_hop["SoDatAB"] / tong_hop["SoSinhVien"] * 100).round(2)

print(tong_hop)
