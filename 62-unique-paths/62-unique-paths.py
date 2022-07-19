class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # bottom up dp
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                dp[r][c] += (dp[r + 1][c] + dp[r][c + 1])
        return dp[0][0]
        
        # memoization top down
        # res = 0
        # memo = {}
        # memo[(m - 1, n - 1)] = 1
        # def dfs(i, j):
        #     nonlocal res
        #     if (i, j) in memo: return memo[(i, j)]
        #     if i >= m or j >= n:
        #         return 0
        #     memo[(i, j)] = dfs(i, j + 1) + dfs(i + 1, j)
        #     return memo[(i, j)] 
        # return dfs(0, 0)
        