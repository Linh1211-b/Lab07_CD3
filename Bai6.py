import pandas as pd

df = pd.read_csv('diem_sinhvien.csv')

df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. GROUPBY THEO LỚP - Tính điểm trung bình từng lớp (Bài 6) ==================
print("="*55)
print("=== BÀI 6: ĐIỂM TRUNG BÌNH THEO TỪNG LỚP ===")
print("="*55)

tb_theo_lop = df.groupby("Lop")["DiemTB"].mean().round(2)

print(tb_theo_lop)

# ================== HIỂN THỊ ĐẸP HƠN (Khuyến nghị) ==================
print("\n" + "="*55)
print("KẾT QUẢ ĐẸP HƠN:")
print("="*55)

# Chuyển thành DataFrame để hiển thị đẹp
ketqua = tb_theo_lop.reset_index()
ketqua.columns = ["Lớp", "Điểm trung bình"]
print(ketqua.to_string(index=False))

# Thêm số lượng sinh viên mỗi lớp
print("\nThống kê chi tiết theo lớp:")
print(df.groupby("Lop").agg(
    So_luong=("MaSV", "count"),
    DiemTB_trung_binh=("DiemTB", "mean")
).round(2))