class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        
        def dfs(r, c):
            if (r, c) in visited or grid[r][c] == 0:
                return 0
            visited.add((r, c))
            count = 1
            for i, j in moves:
                if 0 <= i + r < ROWS and 0 <= j + c < COLS and grid[r + i][j + c] == 1 and (i + r, j + c) not in visited:
                    count += dfs(i + r, j + c)
            return count
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    res = max(res, dfs(r, c))
        return res