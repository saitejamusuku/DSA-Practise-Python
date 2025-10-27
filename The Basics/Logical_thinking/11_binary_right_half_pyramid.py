n = int(input("Enter the number:"))
for i in range(1,n+1):
    for j in range(i):
        if(j%2!=0):
            print(0, end= " ")
        else:
            print(1, end = " ")
    print()

# Enter the number:5
# 1 
# 1 0 
# 1 0 1 
# 1 0 1 0 
# 1 0 1 0 1