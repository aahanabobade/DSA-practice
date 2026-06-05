# Check if Array Is Sorted and Rotated
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

class Solution(object):
    def check(self, nums):
        n = len(nums)
        count = 0

        for i in range(n):
            if nums[i]> nums[(i+1)%n]:
                count+=1

        return count <= 1
        