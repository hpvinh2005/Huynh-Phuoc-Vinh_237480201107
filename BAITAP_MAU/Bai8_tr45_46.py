a,b,c=eval(input('Nhap vao 3 so cach nhau boi dau phay: '))
if(a+b>c)and(b+c>a)and(a+c>b):
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('day la tma giac vuong')
    elif a==b==c:
        print('day la tam giac dieu')
    elif a==b or a==c or c==b:
        print('day la tam giac can')
    else:
        print('day la tam giac thuong')
else:
    print('day khong phai 3 canh cua tam giac')