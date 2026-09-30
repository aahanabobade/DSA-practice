# Maximum Nesting Depth of Two Valid Parentheses Strings
# Difficulty: Medium
# Runtime: 2 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

        for i in seq:
            if i == '(':
                ans.append(depth % 2)
                depth += 1
            else:
                depth -= 1
                ans.append(depth % 2)

        return ans
