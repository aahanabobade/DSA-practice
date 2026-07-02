# Find a Safe Walk Through a Grid
# Difficulty: Medium
# Runtime: 98 ms
# Memory: 12.6 MB
# https://leetcode.com/problems/find-a-safe-walk-through-a-grid/

        directions = [(1,0), (-1,0), (0,1), (0,-1)]


        dq = deque([(0, 0)])
        dist[0][0] = grid[0][0]

        dist = [[INF] * n for _ in range(m)]
        INF = float('inf')

        n = len(grid[0])
        m = len(grid)
        """
        :rtype: bool
        :type health: int
        :type grid: List[List[int]]
        """
