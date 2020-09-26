n = int(input("Nhập n nguyên dương: "))
x = float(input("Nhập x số thực bất kì: "))
s=0
it=1
for i in range (1,n+1):
    it = it *x
    s =s +it
print("S1: "+str(s+1))  
s2 = 0
for i in range(1,n+1):
    if i == n+1:
        s2 = (-1)**i*(x**i)
    else:
        if i%2==0:
            s2+= x**i
        else:
            s2-= x**i
print("S2 = ", 1+s2)

def GiaiThua(a):
    Giai_thua = 1
    if  (a == 0 or a == 1):
        return Giai_thua
    else:
        for i in range (2, n+1):
            Giai_thua = Giai_thua*i
        return Giai_thua
s3 = 0
for i in range(1,n+1):
    if i == n:
         s3+= (x**(i)) / (GiaiThua(i))
    else:
        s3+= x/GiaiThua(i)
print("s3 = ", s3+1)