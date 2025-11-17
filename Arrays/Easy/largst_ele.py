# Brute-force

def brute(lis):
    lis.sort()
    return lis[-1]

if __name__  == "__main__":
    lis = list(map(int,input().split()))
    print(brute(lis))
