class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {}

        n = len(nums)

        for i in range(n):
            num = nums[i]
        
            if num in seen and i -seen[num]<=k:
                return True

            seen[num]=i   

        return False     