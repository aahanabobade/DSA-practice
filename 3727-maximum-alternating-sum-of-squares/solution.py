# Maximum Alternating Sum of Squares
# Difficulty: Medium
# Runtime: 180 ms
# Memory: 21.3 MB
# https://leetcode.com/problems/maximum-alternating-sum-of-squares/

class Solution(object):
    def maxAlternatingSum(self, nums):
        nums = [x * x for x in nums]
        nums.sort()

        n = len(nums)
        
        # Largest ceil(n/2) are positive
        # Smallest floor(n/2) are negative
        return sum(nums[(n // 2):]) - sum(nums[:n // 2])
