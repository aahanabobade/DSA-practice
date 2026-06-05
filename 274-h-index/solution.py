# H-Index
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 12.8 MB
# https://leetcode.com/problems/h-index/

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0

        for i in range(len(citations)):
            if citations[i] >= i + 1:  # i+1 because i is 0-indexed
                h = i + 1
            else:
                break  # since sorted, no point continuing

        return h
            