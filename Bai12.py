import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. PHÂN NHÓM ĐIỂM HỌC LỰC (Bài 12) ==================
print("="*75)
print("=== BÀI 12: PHÂN NHÓM ĐIỂM HỌC LỰC VÀ THỐNG KÊ THEO LỚP ===")
print("="*75)

# Định nghĩa khoảng điểm và nhãn
bins = [0, 5, 7, 8.5, 10]
labels = ["<5", "5-6.9", "7-8.4", ">=8.5"]

# Tạo cột NhomDiem
df["NhomDiem"] = pd.cut(df["DiemTB"],
                        bins=bins,
                        labels=labels,
                        right=False)   # right=False nghĩa là [a, b)

print("Phân nhóm điểm của từng sinh viên:")
print(df[["MaSV", "HoTen", "DiemTB", "NhomDiem"]])

# ================== 4. THỐNG KÊ SỐ LƯỢNG THEO LỚP VÀ NHÓM ĐIỂM ==================
print("\nBẢNG THỐNG KÊ SỐ LƯỢNG SINH VIÊN THEO LỚP VÀ NHÓM ĐIỂM:")
print("-" * 75)

bang_thongke = pd.crosstab(df["Lop"], df["NhomDiem"])

# Thêm cột Tổng
bang_thongke['Tổng'] = bang_thongke.sum(axis=1)

print(bang_thongke)

# Phiên bản đẹp hơn với thứ tự nhóm điểm rõ ràng
print("\nBẢNG THỐNG KÊ ĐẸP HƠN (sắp xếp nhóm điểm):")
print(pd.crosstab(df["Lop"], df["NhomDiem"], margins=True, margins_name="Tổng"))