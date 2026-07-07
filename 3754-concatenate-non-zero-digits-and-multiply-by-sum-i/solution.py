# Concatenate Non-Zero Digits and Multiply by Sum I
# Difficulty: Easy
# Runtime: 5 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-i/

        for ch in str(n):
            if ch != '0':
                digits.append(ch)

        if not digits:
            return 0

        x = int("".join(digits))
        digit_sum = sum(int(d) for d in digits)

        return x * digit_sum
