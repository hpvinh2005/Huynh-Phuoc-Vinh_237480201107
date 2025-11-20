def gia_tri_lon_thu_a(L, a):
    L_sorted = sorted(list(set(L)), reverse=True)
    if a <= len(L_sorted):
        return L_sorted[a-1]
    return None

L = list(map(int, input("Nhập list số nguyên: ").split()))
a = int(input("Nhập a: "))
print("Giá trị lớn thứ a là:", gia_tri_lon_thu_a(L, a))
