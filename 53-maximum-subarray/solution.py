# Maximum Subarray
# Difficulty: Medium
# Runtime: 106 ms
# Memory: 21.1 MB
# https://leetcode.com/problems/maximum-subarray/

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxx = nums[0]
        for i in range(1,n):
        curr = nums[0]

            curr = max(nums[i],curr+nums[i])
            maxx = max(maxx, curr)

        return maxx    
        
