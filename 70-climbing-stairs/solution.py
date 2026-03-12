# Climbing Stairs
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/climbing-stairs/

        
        a, b = 1, 2
        
        for _ in range(3, n + 1):
            a, b = b, a + b
        
        return b
