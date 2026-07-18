# Find Greatest Common Divisor of Array
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

            while b:
                a, b = b, a % b
            return a
        
        return gcd(min(nums), max(nums))
        def gcd(a, b):
        """
        :rtype: int
