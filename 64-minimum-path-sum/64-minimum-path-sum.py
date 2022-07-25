class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = [[float('inf')] * (COLS + 1) for _ in range(ROWS + 1)]
        dp[ROWS][COLS - 1] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                dp[r][c] = min(dp[r][c + 1], dp[r + 1][c]) + grid[r][c]
        return dp[0][0]
    
#           top down memoization
#         memo = {}
#         def dfs(i, j):
#             if (i, j) in memo: 
#                 return memo[(i, j)]
#             if i == ROWS - 1 and j == COLS - 1:
#                 return grid[i][j]
#             if i >= ROWS or j >= COLS:
#                 return float('inf')
#             left = dfs(i + 1, j) + grid[i][j]
#             down = dfs(i, j + 1) + grid[i][j]
#             memo[(i, j)] = min(left, down)
#             return memo[(i, j)]
#         res = dfs(0, 0)
#         return res