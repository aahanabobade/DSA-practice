# Maximum Subarray
# Difficulty: Medium
# Runtime: 105 ms
# Memory: 21.3 MB
# https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        cur = nums[0]
        maxx = nums[0]

        for i in range(1,n):
            cur= max(nums[i],cur+nums[i])
            maxx = max(cur, maxx)

        return maxx
