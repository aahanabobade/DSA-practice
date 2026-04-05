# Subsets
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 12.5 MB
# https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        result = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in result:
                new_subsets.append(subset + [num])
            result.extend(new_subsets)
        
        return result
