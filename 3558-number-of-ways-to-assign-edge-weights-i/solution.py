# Number of Ways to Assign Edge Weights I
# Difficulty: Medium
# Runtime: 816 ms
# Memory: 66.8 MB
# https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-i/

        q = deque([(1, 0)])  # (node, depth)
        visited = {1}
        max_depth = 0

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        graph = [[] for _ in range(n + 1)]
        n = len(edges) + 1

        MOD = 10**9 + 7
    def assignEdgeWeights(self, edges):
class Solution(object):
from collections import deque

