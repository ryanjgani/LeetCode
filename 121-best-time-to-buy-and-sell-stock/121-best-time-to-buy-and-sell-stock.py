class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = 0
        for i in range(len(prices)):
            current = prices[i] - prices[l]
            if current < 0:
                l = i
            else:
                res = max(res, current)
        return res