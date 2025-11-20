def vi_tri_max(lst):
    max_value = max(lst)
    return lst.index(max_value)+1

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
                x=int(input(f"Nhập phần tử thứ {i+1}: "))
                lst.append(x)
                break
            except ValueError:
                print("Vui lòng nhập số nguyên hợp lệ!")
print("Danh sách vừa nhập: ", lst)
print("Vị trí giá trị lớn nhất:", vi_tri_max(lst))
