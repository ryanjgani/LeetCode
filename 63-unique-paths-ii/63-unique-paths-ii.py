class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        temp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        temp[ROWS][COLS - 1] = 1
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if obstacleGrid[r][c] == 0:
                    temp[r][c] = temp[r + 1][c] + temp[r][c + 1]
        return temp[0][0]
        
        
        # memo = {}
        # memo[(ROWS - 1, COLS - 1)] = 1
        # def dfs(i, j):
        #     if i >= ROWS or j >= COLS or obstacleGrid[i][j] == 1:
        #         return 0
        #     if (i, j) in memo:
        #         return memo[(i, j)]
        #     right = dfs(i, j + 1)
        #     left = dfs(i + 1, j)
        #     memo[(i, j)] = right + left
        #     return memo[(i, j)]
        # res = dfs(0, 0)
        # return res
        