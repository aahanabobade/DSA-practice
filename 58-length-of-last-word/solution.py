# Length of Last Word
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1
        length = 0

        # skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # count the last word
        while i >= 0 and s[i] != " ":
            length += 1
            i -= 1

        return length
        
