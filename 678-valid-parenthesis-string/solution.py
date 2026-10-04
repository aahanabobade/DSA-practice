# Valid Parenthesis String
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/valid-parenthesis-string/

                low -= 1
                high -= 1
            elif ch == ')':
                high += 1
            else:  # '*'
                low -= 1
                high += 1

            if high < 0:
                return False

            low = max(low, 0)

        return low == 0
