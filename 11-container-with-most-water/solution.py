# Container With Most Water
# Difficulty: Medium
# Runtime: 123 ms
# Memory: 20.6 MB
# https://leetcode.com/problems/container-with-most-water/


            h = min(height[left], height[right])
            w = right - left
            area = h * w

        while left < right:
        max_area = 0
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
