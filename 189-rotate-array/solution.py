# Rotate Array
# Difficulty: Medium
# Runtime: 16 ms
# Memory: 22.3 MB
# https://leetcode.com/problems/rotate-array/

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        def reverse(left, right):

        k = k%n
        n = len(nums)
        """
        :rtype: None Do not return anything, modify nums in-place instead.

        reverse(0, k - 1)

