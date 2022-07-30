class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur = res = 0
        l = 0
        for r in range(1, len(prices)):
            cur = prices[r] - prices[l]
            if cur < 0:
                cur = 0
            res += cur
            l += 1
        return res
            