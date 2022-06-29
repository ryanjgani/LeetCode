class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # O(log(max(p)) * p)
        res = 0
        
        # this takes O(p) time
        def helper(speed):
            count = 0
            for p in piles:
                count += math.ceil(p / speed)
            return count <= h
        
        # this binary search takes O(log(max(p))) time
        l, r = 1, max(piles) + 1
        while l <= r:
            mid = l + (r - l) // 2
            if helper(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
