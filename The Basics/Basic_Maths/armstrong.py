n = int(input())
import math
cpy =n
c = int(math.log10(n)) + 1
sum=0

while( n > 0):
    rem = n%10
    sum+=rem**c
    n = n//10

if(cpy==sum):
    print("Armstrong")
else:
    print("Not an Armstrong")
