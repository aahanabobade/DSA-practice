# Cyclically Rotating a Grid
# Difficulty: Medium
# Runtime: 111 ms
# Memory: 19.7 MB
# https://leetcode.com/problems/cyclically-rotating-a-grid/

            for i in range(bottom - 1, top, -1):
                elems.append(grid[i][left])

            length = len(elems)
            rot = k % length

            # counter-clockwise rotation
            rotated = elems[rot:] + elems[:rot]

            idx = 0

