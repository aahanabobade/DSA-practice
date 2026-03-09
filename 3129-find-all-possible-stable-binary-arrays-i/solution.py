# Find All Possible Stable Binary Arrays I
# Difficulty: Medium
# Runtime: 6050 ms
# Memory: 19.1 MB
# https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/

        dp = [[[0]*2 for _ in range(one+1)] for __ in range(zero+1)]
        """
        MOD = 10**9 + 7
        
        :type limit: int
        :rtype: int
        """
        :type zero: int
        :type one: int
class Solution(object):
    def numberOfStableArrays(self, zero, one, limit):
