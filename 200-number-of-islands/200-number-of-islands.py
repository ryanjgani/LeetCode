class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] in ("0", "-1"):
                return
            grid[i][j] = '-1'
            for r, c in d:
                if 0 <= i + r < rows and 0 <= j + c < cols:
                    dfs(i + r, j + c)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    res += 1
        return res
            
        