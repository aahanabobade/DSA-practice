# Squares of a Sorted Array
# Difficulty: Easy
# Runtime: 8 ms
# Memory: 14.3 MB
# https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n

        left = 0
        right = n-1
        pos = n-1

        while left<=right:
            if abs(nums[left])>abs(nums[right]):
                result[pos]=nums[left]*nums[left]
                left+=1
            else:
                result[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
    
        return result
                