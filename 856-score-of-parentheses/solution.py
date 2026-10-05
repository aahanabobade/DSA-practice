# Score of Parentheses
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/score-of-parentheses/

                stack.append(0)
            else:
                current = stack.pop()

                if current == 0:
                    current = 1
                else:
                    current = 2 * current

                stack[-1] += current

        return stack[0]
