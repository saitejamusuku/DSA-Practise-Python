def numbers(n):
    if n<=0:
        return
    print(n, end=" ")
    numbers(n-1)

n = int(input("Enter number: "))
numbers(n)