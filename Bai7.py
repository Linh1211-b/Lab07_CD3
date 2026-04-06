import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

print("✅ Đã đọc file diem_sinhvien.csv thành công!\n")

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có cột DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. GROUPBY THEO GIỚI TÍNH (Bài 7) ==================
print("="*60)
print("=== BÀI 7: ĐIỂM TRUNG BÌNH THEO GIỚI TÍNH ===")
print("="*60)

tb_theo_gt = df.groupby("GioiTinh")["DiemTB"].mean().round(2)

print(tb_theo_gt)

# ================== HIỂN THỊ ĐẸP HƠN (Khuyến nghị dùng) ==================
print("\n" + "="*60)
print("KẾT QUẢ ĐẸP HƠN:")
print("="*60)

ketqua = tb_theo_gt.reset_index()
ketqua.columns = ["Giới tính", "Điểm trung bình"]
print(ketqua.to_string(index=False))

# Thêm số lượng sinh viên và thống kê chi tiết
print("\nThống kê chi tiết theo Giới tính:")
print(df.groupby("GioiTinh").agg(
    So_luong=("MaSV", "count"),
    DiemTB_trung_binh=("DiemTB", "mean"),
    DiemTB_max=("DiemTB", "max"),
    DiemTB_min=("DiemTB", "min")
).round(2))