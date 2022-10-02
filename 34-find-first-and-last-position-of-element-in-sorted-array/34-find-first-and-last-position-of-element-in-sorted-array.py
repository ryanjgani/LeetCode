class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] == nums[r] == target:
                return [l, r]
            if nums[l] == target:
                r -= 1
            elif nums[r] == target:
                l += 1
            else:
                r -= 1
                l += 1
        return [-1, -1]
            