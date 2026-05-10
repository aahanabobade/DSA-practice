# Minimum Size Subarray Sum
# Difficulty: Medium
# Runtime: 15 ms
# Memory: 20 MB
# https://leetcode.com/problems/minimum-size-subarray-sum/

        j = 0
        total = 0
        ans = float('inf')
        
        for i in range(n):
            total+=nums[i]

        n = len(nums)
        """
        :rtype: int
        :type target: int
        :type nums: List[int]
        """
    def minSubArrayLen(self, target, nums):
class Solution(object):
