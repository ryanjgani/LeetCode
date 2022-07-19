class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # brute force
        res = 0
        memo = {}
        memo[(m - 1, n - 1)] = 1
        def dfs(i, j):
            nonlocal res
            if (i, j) in memo: return memo[(i, j)]
            if i >= m or j >= n:
                
                return 0
            memo[(i, j)] = dfs(i, j + 1) + dfs(i + 1, j)
            return memo[(i, j)] 
        return dfs(0, 0)
        