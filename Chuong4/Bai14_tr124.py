L = []
while True:
    try:
        n = int(input("hập số lượng phần tử: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")

for i in range(n):
    while True:
        try:
            x = int(input(f"Nhập phần tử thứ {i + 1}: "))
            L.append(x)
            break
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

vi_tri = -1
for i in range(1, len(L) - 1):
    if L[i] == L[i-1] * L[i+1]:
        vi_tri = i + 1
        break

print("Vị trí tìm được là:", vi_tri)
