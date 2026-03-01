#bruteforce

def left_shift(arr, d):
    n = len(arr)
    if n == 0:
        return arr
    
    d = d % n
    
    temp = arr[:d]
    
    for i in range(d, n):
        arr[i-d] = arr[i]
    
    for i in range(n-d, n):
        arr[i] = temp[i-(n-d)]
    
    return arr

def left_shift_d(arr, d):
    n = len(arr)
    d = d % n
    return arr[d:] + arr[:d]

print("Enter the digits:")
lis = list(map(int,input().split(" ")))
print("Enter the D value:")
n = int(input())

# print(left_shift(lis,n))
print(left_shift(lis,n))
