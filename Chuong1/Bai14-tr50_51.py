van = float(input("Nhập điểm môn Văn: "))
toan = float(input("Nhập điểm môn Toán: "))
anh = float(input("Nhập điểm môn Tiếng Anh: "))

dtb = (van + toan + anh) / 3
print("Điểm trung bình =", round(dtb, 2))

if dtb >= 8.5 and toan >= 9 and toan > van and toan > anh:
    print("Học sinh đậu chuyên Toán.")
elif dtb >= 8.5 and van >= 9 and van > anh:
    print("Học sinh đậu chuyên Văn.")
elif dtb >= 8.5 and anh >= 8.0:
    print("Học sinh đậu chuyên Tiếng Anh.")
else:
    print("Học sinh không đậu chuyên nào.")