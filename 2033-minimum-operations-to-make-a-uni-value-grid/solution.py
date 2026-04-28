# Minimum Operations to Make a Uni-Value Grid
# Difficulty: Medium
# Runtime: 196 ms
# Memory: 32.5 MB
# https://leetcode.com/problems/minimum-operations-to-make-a-uni-value-grid/

        median = arr[len(arr) // 2]
        
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops 
