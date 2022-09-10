class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        prev = 0
        if nums[0] != 0:
            return 0
        for i, n in enumerate(nums):
            if i > 0 and prev != n - 1:
                return n - 1
            prev = n
        return len(nums)
        
            