class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up approach
#         dp = {}
#         dp[0] = 0
        
#         for n in range(1, amount + 1):
#             minNum = 99999
#             for c in coins:
#                 if n - c >= 0:
#                     temp = 1 + dp[n - c]
#                     minNum = min(minNum, temp)
#             dp[n] = minNum
#         return -1 if dp[amount] == 99999 else dp[amount]

        # top down memoization approach
        dp = {}
        
        def dfs(rem):
            if rem in dp: return dp[rem]
            if rem == 0: return 0
            if rem < 0 : return float("inf")
            dp[rem] = min([1 + dfs(rem - c) for c in coins])
            return dp[rem]
            
        res = dfs(amount)
        return res if res < float('inf') else -1
