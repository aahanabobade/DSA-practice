# Reverse Integer
# Difficulty: Medium
# Runtime: 25 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 -1
        INT_MIN = - 2**31

        result  = 0

        sign = -1 if x<0 else 1
        x = abs(x)

        while x!=0:
            digit = x%10
            x//=10

            if result >(INT_MAX-digit)//10:
                return 0

            result = result *10 + digit 

        return sign*result

        
        