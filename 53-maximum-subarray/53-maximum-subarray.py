class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curSum = 0
        dp = [nums[0]]
        for n in nums[1:]:
            tmp = max(n, dp[-1] + n)
            dp.append(tmp)
        return max(dp)