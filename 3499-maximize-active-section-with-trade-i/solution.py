# Maximize Active Section with Trade I
# Difficulty: Medium
# Runtime: 2292 ms
# Memory: 25.6 MB
# https://leetcode.com/problems/maximize-active-section-with-trade-i/

        for i in range(1, len(runs) - 1):
            if runs[i][0] == '1':
                left = runs[i - 1][1]
                right = runs[i + 1][1]

                ans = max(ans, ones + left + right)

        return min(ans, len(s))
