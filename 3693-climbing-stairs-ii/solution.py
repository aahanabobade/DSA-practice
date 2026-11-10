# Climbing Stairs II
# Difficulty: Medium
# Runtime: 1173 ms
# Memory: 23.5 MB
# https://leetcode.com/problems/climbing-stairs-ii/


class Solution(object):
    def climbStairs(self, n, costs):
        dp = [float('inf')] * (n + 1)

        dp[0] = 0

        for i in range(1, n + 1):

            for j in range(max(0, i - 3), i):

                jump = i - j

                total = dp[j] + costs[i - 1] + jump * jump

                dp[i] = min(dp[i], total)

        return dp[n]

