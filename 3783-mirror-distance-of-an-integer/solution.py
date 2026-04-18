# Mirror Distance of an Integer
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/mirror-distance-of-an-integer/

class Solution(object):
    def mirrorDistance(self, n):
        """
        :type n: int
        :rtype: int
        """

        reversed_n = int(str(n)[::-1])
        
        return abs(n - reversed_n)
