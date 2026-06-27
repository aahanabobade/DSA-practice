# Find the Maximum Number of Elements in Subset
# Difficulty: Medium
# Runtime: 131 ms
# Memory: 24.2 MB
# https://leetcode.com/problems/find-the-maximum-number-of-elements-in-subset/


            if curr in freq and freq[curr] == 1:
                currLen += 1
            else:
                currLen -= 1

            maxLen = max(maxLen, currLen)

        return maxLen
                currLen += 2
                curr *= curr
