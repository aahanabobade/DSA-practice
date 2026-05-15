# Count and Say
# Difficulty: Medium
# Runtime: 7 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/count-and-say/

        for j in range(n-1):
            count= 1
            ans = ""
            for i in range (len(s)):
                if i+1< len(s) and s[i]==s[i+1]:
                    count+=1
                else:
                    ans+=str(count)+s[i]
        """
        s = "1"
        :type n: int
        :rtype: str
        """
    def countAndSay(self, n):
class Solution(object):
