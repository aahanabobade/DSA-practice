# Rotate String
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/rotate-string/

class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        return goal in (s + s)
