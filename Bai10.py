import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH & XẾP LOẠI ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
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

# ================== 3. TẠO BẢNG PIVOT TABLE - BÀI 10 ==================
print("="*70)
print("=== BÀI 10: BẢNG THỐNG KÊ SỐ LƯỢNG SINH VIÊN THEO LỚP VÀ XẾP LOẠI ===")
print("="*70)

pivot1 = pd.pivot_table(
    df,
    index="Lop",           # Hàng là Lớp
    columns="XepLoai",     # Cột là Xếp loại
    values="MaSV",         # Đếm theo mã sinh viên
    aggfunc="count",       # Đếm số lượng
    fill_value=0           # Nếu không có thì điền 0
)

# Đổi tên cột cho dễ nhìn (tùy chọn)
pivot1.columns.name = "Xếp loại"

print(pivot1)

# ================== PHIÊN BẢN ĐẸP HƠN (Khuyến nghị) ==================
print("\n" + "="*70)
print("BẢNG THỐNG KÊ ĐẸP HƠN:")
print("="*70)

# Sắp xếp các cột theo thứ tự logic: A → B → C → D → F
order = ['A', 'B', 'C', 'D', 'F']
pivot1 = pivot1.reindex(columns=order, fill_value=0)

print(pivot1)

# Thêm tổng cộng (Total)
pivot1.loc['Tổng'] = pivot1.sum()
print("\nVới dòng Tổng:")
print(pivot1)