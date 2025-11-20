def in_bang_cuu_chuong(a, b):
    if a > b:
        n = a
    else:
        n = b
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
in_bang_cuu_chuong(a, b)
