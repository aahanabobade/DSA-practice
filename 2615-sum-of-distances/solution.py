# Sum of Distances
# Difficulty: Medium
# Runtime: 192 ms
# Memory: 43.7 MB
# https://leetcode.com/problems/sum-of-distances/

                prefix[i] = prefix[i-1] + positions[i]
            
            for i in range(k):
                idx = positions[i]
                
                left = positions[i] * i - (prefix[i-1] if i > 0 else 0)
                right = (prefix[k-1] - prefix[i]) - positions[i] * (k - i - 1)
            for i in range(1, k):
            
            prefix[0] = positions[0]
            prefix = [0] * k
            
