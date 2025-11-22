import QuanlySV

def menu():
    print("\n===== Chuong Trinh Quan Ly Sinh Vien =====")
    print("1. Them sinh vien")
    print("2. Xoa sinh vien")
    print("3. Sua sinh vien")
    print("4. Xem danh sach sinh vien")
    print("5. Thoat")

while True:
    menu()
    chon = input("Nhap lua chon: ")

    if chon == "1":
        ma = input("Nhap ma sinh vien: ")
        ten = input("Nhap ten sinh vien: ")
        QuanlySV.add_student(ma, ten)
        print(">> Them thanh cong!")

    elif chon == "2":
        ma = input("Nhap ma sinh vien can xoa: ")
        if QuanlySV.remove_student(ma):
            print(">> Da xoa!")
        else:
            print(">> Khong tim thay sinh vien!")

    elif chon == "3":
        ma = input("Nhap ma sinh vien can sua: ")
        ten_moi = input("Nhap ten moi: ")
        if QuanlySV.update_student(ma, ten_moi):
            print(">> Sua thanh cong!")
        else:
            print(">> Khong tim thay sinh vien!")

    elif chon == "4":
        ds = QuanlySV.get_students()
        print("\n===== Danh Sach Sinh Vien =====")
        if len(ds) == 0:
            print("Danh sach rong!")
        else:
            for sv in ds:
                print(f"Ma: {sv['ma']} - Ten: {sv['ten']}")

    elif chon == "5":
        print("Thoat chuong trinh...")
        break

    else:
        print(">> Lua chon khong hop le!")
