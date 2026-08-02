# Stone Game
# Difficulty: Medium
# Runtime: 649 ms
# Memory: 47.8 MB
# https://leetcode.com/problems/stone-game/

    def stoneGame(self, piles):
        n = len(piles)
        memo = {}

        def dfs(i, j):
            if i == j:
                return piles[i]

            if (i, j) in memo:
                return memo[(i, j)]

            left = piles[i] - dfs(i + 1, j)
            right = piles[j] - dfs(i, j - 1)

            memo[(i, j)] = max(left, right)
            return memo[(i, j)]

        return dfs(0, n - 1) > 0
class Solution(object):
