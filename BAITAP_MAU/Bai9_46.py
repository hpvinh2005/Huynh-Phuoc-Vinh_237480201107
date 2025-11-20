a,b,c=eval(input('Nhap vao 3 so cach nhau boi dau phay: '))
if(a>b):
    if(a>c):
        if(b>c):
            print(c,b,a)
        else:
            print(b,c,a)
    else:
        print(b,a,c)
else:
    if(b>c):
        if(a>c):
            print(c,a,b)
        else:
            print(a,c,b)
    else:
        print(a,b,c)
