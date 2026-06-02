# Remove Element
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/remove-element/

        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        n = len(nums)

        for i in range(n):
            if nums[i]!=val:
                k+=1
                nums[k]=nums[i]

        return k
