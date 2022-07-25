class Solution:
    def numDecodings(self, s: str) -> int:
        
        prev = doubleprev = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                current = 0
            else:
                current = prev
                if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                    current += doubleprev
            doubleprev = prev
            prev = current
            
        return current
        
        
        
        # Bottom up O(n) time and space
        # dp = [0] * (len(s) + 1)
        # dp[len(s)] = 1
        # for i in range(len(s) - 1, -1, -1):
        #     if s[i] == '0':
        #         dp[i] = 0
        #         continue
        #     dp[i] = dp[i + 1]
        #     if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
        #         dp[i] += dp[i + 2]
        # return dp[0]        
        
        
#           Top Down Memo O(n) Time        
#         memo = {len(s): 1}
#         def dfs(i):
#             if i in memo:
#                 return memo[i]
#             if s[i] == '0':
#                 return 0
#             count = dfs(i + 1)
#             if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
#                 count += dfs(i + 2)
#             memo[i] = count
#             return count
            
#         res = dfs(0)
#         return res