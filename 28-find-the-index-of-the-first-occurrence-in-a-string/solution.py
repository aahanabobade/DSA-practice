# Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
