# String to Integer (atoi)
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        i = 0
        n = len(s)

        # Skip leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # Check sign
        sign = 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1

        # Convert digits
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            # Overflow check
            if num > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return sign * num
