# Shift 2D Grid
# Difficulty: Easy
# Runtime: 10 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/shift-2d-grid/

        n = len(grid[0])    
        
        result = [[0] * n for l in range(m)]
        
        for i in range(m):
            for j in range(n):
                total = i * n + j
                
                new_total = (total + k) % (m * n)
                
                new_i = new_total // n
                new_j = new_total % n
                
                result[new_i][new_j] = grid[i][j]
        
        return result
