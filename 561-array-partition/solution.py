# Array Partition
# Difficulty: Easy
# Runtime: 35 ms
# Memory: 14 MB
# https://leetcode.com/problems/array-partition/

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return sum(nums[::2])
        
