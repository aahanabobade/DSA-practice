# Rank Transform of an Array
# Difficulty: Easy
# Runtime: 43 ms
# Memory: 28 MB
# https://leetcode.com/problems/rank-transform-of-an-array/

        rank_map={}
        rank =1

        for i in sorted(set(arr)):
            rank_map[i]=rank
            rank+=1
        
        return [rank_map[i] for i in arr]
