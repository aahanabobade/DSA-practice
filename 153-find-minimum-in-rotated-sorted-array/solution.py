# Find Minimum in Rotated Sorted Array
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

class Solution(object):
    def findMin(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Minimum is in right half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # Minimum is at mid or left half
                right = mid

        return nums[left]
