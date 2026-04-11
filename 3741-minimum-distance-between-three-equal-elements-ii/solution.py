# Minimum Distance Between Three Equal Elements II
# Difficulty: Medium
# Runtime: 518 ms
# Memory: 41.5 MB
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

        ans = float('inf')
        
        # check each value
        for indices in pos.values():
            if len(indices) < 3:
                continue
            
            for i in range(len(indices) - 2):
                ans = min(ans, 2 * (indices[i+2] - indices[i]))
        
        return ans if ans != float('inf') else -1
