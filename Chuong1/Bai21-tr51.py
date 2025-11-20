n = int(input("Nhập số nguyên dương n: "))

if n < 2:
    print(n, "không phải là số nguyên tố.")
else:
    kt = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            kt = False
            break
    if kt:
        print(n, "là số nguyên tố.")
    else:
        print(n, "không phải là số nguyên tố.")