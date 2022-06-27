class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1
        if len(nums) == 1: return True
        
        for i in range(len(nums) - 2, -1, -1):
            print(nums[i], i, target)
            if nums[i] >= target - i:
                target = i
        return target == 0