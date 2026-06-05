# Length of Last Word
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        n = len(s)
        for i in range(n-1,-1,-1):
            if s[i]==" " and count == 0:
                continue
            if s[i]!= " ":
                count +=1
            elif count >0:
                break
        
        return count
        
        #real life application : auto complete search