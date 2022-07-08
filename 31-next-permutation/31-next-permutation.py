class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        strict = -1
        decrease = True
        for i in range(len(nums) - 1, -1, -1):
            if i < len(nums) - 1 and nums[i] < nums[i + 1]:
                decrease = False
                break
        if not decrease:
            for j in range(len(nums) - 1, -1, -1):
                if nums[j] > nums[i]:
                    break
            nums[i], nums[j] = nums[j], nums[i]
        
        l, r = i + 1, len(nums) - 1
        if decrease: l = 0
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
