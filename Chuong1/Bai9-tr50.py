so_tien = int(input("Nhập số tiền: "))
menh_gia = [50000, 20000, 10000, 5000, 2000, 1000]

print("Phân tích số tờ tiền:")
for m in menh_gia:
    so_to = so_tien // m
    if so_to > 0:
        print(so_to, "tờ", m)
    so_tien = so_tien % m

if so_tien >= 0:
    print("Số tiền còn dư: ", so_tien)
