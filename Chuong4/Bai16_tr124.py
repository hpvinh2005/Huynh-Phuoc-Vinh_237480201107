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
            x = int(input(f"Nhập phần tử thứ {i + 1}: "))
            L.append(x)
            break
        except ValueError:
            print("Nhập số nguyên hợp lệ!")

L.sort()
print("List sau khi sắp xếp:", L)
