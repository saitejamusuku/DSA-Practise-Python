def numbers(n,sum):
    if n<=0:
        return sum
    return numbers(n-1, sum+n)

n = int(input("Enter number: "))
sum=0
print(numbers(n,sum))