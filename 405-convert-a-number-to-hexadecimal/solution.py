# Convert a Number to Hexadecimal
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        
        hex_chars = "0123456789abcdef"
        num &= 0xffffffff
        result = ""
