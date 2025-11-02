def insertion(arr,n):
    for i in range(n-1):
        for j in range(i+1,0,-1):
            if arr[j] < arr[j-1]:
                arr[j],arr[j-1] = arr[j-1],arr[j]
            
    return arr

lis = list(map(int,input().split()))
print(insertion(lis,len(lis)))