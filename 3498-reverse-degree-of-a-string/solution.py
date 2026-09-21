# Reverse Degree of a String
# Difficulty: Easy
# Runtime: 13 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/reverse-degree-of-a-string/

        for i, ch in enumerate(s):
            # a -> 26, b -> 25, ..., z -> 1
            reverse_value = 26 - (ord(ch) - ord('a'))

            # i is 0-indexed, so position is i + 1
            ans += reverse_value * (i + 1)

        return ans

