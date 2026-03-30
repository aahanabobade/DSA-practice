# Maximum Subarray
# Difficulty: Medium
# Runtime: 107 ms
# Memory: 21.1 MB
# https://leetcode.com/problems/maximum-subarray/

        :rtype: int
        """
        n = len(nums)
        max_sum = nums[0]
        curr_sum = nums[0]

        for i in range(1,n):
            curr_sum = max(nums[i],nums[i]+curr_sum)
            max_sum = max(curr_sum,max_sum)
        
        return max_sum
        
