import math

print("Giải phương trình bậc 2: ax^2 + bx + c = 0")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a == 0:
    if b == 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình có 1 nghiệm x = ", -c / b)

delta = b ** 2 - 4 *(a * c)
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có 1 nghiệm kép x = ", -b / (2 * a))
else:
    print("Phương trình có 2 nghiệm")
    print("x1 = ", int((-b - math.sqrt(delta)) / (2 * a)))
    print("x2 = ", int((-b + math.sqrt(delta)) / (2 * a)))