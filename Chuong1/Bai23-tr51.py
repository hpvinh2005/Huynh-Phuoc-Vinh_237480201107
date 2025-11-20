n = int(input("Nhập số nguyên dương n: "))
dem = 0
tam = n

while tam > 0:
    dem += 1
    tam //= 10

print("Số", n, "có", dem, "chữ số.")