# Furthest Point From Origin
# Difficulty: Easy
# Runtime: 5 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/furthest-point-from-origin/

        """
        :type moves: str
        :rtype: int
        """

        L = moves.count('L')
        R = moves.count('R')
        blank = moves.count('_')
        
        return abs(R - L) + blank
        
