# Valid Anagram
# Difficulty: Easy
# Runtime: 27 ms
# Memory: 13.4 MB
# https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)
        
