# Path Existence Queries in a Graph I
# Difficulty: Medium
# Runtime: 100 ms
# Memory: 45.3 MB
# https://leetcode.com/problems/path-existence-queries-in-a-graph-i/


        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                cid += 1
            comp[i] = cid

        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans
