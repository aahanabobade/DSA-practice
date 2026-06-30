# Number of Substrings Containing All Three Characters
# Difficulty: Medium
# Runtime: 146 ms
# Memory: 14.4 MB
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

        n = len(s)
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        ans = 0

        for right in range(n):
            count[s[right]] += 1

            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                ans += n - right
                count[s[left]] -= 1
                left += 1

        return ans
