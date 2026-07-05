# Number of Paths with Max Score
# Difficulty: Hard
# Runtime: 160 ms
# Memory: 13.5 MB
# https://leetcode.com/problems/number-of-paths-with-max-score/


                best_score, best_count = combine(i, j)

                if best_count == 0:
                    continue  # no valid path reaches here

                v = val(i, j)
                dp[i][j] = (best_score + v, best_count % MOD)

        score, count = dp[0][0]
        return [score, count] if count > 0 else [0, 0]
