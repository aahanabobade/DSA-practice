# Jump Game
# Difficulty: Medium
# Runtime: 34 ms
# Memory: 13.4 MB
# https://leetcode.com/problems/jump-game/

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i >max_reach:
                return False
            max_reach = max(max_reach, i+nums[i])

        return True