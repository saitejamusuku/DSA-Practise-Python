import math

n = int(input())
#brute-force
c = 0
while n > 0:
    c+=1
    n = n // 10
print(c)


#optimal-approach
c = int(math.log10(n) + 1)
print(c)

