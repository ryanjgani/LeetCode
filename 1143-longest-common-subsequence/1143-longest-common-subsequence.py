class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         Top down
        memo = {}
        def dfs(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            if text1[i] == text2[j]:
                res = 1 + dfs(i + 1, j + 1)
            else:
                res = max(dfs(i + 1, j), dfs(i, j + 1))
            memo[(i, j)] = res
            return res
            
        return dfs(0, 0)
        
        
        
        
        # brute force O(2^n)
#         def dfs(i, j):
#             if i == len(text1) or j == len(text2):
#                 return 0
#             if text1[i] == text2[j]:
#                 return 1 + dfs(i + 1, j + 1)
#             else:
#                 return max(dfs(i + 1, j), dfs(i, j + 1))
            
#         return dfs(0, 0)
        
        
        # bottom up
        # ROWS = len(text1)
        # COLS = len(text2)
        # dp = []
        # for j in range(ROWS + 1):
        #     row_dp = []
        #     for i in range(COLS + 1):
        #         row_dp.append(0)
        #     dp.append(row_dp)
        # for i in range(ROWS - 1, -1, -1):
        #     for j in range(COLS - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        # return dp[0][0]