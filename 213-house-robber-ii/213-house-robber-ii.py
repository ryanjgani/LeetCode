class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob1(nums):
            if not len(nums): return 0
            res = first = nums[0]
            sec = 0
            for i in range(1, len(nums)):
                res = max(nums[i] + sec, first)
                sec = first
                first = res
            return res
        return max(rob1(nums[:-1]), rob1(nums[1:]))
        