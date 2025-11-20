def tim_vi_tri_k(lst, k):
    try:
        return lst.index(k)+1
    except ValueError:
        return -1

if __name__ == "__main__":
    while True:
        try:
            n = int(input("Nhập n: "))
            if(n>0):
                break
            else:
                print("Vui lòng nhập số nguyên dương")
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
    while True:
        try:
            k = int(input("Nhập số nguyên k: "))
            break
        except ValueError:
            print("nhập phần tử tìm vi!")

    pos = tim_vi_tri_k(lst,k)
    print(f"Vi trí phần tử đầu tiên = {k} là: {pos}")
