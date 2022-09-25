class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        dp = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]
        for r in range(len(text2) - 1, -1, -1):
            for c in range(len(text1) - 1, -1, -1):
                if text2[r] == text1[c]:
                    dp[r][c] = 1 + dp[r + 1][c + 1]
                else:
                    dp[r][c] = max(dp[r + 1][c], dp[r][c + 1])
        return dp[0][0]
        
        
        dp = {}
        def dfs(i, j):
            if (i, j) in dp: return dp[(i, j)]
            if i == len(text1) or j == len(text2):
                return 0
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + dfs(i + 1, j + 1)
            else:
                dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return dp[(i, j)]
        return dfs(0, 0)
