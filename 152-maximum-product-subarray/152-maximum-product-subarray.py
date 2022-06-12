class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # bottom up O(n)
        res = max(nums)
        curMax, curMin = 1, 1
        
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = curMax
            curMax = max(curMax * n, curMin * n, n)
            curMin = min(temp * n, curMin * n, n)
            res = max(res, curMax)
        return res
        
        
        