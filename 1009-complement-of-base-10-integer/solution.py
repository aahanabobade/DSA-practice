# Complement of Base 10 Integer
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/complement-of-base-10-integer/

        """
        if n == 0:
            return 1
        
        mask = 1
        while mask <= n:
            mask <<= 1
        
        return (mask - 1) ^ n
        :rtype: int
        :type n: int
