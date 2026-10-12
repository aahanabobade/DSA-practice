# Sum of Squares of Special Elements
# Difficulty: Easy
# Runtime: 8 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/sum-of-squares-of-special-elements/

class Solution(object):
    def sumOfSquares(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n):
            index = i + 1

            if n % index == 0:
                ans += nums[i] * nums[i]

        return ans
