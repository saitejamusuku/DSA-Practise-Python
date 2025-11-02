def maxMinFreq(arr,n):
    mp ={}
    maxele = 0
    maxfr=0
    minele = 0
    minfr=n
    for i in range(n):
        if arr[i] in mp:
            mp[arr[i]] +=1
        else:
            mp[arr[i]] = 1
    for x in mp:
        if mp[x] > maxfr:
            maxfr=mp[x]
            maxele = x
        if mp[x] < minfr:
            minfr = mp[x]
            minele = x
    print(f"Max Freq ele is {maxele} freq is {maxfr}.")
    print(f"Min Freq ele is {minele} freq is {minfr}.")

    for x in mp:
        print(x,mp[x])
                     

lis = list(map(int,input("Enter all numbers: ").split()))

maxMinFreq(lis,len(lis))
