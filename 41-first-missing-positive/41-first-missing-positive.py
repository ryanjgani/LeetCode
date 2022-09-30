class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        i = 0
        while i < len(nums) and nums[i] <= 0:
            i += 1
        res = 1
            
        for n in nums[i:]:
            if res != n: return res
            res += 1
        return res
        