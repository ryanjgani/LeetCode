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
        
        
        # dp = {}
        # def dfs(i, j, count):
        #     if (i, j) in dp: return dp[(i, j)]
        #     if i == len(text1) or j == len(text2):
        #         return count
        #     if text1[i] == text2[j]:
        #         count += 1
        #         dp[(i, j)] = max(count, dfs(i + 1, j + 1, count))
        #     else:
        #         dp[(i, j)] = max(count, dfs(i + 1, j, count), dfs(i, j + 1, count))
        #     return dp[(i, j)]
        # return dfs(0, 0, 0)
