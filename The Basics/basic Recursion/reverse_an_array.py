#optimal
def reverse(lis):
    for i in range(0,len(lis)//2,1):
        lis[i], lis[len(lis)-1-i] = lis[len(lis)-1-i], lis[i]
    return lis

#Brute force
def reverselis(lis):
    revlis = []
    for i in range(len(lis),0,-1):
        revlis.append(i)
    return revlis

lis = list(map(int,input("Enter all element: ").split(" ")))
print(f"Original list: {lis}")

print(f"Reversed list: {reverse(lis)}")
print(f"Reversed list: {reverselis(lis)}")