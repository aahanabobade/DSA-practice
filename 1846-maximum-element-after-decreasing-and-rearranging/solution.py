# Maximum Element After Decreasing and Rearranging
# Difficulty: Medium
# Runtime: 50 ms
# Memory: 17.6 MB
# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/

class Solution(object):
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()

        arr[0] = 1

        for i in xrange(1, len(arr)):
            arr[i] = min(arr[i], arr[i - 1] + 1)

        return arr[-1]
