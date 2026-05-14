# Fibonacci Number
# Difficulty: Easy
# Runtime: 658 ms
# Memory: 12.3 MB
# https://leetcode.com/problems/fibonacci-number/

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        else:
        
        elif n ==1:
            return 1
            return self.fib(n - 1) + self.fib(n - 2)
        
