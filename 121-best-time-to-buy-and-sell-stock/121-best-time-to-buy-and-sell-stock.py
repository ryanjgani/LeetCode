class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curMax = 0
        l = 0
        for r in range(len(prices)):
            curMax = prices[r] - prices[l]
            res = max(res, curMax)
            if curMax < 0:
                l = r
        return res
            