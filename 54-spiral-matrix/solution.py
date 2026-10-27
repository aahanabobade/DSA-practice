# Spiral Matrix
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.1 MB
# https://leetcode.com/problems/spiral-matrix/


        while left<=right and top<=bottom:

        result = []

        top = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        left = 0
