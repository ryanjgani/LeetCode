class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0
        visited = [([False] * COLS) for _ in range(ROWS)]
        
        stack = []
        for i in range(ROWS):
            for j in range(COLS):
                if not visited[i][j] and grid[i][j] == '1':
                    queue = [[i, j]]
                    while queue:
                        r, c = queue.pop(0)
                        if r >= ROWS or c >= COLS or c < 0 or r < 0 or visited[r][c] or grid[r][c] == '0': continue
                        visited[r][c] = True
                        queue.append([r, c + 1])
                        queue.append([r + 1, c])
                        queue.append([r, c - 1])
                        queue.append([r - 1, c])
                    res += 1
        return res
        
        
#         def dfs(r, c):
#             if r >= ROWS or c >= COLS or c < 0 or r < 0 or visited[r][c] or grid[r][c] == '0':
#                 return
#             visited[r][c] = True
#             dfs(r, c + 1)
#             dfs(r + 1, c)
#             dfs(r, c - 1)
#             dfs(r - 1, c)
        
#         for i in range(ROWS):
#             for j in range(COLS):
#                 if not visited[i][j] and grid[i][j] == '1':
#                     dfs(i, j)
#                     res += 1
#         return res