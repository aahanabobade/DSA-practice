class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        count = 0
        curr = 0

        for i in range(n):
            if nums[i]==1:
                curr+=1
                
            else:
                curr = 0

            count = max(count, curr)

        
        
        
        return count

        