# Find X Value of Array I
# Difficulty: Medium
# Runtime: 504 ms
# Memory: 21.4 MB
# https://leetcode.com/problems/find-x-value-of-array-i/

                if dp[r]:
                    new_r = (r * x) % k
                    new_dp[new_r] += dp[r]
            
            dp = new_dp
            
            # Every subarray ending here is one valid operation
            for r in range(k):
                ans[r] += dp[r]
        
        return ans

