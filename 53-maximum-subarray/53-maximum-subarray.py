class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = 0
        for n in nums:
            curSum += n
            res = max(res, curSum)
            if curSum < 0:
                curSum = 0
        return res