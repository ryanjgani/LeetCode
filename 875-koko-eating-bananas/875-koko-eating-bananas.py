class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        res = 0
        def helper(speed):
            count = 0
            for p in piles:
                count += math.ceil(p / speed)
            return count <= h
        
        l, r = 1, max(piles) + 1
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
