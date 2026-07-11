# Count the Number of Complete Components
# Difficulty: Medium
# Runtime: 141 ms
# Memory: 12.7 MB
# https://leetcode.com/problems/count-the-number-of-complete-components/

        for i in range(n):
            if find(i) == i:
                v = vertex_count[i]
                e = edge_count[i]
                if e == v * (v - 1) // 2:
                    result += 1
        
        return result
