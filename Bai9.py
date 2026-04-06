import pandas as pd

# ================== 1. ĐỌC DỮ LIỆU TỪ FILE ==================
df = pd.read_csv('diem_sinhvien.csv')

# ================== 2. TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemGK"] = df["DiemThi"]      # Tạm gán vì file không có DiemGK
df["DiemCK"] = df["DiemThi"]

df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]
df["DiemTB"] = df["DiemTB"].round(2)

# ================== 3. TẠO CỘT XẾP LOẠI (tùy chọn nhưng nên có) ==================
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

# ================== 4. GROUPBY NHIỀU CỘT - BÀI 9 ==================
print("="*80)
print("=== BÀI 9: GROUPBY THEO LỚP VÀ GIỚI TÍNH ===")
print("="*80)

baocao = df.groupby(["Lop", "GioiTinh"])["DiemTB"].agg(
    SoLuong="count",
    TrungBinh="mean",
    CaoNhat="max",
    ThapNhat="min"
)

# Làm tròn và đổi tên cột cho dễ đọc
baocao = baocao.round(2)
baocao = baocao.rename(columns={
    "SoLuong": "Số lượng SV",
    "TrungBinh": "Điểm trung bình",
    "CaoNhat": "Điểm cao nhất",
    "ThapNhat": "Điểm thấp nhất"
})

print(baocao)

# ================== PHIÊN BẢN ĐẸP HƠN (Khuyến nghị) ==================
print("\n" + "="*80)
print("KẾT QUẢ ĐẸP HƠN (sắp xếp theo điểm trung bình giảm dần):")
print("="*80)

# Reset index để hiển thị đẹp hơn
baocao_dep = baocao.reset_index()
print(baocao_dep.to_string(index=False))

# ================== BẢNG CHÉO XẾP LOẠI (tùy chọn bổ sung) ==================
print("\n" + "="*80)
print("SỐ LƯỢNG SINH VIÊN THEO XẾP LOẠI (Lớp & Giới tính):")
print("="*80)
print(pd.crosstab([df["Lop"], df["GioiTinh"]], df["XepLoai"]))