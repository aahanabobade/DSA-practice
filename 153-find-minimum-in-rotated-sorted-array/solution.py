# Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n -1

        while left< right:
            mid = (left+right)//2

            if nums[mid]>nums[right]:
                left=mid+1
            else:
                right = mid
    def findMin(self, nums):
        """
class Solution(object):
