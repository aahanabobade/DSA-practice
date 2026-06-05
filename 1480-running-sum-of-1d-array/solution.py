# Running Sum of 1d Array
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        summ = 0
        n =len(nums)
  

        for i in range(n):
            summ = summ+nums[i]
            nums[i]=summ   

        return nums

            
