students =[]

def add_student(ma,ten):
    students.append({"ma": ma,"ten": ten})
def remove_student(ma):
    for sv in students:
        if sv["ma"]==ma:
            students.remove(sv)
            return True
        return False
def update_student(ma,ten_moi):
    for sv in students:
        if sv["ma"]==ma:
            sv["ten"]=ten_moi
            return True
    return False

def get_students():
    return students