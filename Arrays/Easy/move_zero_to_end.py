
#brute
def move_brute(arr):
    temp = [0]*len(arr)
    index=0
    for num in arr:
        if num!=0:
            temp[index] = num
            index+=1
    arr = temp
    return arr

#optimal
def move_optimal(arr):
    n = len(arr)
    j = -1
    
    for i in range(n):
        if arr[i] == 0:
            j = i
            break
    
    if j == -1:
        return arr
    
    for i in range(j + 1, n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr
        

print("Enter the digits:")
lis = list(map(int,input().split(" ")))
print(move_optimal(lis))