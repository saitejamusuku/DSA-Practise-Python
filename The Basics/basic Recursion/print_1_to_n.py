def numbers(count,n):
    if count > n:
        return
    print(count, end=" ")
    numbers(count+1,n)

n = int(input("Enter number: "))
numbers(1,n)