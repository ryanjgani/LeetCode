class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}
        dp[0] = 0
        for a in range(1, amount + 1):
            temp = float('inf')
            for c in coins:
                if a - c >= 0:
                    temp = min(temp, 1 + dp[a - c])
            dp[a] = temp
        return dp[amount] if dp[amount] < float('inf') else -1
        
        
        dp = {}
        dp[amount] = 0
        def dfs(i, total):
            if total in dp: return dp[total]
            if total == amount: return 0
            if total > amount or i == len(coins):
                return float('inf')
            withcoin = 1 + dfs(i, total + coins[i])
            withoutcoin = dfs(i + 1, total)
            dp[total] = min(withcoin, withoutcoin)
            return dp[total]
        
        res = dfs(0, 0)
        print(dp[0])
        return res if res < float('inf') else -1