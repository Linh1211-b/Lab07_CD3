import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH & XẾP LOẠI (để code chạy ổn định) ==================
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

# ================== 3. TẠO BẢNG CHÉO CROSSTAB - BÀI 11 ==================
print("="*65)
print("=== BÀI 11: BẢNG CHÉO THỐNG KÊ SỐ LƯỢNG SINH VIÊN THEO LỚP VÀ GIỚI TÍNH ===")
print("="*65)

bang_cheo = pd.crosstab(df["Lop"], df["GioiTinh"])

# Đổi tên cột cho dễ đọc hơn
bang_cheo.columns.name = "Giới tính"
bang_cheo.index.name = "Lớp"

print(bang_cheo)

# ================== PHIÊN BẢN ĐẸP HƠN (Khuyến nghị) ==================
print("\n" + "="*65)
print("BẢNG CHÉO ĐẸP HƠN (có thêm tổng cộng):")
print("="*65)

# Thêm cột Tổng và dòng Tổng
bang_cheo['Tổng'] = bang_cheo.sum(axis=1)
bang_cheo.loc['Tổng'] = bang_cheo.sum()

print(bang_cheo)

# Thêm phiên bản với phần trăm
print("\nBẢNG CHÉO VỚI TỶ LỆ (%):")
print((pd.crosstab(df["Lop"], df["GioiTinh"], normalize='index') * 100).round(1))