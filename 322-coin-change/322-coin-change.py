class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        
        for n in range(1, amount + 1):
            dp[n] = float('inf')
            for c in coins:
                if n - c >= 0:
                    dp[n] = min(dp[n], 1 + dp[n - c])
        return dp[amount] if dp[amount] < float('inf') else -1
        # def dfs(i, count, total):
        #     if total == amount:
        #         return count
        #     if total in dp: return total
        #     if total > amount or i >= len(coins):
        #         return float('inf')
        #     dp[total] = min(dfs(i, count + 1, total + coins[i]), dfs(i + 1, count, total))
        #     return dp[total]
        # res = dfs(0, 0, 0)
        # print(dp)
        # return res if res < float('inf') else -1