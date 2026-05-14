# Search Insert Position
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left = 0
        right = n -1

        while left <= right :
            mid = left+(right-left)//2

            if nums[mid] ==target:
                return mid
            elif nums[mid]<target:
                left = mid +1
            else:
                right = mid -1
        
        return left
