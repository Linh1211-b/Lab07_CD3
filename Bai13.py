import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. XẾP HẠNG TRONG TỪNG LỚP (Bài 13) ==================
print("="*75)
print("=== BÀI 13: XẾP HẠNG SINH VIÊN TRONG TỪNG LỚP ===")
print("="*75)

# Tạo cột xếp hạng theo từng lớp
df["XepHangTrongLop"] = df.groupby("Lop")["DiemTB"].rank(
    ascending=False,      # Điểm cao hơn xếp hạng cao hơn (1 là cao nhất)
    method="dense"        # Xếp hạng liền kề (không bị nhảy số)
)

# Chuyển kiểu xếp hạng thành số nguyên
df["XepHangTrongLop"] = df["XepHangTrongLop"].astype(int)

# Hiển thị kết quả theo yêu cầu
print(df[["HoTen", "Lop", "DiemTB", "XepHangTrongLop"]]
      .sort_values(["Lop", "XepHangTrongLop"]))

# ================== PHIÊN BẢN ĐẸP HƠN (Khuyến nghị) ==================
print("\n" + "="*75)
print("BẢNG XẾP HẠNG ĐẸP HƠN THEO TỪNG LỚP:")
print("="*75)

# Nhóm và hiển thị rõ ràng từng lớp
for lop in sorted(df["Lop"].unique()):
    print(f"\n→ Lớp {lop}:")
    lop_data = df[df["Lop"] == lop].copy()
    lop_data = lop_data.sort_values("XepHangTrongLop")
    print(lop_data[["HoTen", "DiemTB", "XepHangTrongLop"]].to_string(index=False))