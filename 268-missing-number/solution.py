# Missing Number
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.4 MB
# https://leetcode.com/problems/missing-number/

    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        expected = n * (n + 1) // 2
        actual = sum(nums)

        return expected - actual

