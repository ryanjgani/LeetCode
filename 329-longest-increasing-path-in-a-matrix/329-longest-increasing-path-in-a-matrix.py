class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        memo = {}
        def dfs(i, j, prev):
            if i >= rows or j >= cols or i < 0 or j < 0 or matrix[i][j] <= prev:
                return -1
            if (i, j) in memo:
                return memo[(i, j)]
            temp = 0
            for r, c in directions:
                temp = max(temp, 1 + dfs(i + r, j + c, matrix[i][j]))
            memo[(i, j)] = temp
            return temp
        res = 0
        for r in range(rows):
            for c in range(cols):
                res = max(res, 1 + dfs(r, c, -1))
        return res