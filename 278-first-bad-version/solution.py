# First Bad Version
# Difficulty: Easy
# Runtime: 15 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
    
#use 2 pointer
        left =1
        right =n

        while left<right:
            mid = left+(right-left)//2

            if isBadVersion(mid):
                right = mid
            else:
                left =mid+1
        
        return left
