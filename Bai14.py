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

# ================== BÀI 14: Sinh viên có điểm cao nhất từng lớp ==================
print("="*70)
print("=== BÀI 14: SINH VIÊN CÓ ĐIỂM CAO NHẤT TỪNG LỚP ===")
print("="*70)

idx = df.groupby("Lop")["DiemTB"].idxmax()
sv_max = df.loc[idx, ["HoTen", "Lop", "DiemTB", "XepLoai"]].sort_values("Lop")
print(sv_max.to_string(index=False))