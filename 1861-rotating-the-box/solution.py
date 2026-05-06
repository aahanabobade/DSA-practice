# Rotating the Box
# Difficulty: Medium
# Runtime: 203 ms
# Memory: 53.3 MB
# https://leetcode.com/problems/rotating-the-box/

        
        res = [[None] * m for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                res[j][m - 1 - i] = boxGrid[i][j]
        
        return res
