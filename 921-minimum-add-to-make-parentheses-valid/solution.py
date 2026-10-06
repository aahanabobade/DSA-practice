# Minimum Add to Make Parentheses Valid
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    add += 1

        return add + open
