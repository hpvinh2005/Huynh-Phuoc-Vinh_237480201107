def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_trong_list(L, a):
    result = []
    for x in L:
        if la_nguyen_to(x):
            result.append(x)
            if len(result) == a:
                break
    return result

L = list(map(int, input("Nhập list số nguyên: ").split()))
a = int(input("Nhập a: "))
print("List số nguyên tố:", so_nguyen_to_trong_list(L, a))
