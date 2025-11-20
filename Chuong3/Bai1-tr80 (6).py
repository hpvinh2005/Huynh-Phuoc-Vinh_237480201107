def chuoi_ngan_nhat(lst):
    return min(lst, key=len)
if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập n: "))
            break
        except ValueError:
            print("nhập số bất kỳ!")
    lst=[]
    for i in range(n):
        while True:
            try:
                x=input(f"Nhập phần tử thứ {i+1}: ")
                lst.append(x)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")

print("Chuỗi ngắn nhất là:", chuoi_ngan_nhat(lst))
