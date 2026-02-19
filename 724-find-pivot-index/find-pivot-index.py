class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        summ = 0 

        for i in range(n):
            summ +=nums[i]

        left = 0 

        for i in range(n):
            right = summ -left - nums[i]

            if left == right:
                return i 

            left +=nums[i]
        
        return -1
            
        