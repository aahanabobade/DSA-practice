# Remove Duplicates from Sorted Array
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 14 MB
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        
        return k
        for i in range(1,n):

        k = 1
        n = len(nums)
        """
        :rtype: int
            

