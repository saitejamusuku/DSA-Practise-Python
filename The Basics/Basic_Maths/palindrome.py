n = int(input())
cpy = n
sum=0
while(n > 0):
    r = n%10
    sum = sum*10 + r
    n = n //10

if(sum == cpy):
    print("palindrome")
else:
    print("Not a Palindrome")

#CPP-Code

# class Solution {
# public:
#     bool isPalindrome(int x) {
#         if (x < 0) return false;
        
#         long rev = 0;
#         int cpy = x;

#         while (x != 0) {
#             int rem = x % 10;
#             rev = rev * 10 + rem;
#             x /= 10;

#             if (rev > INT_MAX) return false; 
#         }

#         return rev == cpy;
#     }
# };
