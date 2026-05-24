# Jump Game V
# Difficulty: Hard
# Runtime: 538 ms
# Memory: 23.5 MB
# https://leetcode.com/problems/jump-game-v/


        dp = [-1] * n
        n = len(arr)
    def maxJumps(self, arr, d):
class Solution:
        def dfs(i):
            if dp[i] != -1:
                return dp[i]

            ans = 1

            # explore left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]:
                    break
                ans = max(ans, 1 + dfs(j))
