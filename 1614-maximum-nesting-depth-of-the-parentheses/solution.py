# Maximum Nesting Depth of the Parentheses
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.2 MB
# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

        depth = 0
        max_depth = 0

        for ch in s:
            if ch == '(':
                depth += 1
                max_depth = max(max_depth, depth)

            elif ch == ')':
                depth -= 1

        return max_depth
