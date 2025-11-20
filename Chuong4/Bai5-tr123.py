chuoi = input("Nhập vào một chuỗi: ")
in_hoa=0
in_thuong=0
so=0
for i in chuoi:
    if i.isupper():
        in_hoa += 1
    elif i.islower():
        in_thuong += 1
    elif i.isdigit():
        so += 1
print("Số ký tự in hoa: ",in_hoa)
print("Số ký tự in thuong: ",in_thuong)
print("Số ký tự số: ",so)