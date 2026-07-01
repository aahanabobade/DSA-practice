# Find the Safest Path in a Grid
# Difficulty: Medium
# Runtime: 6198 ms
# Memory: 25.8 MB
# https://leetcode.com/problems/find-the-safest-path-in-a-grid/


        left = 0
        right = max(max(row) for row in dist)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
