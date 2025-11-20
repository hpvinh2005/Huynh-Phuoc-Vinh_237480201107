def la_armstrong(a):
    str_a = str(a)
    so_chu_so = len(str_a)
    tong = sum(int(ch) ** so_chu_so for ch in str_a)
    return tong == a

a = int(input("Nhập số cần kiểm tra Armstrong: "))
if la_armstrong(a):
    print("Là số Armstrong" )
else:
    print("Không phải số Armstrong")