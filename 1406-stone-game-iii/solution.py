# Stone Game III
# Difficulty: Hard
# Runtime: 1016 ms
# Memory: 15.5 MB
# https://leetcode.com/problems/stone-game-iii/

            best = float("-inf")
            take = 0

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]
                    best = max(best, take - dp[k])

            dp = [best] + dp[:3]

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
