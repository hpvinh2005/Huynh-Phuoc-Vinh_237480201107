n = int(input("Nhập vào số nguyên có 4 chữ số: "))

a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
tong = a + b + c + d
d = n % 10

print("Tổng các chữ số của", n, "là:", tong)