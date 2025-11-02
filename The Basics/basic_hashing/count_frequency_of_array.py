def freq(arr,n):
    mp ={}
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x,mp[x])

lis = list(map(int,input("Enter all numbers: ").split()))

freq(lis,len(lis))
