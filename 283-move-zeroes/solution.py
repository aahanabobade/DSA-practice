# Move Zeroes
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 13.6 MB
# https://leetcode.com/problems/move-zeroes/

        
        j = 0
        n = len(nums)
        
    def moveZeroes(self, nums):

        for i in range(n):
            if nums[i]!=0:
                nums[j],nums[i] = nums[i],nums[j]
                j+=1
