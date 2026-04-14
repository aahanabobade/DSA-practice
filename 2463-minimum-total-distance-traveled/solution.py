# Minimum Total Distance Traveled
# Difficulty: Hard
# Runtime: 635 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/minimum-total-distance-traveled/

            for i in range(1, n + 1):
                cost = 0
                
                for k in range(1, min(limit, i) + 1):
                    cost += abs(robot[i - k] - pos)
                    new_dp[i] = min(new_dp[i], dp[i - k] + cost)
            
            dp = new_dp
        
        return dp[n]
