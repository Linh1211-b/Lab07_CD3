import pandas as pd

df = pd.read_csv('diem_sinhvien.csv')

print("✅ Đã đọc file diem_sinhvien.csv thành công!\n")

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

print("="*50)
print("=== THỐNG KÊ MÔ TẢ ĐIỂM TRUNG BÌNH (Bài 4) ===")
print("="*50)

print(f"Trung bình      : {df['DiemTB'].mean():.2f}")
print(f"Lớn nhất        : {df['DiemTB'].max():.2f}")
print(f"Nhỏ nhất        : {df['DiemTB'].min():.2f}")
print(f"Độ lệch chuẩn   : {df['DiemTB'].std():.2f}")

# ================== HIỂN THỊ BẢNG TÓM TẮT ==================
print("\nBảng chi tiết DiemTB và Xếp loại:")
print(df[["MaSV", "HoTen", "DiemTB", "XepLoai"]])