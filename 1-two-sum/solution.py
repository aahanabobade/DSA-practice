# Two Sum
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 13.2 MB
# https://leetcode.com/problems/two-sum/

        seen = {}

        for i in range(n):
            complement = target- nums[i]

            if complement in seen:
                return (seen[complement],i)
            
            seen[nums[i]]=i
