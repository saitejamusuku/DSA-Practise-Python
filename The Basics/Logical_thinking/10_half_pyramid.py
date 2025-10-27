n = int(input("Enter the number: "))

for i in range(2*n - 1):
    s = i
    if i > n: 
        s = 2*n - i

    for j in range(s-1):
        print("*",end="")
    print()

# Enter the number: 5

# *
# **
# ***
# ****
# ***
# **
# *