n = int(input("Nhập số nguyên dương n: "))
S = 0
k = 0

while S + (k + 1) < n:
    k += 1
    S += k

print("Giá trị k lớn nhất nhưng S(k) < n là:", k)
print("Tổng S(k) =", S)
