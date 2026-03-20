# Combination Sum
# Difficulty: Medium
# Runtime: 15 ms
# Memory: 12.4 MB
# https://leetcode.com/problems/combination-sum/

                
                backtrack(i, current, remaining - candidates[i])
                
                current.pop()
        
        backtrack(0, [], target)
        return result
