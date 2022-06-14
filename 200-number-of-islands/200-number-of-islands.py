class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        # def dfs(r, c):
        #     if r not in range(rows) or c not in range(cols) or grid[r][c] != 1
        
        def bfs(r, c):
            q = []
            q.append((r, c))
            grid[r][c] = '#'
            while q:
                row, col = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == '1':
                        grid[r][c] = '#'
                        q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
                
        return res