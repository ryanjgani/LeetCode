class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up approach from the last index
        LIS = [0] * len(nums)
        LIS[len(nums) - 1] = 1
        for i in range(len(nums) - 2, -1, -1):
            LIS[i] = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)