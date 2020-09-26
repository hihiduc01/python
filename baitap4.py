a = int(input("Nhập a:"))
b = int(input("Nhập b:"))
c = int(input("Nhập c:"))
if(a<b+c and b<a+c and c<a+b):
    if(c*c==a*a+b*b)or(b*b==c*c+a*a)or(a*a==b*b+c*c):
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Đây không phải là tam giác")
