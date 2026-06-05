# Find Numbers with Even Number of Digits
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        n = len(nums)

        for i in range(n):
            if len(str(nums[i]))%2== 0 :
                count+=1
            



        return count