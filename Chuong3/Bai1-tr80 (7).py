def trung_binh_a_phan_tu(L, a):
    if a > len(L):
        return None
    return sum(L[:a]) / a

L = list(map(int, input("Nhập list số nguyên: ").split()))
a = int(input("Nhập số a: "))
print("Giá trị trung bình:", trung_binh_a_phan_tu(L, a))
