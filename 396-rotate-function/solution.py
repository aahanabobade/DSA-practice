# Rotate Function
# Difficulty: Medium
# Runtime: 136 ms
# Memory: 31.5 MB
# https://leetcode.com/problems/rotate-function/

        total_sum = sum(nums)

        curr = sum(i * num for i, num in enumerate(nums))
        max_val = curr
        
        for k in range(1, n):
            curr = curr + total_sum - n * nums[n - k]
        n = len(nums)
class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
            max_val = max(max_val, curr)
