class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # linear time and constant space
        for i in range(len(nums)):
            if nums[i] <= 0: nums[i] = len(nums) + 2
        for i, n in enumerate(nums):
            if 0 < abs(n) <= len(nums) and nums[abs(n) - 1] >= 0:
                nums[abs(n) - 1] *= -1
        for i in range(1, len(nums) + 1):
            if nums[i - 1] >= 0: return i
        return len(nums) + 1
        
        
        
        # linear time and space
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums: return i
        
        # nlogn time, linear space
        nums = list(set(nums))
        nums.sort()
        res = 1
        for n in nums:
            if n <= 0: continue
            if res != n: return res
            res += 1
        return res
        
        