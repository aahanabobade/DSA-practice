# Missing Number
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.3 MB
# https://leetcode.com/problems/missing-number/

        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        actual = n*(n+1)//2
        expected = sum(nums)
        """
    def missingNumber(self, nums):
class Solution(object):
