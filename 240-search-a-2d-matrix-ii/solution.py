# Search a 2D Matrix II
# Difficulty: Medium
# Runtime: 128 ms
# Memory: 18.4 MB
# https://leetcode.com/problems/search-a-2d-matrix-ii/

        """
        row = len(matrix)
        col = len(matrix[0])

        i = 0
        j = col-1

        while i<row and j >=0:
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                j-=1
            else:
                i+=1
        
        return False
        
