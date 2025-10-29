#Note: If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.


n = int(input())
sum=0
while(n > 0):
    r = n%10
    sum = sum*10 + r
    n = n //10
print(sum)