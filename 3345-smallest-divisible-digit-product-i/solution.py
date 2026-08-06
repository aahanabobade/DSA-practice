# Smallest Divisible Digit Product I
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/smallest-divisible-digit-product-i/

            prod = 1
            for digit in str(n):
                prod *= int(digit)

            if prod % t == 0:
                return n

            n += 1
        while True:
        """
