class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        prev = nums[0]
        for n in nums[1:]:
            tmp = max(n, prev + n)
            prev = tmp
            res = max(res, tmp)
        return res