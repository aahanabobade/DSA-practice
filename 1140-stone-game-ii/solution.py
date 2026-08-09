# Stone Game II
# Difficulty: Medium
# Runtime: 316 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/stone-game-ii/


                # Try taking X piles
                for X in range(1, 2 * M + 1):
                    opponent = dp[i + X][max(M, X)]

                    # Total remaining - what opponent gets
                    current = suffix[i] - opponent

                    best = max(best, current)

                dp[i][M] = best

        return dp[0][1]


