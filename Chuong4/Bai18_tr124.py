L = []
while True:
    try:
        n = int(input("Nhập số lượng phần tử: "))
        break
    except ValueError:
        print("Nhập số bất kỳ!")
for i in range(n):
    while True:
        try:
            x = int(input(f"Nhập phần tử thứ {i+1}: "))
            L.append(x)
            break
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

is_sorted = True
for i in range(len(L) - 1):
    if L[i] > L[i+1]:
        is_sorted = False
        break

print(is_sorted)
