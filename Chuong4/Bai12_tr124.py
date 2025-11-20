while True:
    try:
        n = int(input("Nhập n: "))
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
    while True:
        try:
            a = int(input("Nhập a: "))
            b = int(input("Nhập b: "))
            if 0 <= a < b < len(lst):
                break
            else:
                print("a < b < len(lst). Vui lòng nhập lại!")
        except ValueError:
            print("nhập số bất kỳ!")
    min_value = min(lst[a+1 : b+1])
    print("list nhập là: ",lst)
    print(f"Số nhỏ nhất từ vị trí {a} đến {b} là: ", min_value)
    break