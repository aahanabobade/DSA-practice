# Predict the Winner
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/predict-the-winner/

class Solution(object):
    def predictTheWinner(self, nums):
        n = len(nums)
        dp = nums[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(
                    nums[i] - dp[j],
                    nums[j] - dp[j - 1]
                )

        return dp[n - 1] >= 0
