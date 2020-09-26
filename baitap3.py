sum =0
n = int(input("Nhập số dương n (1->1000): "))
while (n>999 or n <0):
    print("Nhập lại 1 số nguyên duong n (n<1000):", end=" ")
while (n > 0):
    sum += n%10
    n = int(n/10)

print(f"Kết quả : {sum}")