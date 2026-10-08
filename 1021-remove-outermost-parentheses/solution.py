# Remove Outermost Parentheses
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/remove-outermost-parentheses/

        for ch in s:
            if ch == '(':
                if depth > 0:
                    result.append(ch)
                depth += 1

            else:
                depth -= 1
                if depth > 0:
                    result.append(ch)

        return ''.join(result)
