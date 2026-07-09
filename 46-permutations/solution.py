# Permutations
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/permutations/

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res =[]
        

        def backtrack(path, remaining):
            if not remaining:
                res.append(path[:])
                return

            n= len(remaining)
            
            for i in range(n):
                path.append(remaining[i])
                backtrack(path,remaining[:i]+remaining[i+1:])
                path.pop()
        
        backtrack([],nums)
        return res
