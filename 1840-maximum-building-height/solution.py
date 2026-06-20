# Maximum Building Height
# Difficulty: Hard
# Runtime: 406 ms
# Memory: 38.3 MB
# https://leetcode.com/problems/maximum-building-height/

        m = len(restrictions)

        restrictions.sort()
        # Sort by building index

        restrictions.append([n, n - 1])
        # Add mandatory restrictions
        restrictions.append([1, 0])
        :rtype: int
        """
        :type restrictions: List[List[int]]
        """
        :type n: int
    def maxBuilding(self, n, restrictions):
class Solution(object):
