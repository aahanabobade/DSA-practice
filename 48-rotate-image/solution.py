# Rotate Image
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            left, right = 0, n - 1
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1