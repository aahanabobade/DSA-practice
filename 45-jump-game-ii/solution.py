# Jump Game II
# Difficulty: Medium
# Runtime: 13 ms
# Memory: 13.2 MB
# https://leetcode.com/problems/jump-game-ii/

        farthest = 0

        for i in range(n - 1):   # don't need to jump FROM the last index
            farthest = max(farthest, nums[i] + i)       # update furthest reachable

            if i == current_end:  # exhausted current level
        n = len(nums)
        current_end = 0
        jumps = 0
        """
        :type nums: List[int]
        :rtype: int
        """
    def jump(self, nums):
class Solution(object):
