# Two Sum
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.2 MB
# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        n = len(nums)

        for i in range(n):
            if comp in seen:
                
            comp = target -nums[i]
                return [seen[comp],i]
            
            seen[nums[i]]=i
