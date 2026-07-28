# Smallest Palindromic Rearrangement I
# Difficulty: Medium
# Runtime: 483 ms
# Memory: 13.6 MB
# https://leetcode.com/problems/smallest-palindromic-rearrangement-i/

        """
        :type s: str
        :rtype: str
        """
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        half = []
        mid = ""

        for i in range(26):
