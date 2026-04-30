# Maximum Path Score in a Grid
# Difficulty: Medium
# Runtime: 6358 ms
# Memory: 21.9 MB
# https://leetcode.com/problems/maximum-path-score-in-a-grid/

                            )
                    
                    # from left
                    if j > 0 and new_dp[j-1][c] != -1:
                        if c + cost_add <= k:
                            new_dp[j][c + cost_add] = max(
                                new_dp[j][c + cost_add],
                                new_dp[j-1][c] + score_add
                            )
            
            dp = new_dp
        
