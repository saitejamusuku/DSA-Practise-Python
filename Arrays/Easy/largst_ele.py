# Brute-force

def brute(lis):
    lis.sort()
    return lis[-1]
#optimal
def optimal(lis):
    max = lis[0]
    for i in range(1,len(lis)):
        if max < lis[i]:
            max = lis[i]
    return max
if __name__  == "__main__":
    lis = list(map(int,input().split()))
    print(optimal(lis))
