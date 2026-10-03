# Longest Valid Parentheses
# Difficulty: Hard
# Runtime: 23 ms
# Memory: 13.6 MB
# https://leetcode.com/problems/longest-valid-parentheses/

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
