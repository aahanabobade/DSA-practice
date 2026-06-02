# Remove Duplicates from Sorted Array II
# Difficulty: Medium
# Runtime: 59 ms
# Memory: 15.2 MB
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

        """
        n = len(nums)

        if n <=2:
            return n
        
        k = 2

        for i in range(2,n):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        
        return k
