# Remove K Digits
# Difficulty: Medium
# Runtime: 35 ms
# Memory: 13.3 MB
# https://leetcode.com/problems/remove-k-digits/

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack = []

        for i in num:
            while k >0 and stack and stack[-1]>i:
                stack.pop()
                k -=1
            stack.append(i)
        
        while k >0:
            stack.pop()
            k-=1
        
        result = "".join(stack).lstrip("0")

        return result if result else "0"
