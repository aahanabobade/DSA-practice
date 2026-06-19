# Find the Highest Altitude
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.2 MB
# https://leetcode.com/problems/find-the-highest-altitude/

        """
        :type gain: List[int]
        :rtype: int
        """
        start = 0
        n = len(gain)
        new= [0]*n

        for i in range(n):  
            start += gain[i]
            new[i] = start

        return max(new + [0])      
