chuoi = input("Nhập vào một chuỗi: ")
tong = 0
for i in chuoi:
    if i.isdigit():
        tong += int(i)
print("Tổng các chữ số trong chuỗi là: ",tong)