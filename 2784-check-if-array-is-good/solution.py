# Check if Array is Good
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 12.2 MB
# https://leetcode.com/problems/check-if-array-is-good/

    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        n = nums[-1]

·‌·‌·‌·‌·‌·‌·‌·‌#·‌Length·‌must·‌be·‌n·‌+·‌1
        if len(nums) != n + 1:
            return False

        # Check 1 to n-1 appear once
        for i in range(n - 1):
            if nums[i] != i + 1:
                return False

        # Last two elements must both be n
        return nums[-1] == n and nums[-2] == n
