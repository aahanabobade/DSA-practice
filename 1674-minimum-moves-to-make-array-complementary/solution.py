# Minimum Moves to Make Array Complementary
# Difficulty: Medium
# Runtime: 355 ms
# Memory: 26 MB
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

class Solution(object):
    def minMoves(self, nums, limit):
        n = len(nums)

        # sums range from 2 to 2*limit
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            # default +2 moves
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # one move range becomes 1 instead of 2
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1

            # exact sum becomes 0 instead of 1
