class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prev = 1
        pre = [1]
        for i in range(len(nums) - 1):
            pre.append(prev * nums[i])
            prev *= nums[i]
        post = [1]
        prev = 1
        for i in range(len(nums) - 1, 0, -1):
            post.append(prev * nums[i])
            prev *= nums[i]
        post = post[::-1]
        for i in range(len(pre)):
            pre[i] *= post[i]
        return pre
        