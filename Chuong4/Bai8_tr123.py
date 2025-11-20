import string
mat_khau = input("Nhập mật khẩu: ")

co_in_hoa = any(c.isupper() for c in mat_khau)
co_in_thuong = any(c.islower() for c in mat_khau)
co_so = any(c.isdigit() for c in mat_khau)
co_ky_tu_dac_biet = any(c in string.punctuation for c in mat_khau)
doi_dai_hop_le = len(mat_khau)>6

if co_in_hoa and co_in_thuong and co_so and co_ky_tu_dac_biet and doi_dai_hop_le:
    print("Mật khẩu mạnh")
else:
    print("Mật khẩu yếu")