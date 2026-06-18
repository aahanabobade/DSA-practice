# Is Subsequence
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/is-subsequence/

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0  
        n = len(s)
        for j in t:
            if i < n and s[i] == j:
                i += 1

        return i == len(s)
