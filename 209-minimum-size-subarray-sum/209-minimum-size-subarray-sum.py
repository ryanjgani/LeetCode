class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l = 0
        count = 0
        for r in range(len(nums)):
            count += nums[r]
                
            while count >= target and l <= r:
                res = min(res, r - l + 1)
                count -= nums[l]
                l += 1
                
        return res if res < float('inf') else 0