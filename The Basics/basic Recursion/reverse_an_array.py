
#Brute force
def reverselis(lis):
    revlis = []
    for i in range(len(lis),0,-1):
        revlis.append(i)
    return revlis

lis = list(map(int,input("Enter all element: ").split(" ")))
print(f"Original list: {lis}")
print(f"Reversed list: {reverselis(lis)}")