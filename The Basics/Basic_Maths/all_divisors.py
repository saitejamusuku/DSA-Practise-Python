n = int(input())
import math

lis = []

for i in range(1, n//2 + 1):
    if n % i == 0:
        lis.append(i)
lis.append(n)
print(lis)

