# Number of Strings That Appear as Substrings in Word
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        count = 0

        for i in patterns:
            if i in word:
                count += 1

        return count
