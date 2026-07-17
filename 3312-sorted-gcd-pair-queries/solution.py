# Sorted GCD Pair Queries
# Difficulty: Hard
# Runtime: 813 ms
# Memory: 34.2 MB
# https://leetcode.com/problems/sorted-gcd-pair-queries/

        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
from bisect import bisect_right

class Solution(object):
    def gcdValues(self, nums, queries):
