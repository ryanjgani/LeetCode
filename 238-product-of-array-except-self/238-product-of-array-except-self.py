class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums[:]
        for i in range(len(nums)):
            if i == 0:
                continue
            res[i] *= res[i - 1]
        res = [1] + res[:-1]
        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res