# Number of Ways to Assign Edge Weights II
# Difficulty: Hard
# Runtime: 1944 ms
# Memory: 86.1 MB
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

                    u = parent[j][u]
                    v = parent[j][v]

            return parent[0][u]

        ans = []
        for u, v in queries:
            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow(2, dist - 1, MOD))

        return ans
