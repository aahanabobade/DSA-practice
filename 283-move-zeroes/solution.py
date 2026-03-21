# Move Zeroes
# Difficulty: Easy
# Runtime: 7 ms
# Memory: 13.5 MB
# https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        j = 0  # position for next non-zero
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
