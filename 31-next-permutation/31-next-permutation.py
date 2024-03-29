class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        prev = 0
        for i in range(len(nums) - 1, -2, -1):
            if i == -1: break
            if i < len(nums) - 1 and nums[i] < prev:
                break
            prev = nums[i]
        if i >= 0:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        