# Maximum Number of Jumps to Reach the Last Index
# Difficulty: Medium
# Runtime: 472 ms
# Memory: 12.7 MB
# https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

        dp[0] = 0
        
        for i in range(n):
            if dp[i] == -1:
                continue
                
            for j in range(i + 1, n):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[n - 1]
