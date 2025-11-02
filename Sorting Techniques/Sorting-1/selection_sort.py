def selection(arr,n):
    for i in range(n):
        for j in range(i,n):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    for i in arr:
        print(i,end=" ")


lis = list(map(int,input().split()))
selection(lis,len(lis))
