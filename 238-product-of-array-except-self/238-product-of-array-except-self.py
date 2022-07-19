class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        pre = [1]
        for i in range(len(nums) - 1):
            pre.append(prev * nums[i])
            prev *= nums[i]
        prev = 1
        for i in range(len(nums) - 2, -1, -1):
            pre[i] *= prev * nums[i + 1]
            prev *= nums[i + 1]
        return pre        