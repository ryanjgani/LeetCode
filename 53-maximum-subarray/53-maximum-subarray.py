class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            curSum += n
            maxSum = max(maxSum, curSum)
            if curSum < 0:
                curSum = 0
        return maxSum