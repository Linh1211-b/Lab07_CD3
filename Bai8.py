import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. TẠO CỘT XẾP LOẠI (bắt buộc cho crosstab) ==================
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

# ================== 4. TỔNG HỢP THEO LỚP - BÀI 8 ==================
print("="*70)
print("=== BÀI 8: TỔNG HỢP NHIỀU CHỈ TIÊU THEO TỪNG LỚP ===")
print("="*70)

tonghop = df.groupby("Lop")["DiemTB"].agg(["count", "mean", "max", "min"])

# Đổi tên cột cho dễ đọc
tonghop.columns = ["Số lượng SV", "Điểm TB", "Điểm cao nhất", "Điểm thấp nhất"]
tonghop = tonghop.round(2)

print(tonghop)

# ================== PHIÊN BẢN ĐẸP HƠN ==================
print("\n" + "="*70)
print("KẾT QUẢ ĐẸP HƠN (sắp xếp theo điểm TB giảm dần):")
print("="*70)

tonghop_dep = tonghop.sort_values(by="Điểm TB", ascending=False)
print(tonghop_dep)

# ================== THỐNG KÊ XẾP LOẠI THEO LỚP ==================
print("\n" + "="*70)
print("SỐ LƯỢNG SINH VIÊN THEO XẾP LOẠI TRONG TỪNG LỚP:")
print("="*70)
print(pd.crosstab(df["Lop"], df["XepLoai"]))