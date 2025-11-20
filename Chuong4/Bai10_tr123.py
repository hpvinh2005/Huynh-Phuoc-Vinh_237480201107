a = input("Nhập chuỗi a: ")
b = input("Nhập chuỗi b: ")
ket_qua = ""
i = 0
while i<len(a):
    if a[i:i+len(b)] == b:
        i += len(b)
    else:
        ket_qua += a[i]
        i += 1
print("Chuỗi sau khi xoá b khỏi a: ",ket_qua)