n = int(input("Enter the number: "))

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range( 2 * (n-1-i) - 1):
        print("*", end="")
    print()

# Enter the number: 5
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *