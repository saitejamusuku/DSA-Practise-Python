n1 = int(input("ENter n1 "))
n2 = int(input("Enter n2 "))
#Bruteforce
for i in range(1, min(n1,n2)//2 + 1):
    if n1 % i == 0 and n2 %i==0:
        gsd = i
print(gsd)