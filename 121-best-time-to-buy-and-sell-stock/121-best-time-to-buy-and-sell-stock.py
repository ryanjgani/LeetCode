class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        cp, mp = 0, 0
        for r in range(1, len(prices)):
            cp = prices[r] - prices[l]
            if cp < 0:
                cp = 0
                l = r
                
            mp = max(mp, cp)
        return mp