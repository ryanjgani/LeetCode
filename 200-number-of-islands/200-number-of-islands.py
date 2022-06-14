class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        rows, cols = len(grid), len(grid[0])
        res = 0
        
        def bfs(r, c):
            q = []
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.pop(0)
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    r = dr + row
                    c = dc + col
                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visit:
                        visit.add((r, c))
                        q.append((r, c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    res += 1
                
        return res