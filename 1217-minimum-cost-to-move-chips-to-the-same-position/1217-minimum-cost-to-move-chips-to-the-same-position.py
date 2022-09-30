class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds, evens = 0, 0
        for p in position:
            if p % 2: evens += 1
            else: odds += 1
        if not evens or not odds: return 0
        return min(evens, odds)