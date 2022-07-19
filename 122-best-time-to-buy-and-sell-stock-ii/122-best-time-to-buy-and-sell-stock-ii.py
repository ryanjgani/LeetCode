class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(len(prices)):
            if prices[r] - prices[l] > 0:
                res += prices[r] - prices[l]
            l = r
        return res