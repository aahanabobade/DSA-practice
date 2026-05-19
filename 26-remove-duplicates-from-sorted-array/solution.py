# Remove Duplicates from Sorted Array
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.7 MB
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
        
        k =1
                k+=1
        return k
