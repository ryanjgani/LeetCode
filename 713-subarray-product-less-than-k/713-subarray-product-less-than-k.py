class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        res = 0
        prod = 1
        l = 0
        r = 0
        if k < 1: return 0
        while r < len(nums):
            prod *= nums[r]
            
            while prod >= k and l <= r:
                print(l)
                prod /= nums[l]
                l += 1
            
            res += r - l + 1
            r += 1
        
        
        return res