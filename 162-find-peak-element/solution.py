# Find Peak Element
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/find-peak-element/

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n-1

        while left<right:
            mid = left+(right-left)//2

            if nums[mid]<nums[mid+1]:
                left = mid+1
            else:
                right = mid
        
        return left
