# Divide Two Integers
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/divide-two-integers/

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        d = abs(dividend)
        dv = abs(divisor)
        output = 0

        while d>=dv:
            temp = dv
            mul = 1

            while d>=temp:
                d-=temp
                output+=mul
                mul+=mul
                temp+=temp
    
        if (dividend < 0 and divisor>=0) or (divisor<0 and dividend >=0):
            output = -output
        
        return min(2147483647, max(-2147483648,output))