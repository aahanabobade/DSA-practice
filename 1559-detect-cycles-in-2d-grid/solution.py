# Detect Cycles in 2D Grid
# Difficulty: Medium
# Runtime: 619 ms
# Memory: 213.9 MB
# https://leetcode.com/problems/detect-cycles-in-2d-grid/

                    if dfs(nr, nc, r, c, ch):
                        continue
                    if nr == pr and nc == pc:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == ch:
                nr, nc = r + dr, c + dc
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            visited[r][c] = True
                return True
            if visited[r][c]:
        def dfs(r, c, pr, pc, ch):
        
        visited = [[False]*n for _ in range(m)]
