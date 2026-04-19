# Maximum Distance Between a Pair of Values
# Difficulty: Medium
# Runtime: 70 ms
# Memory: 23.9 MB
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

        
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                maxx = max(maxx, j - i)
                j += 1  
            else:
                i += 1
        
        return maxx
