def la_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

a = int(input("Nhập số nguyên a: "))
if la_nguyen_to(a):
    print("Là số nguyên tố" )
else:
    print("Không phải số nguyên tố")