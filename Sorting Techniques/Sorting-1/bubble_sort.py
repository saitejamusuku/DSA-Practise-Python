def bubble(arr,n):
    for i in range(n):
        for j in range(0,n-i-1,1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr                

lis = list(map(int,input().split()))
print(bubble(lis,len(lis)))