# Palindrome Number
# Difficulty: Easy
# Runtime: 7 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        while x < 0 or(x%10 == 0  and x!=0):
            return False

        reversed_half = 0

        while x>reversed_half:
            reversed_half = reversed_half *10+x%10
            x//=10
        
        return x == reversed_half or  x==reversed_half//10