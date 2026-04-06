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
print("=== BÀI 15: PHÂN TÍCH TỶ LỆ ĐỖ - TRƯỢT THEO TỪNG LỚP ===")
print("="*70)

df["KetQua"] = np.where(df["DiemTB"] >= 4.0, "Đỗ", "Trượt")

so_luong = pd.crosstab(df["Lop"], df["KetQua"], margins=True, margins_name="Tổng")
print("Số lượng Đỗ / Trượt theo lớp:")
print(so_luong)

ty_le = pd.crosstab(df["Lop"], df["KetQua"], normalize="index") * 100
print("\nTỷ lệ (%) Đỗ / Trượt theo lớp:")
print(ty_le.round(2))