class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # bottom up
        maxNum = float('inf')
        dp = {}
        dp[0] = 0
        
        for a in range(1, amount + 1):
            dp[a] = maxNum
            temp = dp[a]
            for c in coins:
                if a - c >= 0:
                    temp = min(1 + dp[a - c], temp)
            dp[a] = temp
        
        return dp[amount] if dp[amount] < maxNum else -1
        
        
        # top down
#         dp = {}
        
#         def dfs(rem):
#             if rem in dp: return dp[rem]
#             if rem == 0: return 0
#             if rem < 0: return float('inf')
            
#             dp[rem] = min([1 + dfs(rem - c) for c in coins])
#             return dp[rem]
        
#         res = dfs(amount)
#         return res if res < float('inf') else -1
        