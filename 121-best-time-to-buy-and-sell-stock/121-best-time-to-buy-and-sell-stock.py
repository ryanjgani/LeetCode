class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0
        for i in range(1, len(prices)):
            cp = prices[i] - prices[l]
            maxProfit = max(maxProfit, cp)
            if cp < 0:
                l = i
        return maxProfit
            
            