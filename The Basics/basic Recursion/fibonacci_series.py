n = int(input("Enter the number: "))

def fibo(n):
    if n==0:
        print(0)
    if n==1:
        print(1)
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(0,n-2,1):
        c = a+b
        a = b
        b = c
        print(c,end=" ")

fibo(n)