import pandas as pd
df = pd.read_csv('diem_sinhvien.csv')   # Đảm bảo file nằm cùng thư mục với file .py

print("✅ Đã đọc file diem_sinhvien.csv thành công!")
print("Các cột:", df.columns.tolist())
print("\n5 dòng đầu tiên:")
print(df.head())

df["DiemGK"] = df["DiemThi"]      # Tạm gán DiemGK = DiemThi
df["DiemCK"] = df["DiemThi"]      # DiemThi là điểm cuối kỳ

df["DiemTB"] = (0.2 * df["DiemQT"] +
                0.3 * df["DiemGK"] +
                0.5 * df["DiemCK"])

df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. XẾP LOẠI SINH VIÊN (Bài 3) ==================
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

# ================== 4. HIỂN THỊ KẾT QUẢ ==================
print("\n" + "="*60)
print("=== KẾT QUẢ TÍNH ĐIỂM TRUNG BÌNH VÀ XẾP LOẠI ===")
print("="*60)

print(df[["MaSV", "HoTen", "DiemQT", "DiemThi", "DiemTB", "XepLoai"]])

print("\nKết quả theo yêu cầu Bài 3:")
print(df[["HoTen", "DiemTB", "XepLoai"]])