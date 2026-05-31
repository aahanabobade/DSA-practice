# Destroying Asteroids
# Difficulty: Medium
# Runtime: 91 ms
# Memory: 21.5 MB
# https://leetcode.com/problems/destroying-asteroids/

class Solution(object):
    def asteroidsDestroyed(self, mass, asteroids):
        """
        :type mass: int
        :type asteroids: List[int]
        :rtype: bool
        """
        asteroids.sort()
        for a in asteroids:
            if mass < a:
                return False
            mass += a
        return True
