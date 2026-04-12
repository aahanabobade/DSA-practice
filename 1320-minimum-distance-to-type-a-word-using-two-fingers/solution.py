# Minimum Distance to Type a Word Using Two Fingers
# Difficulty: Hard
# Runtime: 112 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/minimum-distance-to-type-a-word-using-two-fingers/

            for j in range(26):
                gain = max(gain, dp[j] + dist(prev, cur) - dist(j, cur))
            
            dp[prev] = gain
            res += dist(prev, cur)
        
        return res - max(dp)
