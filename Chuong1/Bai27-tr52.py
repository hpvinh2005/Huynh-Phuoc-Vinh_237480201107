m = float(input("Nhập m: "))
S = 0
n = 0

while S <= m:
    n += 1
    S += 1 / n

print("Giá trị n nhỏ nhất sao cho tổng > m là:", n)
print("Tổng S =", S)