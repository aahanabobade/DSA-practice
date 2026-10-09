# Minimum Insertions to Balance a Parentheses String
# Difficulty: Medium
# Runtime: 131 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/


                if open > 0:
                    open -= 1
                else:
                    # No '(' to match this '))'
                    # Insert '('
                    ans += 1

        # Every remaining '(' needs two ')'
        ans += open * 2

        return ans
