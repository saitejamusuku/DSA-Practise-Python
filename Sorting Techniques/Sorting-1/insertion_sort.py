def insertion(arr,n):
    for i in range(1,n-1):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -=1
            
    return arr

lis = list(map(int,input().split()))
print(insertion(lis,len(lis)))