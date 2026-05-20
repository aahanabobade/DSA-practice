# Two Sum
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 13.2 MB
# https://leetcode.com/problems/two-sum/

        :rtype: List[int]
        """
        seen = {}

        n = len(nums)
        for i in range(n):
            comp = target -nums[i]
            if comp in seen:
                return [seen[comp],i]
        
            seen[nums[i]]=i
