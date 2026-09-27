# Reverse Substrings Between Each Pair of Parentheses
# Difficulty: Medium
# Runtime: 31 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

                temp = []
                while stack[-1] != '(':
                    temp.append(stack.pop())
                stack.pop()  
                stack.extend(temp)
            else:
                stack.append(i)

        return "".join(stack)
