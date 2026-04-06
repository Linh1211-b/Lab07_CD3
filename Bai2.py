import pandas as pd
data = {
    'MaSV': ['SV001', 'SV002', 'SV003', 'SV004', 'SV005'],
    'HoTen': ['Nguyễn Văn A', 'Trần Thị B', 'Lê Văn C', 'Phạm Thị D', 'Hoàng Văn E'],
    'DiemQT': [8.0, 7.5, 9.0, 6.0, 8.5],
    'DiemGK': [7.5, 7.0, 9.5, 6.5, 8.0],
    'DiemCK': [8.0, 8.0, 9.0, 6.5, 9.0]
}

df = pd.DataFrame(data)
# ================== TÍNH ĐIỂM TRUNG BÌNH ==================
df["DiemTB"] = 0.2 * df["DiemQT"] + 0.3 * df["DiemGK"] + 0.5 * df["DiemCK"]

# Làm tròn 2 chữ số thập phân (rất nên làm)
df["DiemTB"] = df["DiemTB"].round(2)

# Hiển thị kết quả
print("=== ĐIỂM TRUNG BÌNH HỌC PHẦN ===")
print(df[["MaSV", "HoTen", "DiemQT", "DiemGK", "DiemCK", "DiemTB"]])

# Nếu chỉ muốn hiển thị 3 cột như yêu cầu bài:
print("\nKết quả yêu cầu bài:")
print(df[["MaSV", "HoTen", "DiemTB"]].head())