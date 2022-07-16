class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}       
        res = float('inf')
        
        def dfs(rem):
            if rem in dp: return dp[rem]
            if rem == 0: return 0
            if rem < 0: return float('inf')
            
            dp[rem] = min([1 + dfs(rem - c) for c in coins])
            return dp[rem]
            
        res = dfs(amount)
        return res if res < float('inf') else -1