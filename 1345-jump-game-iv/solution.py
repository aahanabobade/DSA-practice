# Jump Game IV
# Difficulty: Hard
# Runtime: 353 ms
# Memory: 27.2 MB
# https://leetcode.com/problems/jump-game-iv/

from collections import defaultdict, deque

class Solution(object):

    def minJumps(self, arr):

        n = len(arr)

        if n == 1:
            return 0

        # value -> list of indices
        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        q = deque([(0, 0)])   # (index, steps)

        visited = set([0])

        while q:

            idx, steps = q.popleft()

            # reached end
            if idx == n - 1:
                return steps

            neighbors = []

            # same value jumps
            neighbors.extend(graph[arr[idx]])

            # adjacent jumps
            neighbors.append(idx - 1)
            neighbors.append(idx + 1)

            for nei in neighbors:

                if 0 <= nei < n and nei not in visited:

                    visited.add(nei)

                    q.append((nei, steps + 1))

            # IMPORTANT OPTIMIZATION
            # avoid revisiting same-value group
            del graph[arr[idx]]