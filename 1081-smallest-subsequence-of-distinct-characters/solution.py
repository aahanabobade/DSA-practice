# Smallest Subsequence of Distinct Characters
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

                continue
            
            while stack and stack[-1] > char and last_occurrence[stack[-1]] > i:
                stack.pop()
            
            stack.append(char)

        return ''.join(stack)
