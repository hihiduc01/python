n = int(input("Nhập n:"))
sum = 0
for i in range(n+1):
    if(i<n and i == 17):
        continue
    sum += i 
print(f"Tổng là {sum}")