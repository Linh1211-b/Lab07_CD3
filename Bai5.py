import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH & XẾP LOẠI (bắt buộc) ==================
df["DiemGK"] = df["DiemThi"]   # Tạm gán vì file không có DiemGK
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

# ================== 3. THỐNG KÊ TẦN SUẤT (Bài 5) ==================
print("="*60)
print("=== BÀI 5: THỐNG KÊ TẦN SUẤT DỮ LIỆU ===")
print("="*60)

print("1. Số lượng sinh viên theo Giới tính:")
print(df["GioiTinh"].value_counts())
print("-" * 40)

print("\n2. Số lượng sinh viên theo Lớp:")
print(df["Lop"].value_counts())
print("-" * 40)

# Lưu ý: File của bạn KHÔNG có cột "ChuyenNganh"
# Nếu muốn thống kê theo chuyên ngành, ta có thể dùng cột "Lop" thay thế hoặc tạo mới
print("\n3. Số lượng sinh viên theo Lớp (thay cho Chuyên ngành):")
print(df["Lop"].value_counts())
print("-" * 40)

print("\n4. Số lượng sinh viên theo Xếp loại:")
print(df["XepLoai"].value_counts())
print("-" * 40)

# ================== THỐNG KÊ CHI TIẾT HƠN (tùy chọn - đẹp hơn) ==================
print("\n=== THỐNG KÊ CHI TIẾT ===")
print("Số lượng sinh viên theo Giới tính và Xếp loại:")
print(pd.crosstab(df["GioiTinh"], df["XepLoai"]))

print("\nSố lượng sinh viên theo Lớp và Xếp loại:")
print(pd.crosstab(df["Lop"], df["XepLoai"]))