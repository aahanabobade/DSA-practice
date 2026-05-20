# Remove Duplicates from Sorted Array
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.8 MB
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

        :rtype: int
        """
        n = len(nums)
        k = 1

        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k]= nums[i]
                k+=1
        
        return k
