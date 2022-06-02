class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        dp[0] = 0
        for i in range(1, amount + 1):
            minNum = 99999
            for n in coins:
                if i - n >= 0:
                    temp = 1 + dp[i - n]
                    minNum = min(temp, minNum)
            dp[i] = minNum
        if dp[amount] == 99999:
            return -1
        return dp[amount]