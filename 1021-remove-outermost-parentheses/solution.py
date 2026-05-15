# Remove Outermost Parentheses
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result  = []
        balance = 0

        for i in s:
            if i == "(":
                if balance >0:
                    result.append(i)
                balance+=1

            else:
                balance-=1 
                if balance> 0:
                    result.append(i)
        
        return "".join(result)

        
