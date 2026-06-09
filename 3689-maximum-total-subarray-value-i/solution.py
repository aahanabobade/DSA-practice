# Maximum Total Subarray Value I
# Difficulty: Medium
# Runtime: 26 ms
# Memory: 16.3 MB
# https://leetcode.com/problems/maximum-total-subarray-value-i/

class Solution(object):
    def maxTotalValue(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return k * (max(nums) - min(nums))
        
