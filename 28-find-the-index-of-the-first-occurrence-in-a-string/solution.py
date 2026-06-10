# Find the Index of the First Occurrence in a String
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        m = len(needle)
        l = n-m+1
        for i in range(l):
            if haystack[i:i + m] == needle:
                return i


        return -1
