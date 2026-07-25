# Maximum Product of Two Digits
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/maximum-product-of-two-digits/

        ans = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                ans = max(ans, digits[i] * digits[j])

        return ans
