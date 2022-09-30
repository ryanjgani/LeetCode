class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # nums = list(set(nums))
        # nums.sort()
        # res = 1
        # for n in nums:
        #     if n <= 0: continue
        #     if res != n: return res
        #     res += 1
        # return res
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums: return i
        
        