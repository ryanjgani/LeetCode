class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = res = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] <= 0:
                l = r
            else:
                res = max(res, prices[r] - prices[l])
        return res