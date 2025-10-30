def printname(name,n):
    if(n<=0):
        return
    else:
        print(name)
    return printname(name,n-1)

n = input("Enter your name: ")
printname(n, 5)
