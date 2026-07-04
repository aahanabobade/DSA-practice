# Minimum Score of a Path Between Two Cities
# Difficulty: Medium
# Runtime: 319 ms
# Memory: 77.5 MB
# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

            graph[v].append((u, d))
            graph[u].append((v, d))

        for u, v, d in roads:

        visited = set()
        ans = [float("inf")]

        def dfs(node):
            visited.add(node)

            for nei, dist in graph[node]:
                ans[0] = min(ans[0], dist)
                if nei not in visited:
                    dfs(nei)

