# Valid Parentheses
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/valid-parentheses/


        for i in s:

            if i in mp:
                
                if not stack or stack[-1] != mp[i]:
                    return False

                stack.pop()

            else:
                stack.append(i)

        return len(stack) == 0
