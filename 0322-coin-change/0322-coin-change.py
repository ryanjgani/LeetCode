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
        
        # top down masih gabisa
        dp = {}
        dp[0] = 0
        def dfs(i, rem):
            if rem in dp: return dp[rem]
            if rem < 0 or i == len(coins):
                return float('inf')
            withcoin = 1 + dfs(i, rem - coins[i])
            withoutcoin = dfs(i + 1, rem)
            dp[rem] = min(withcoin, withoutcoin)
            return dp[rem]
        
        res = dfs(0, amount)
        return res if res < float('inf') else -1