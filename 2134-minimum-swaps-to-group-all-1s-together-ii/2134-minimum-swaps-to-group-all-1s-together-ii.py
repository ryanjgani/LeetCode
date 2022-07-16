class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        wlen = 0
        for n in nums:
            wlen += 1 if n == 1 else 0
        if not wlen: return 0
        count = [0] * 2
        res, l = len(nums), 0
        for i in range(len(nums)):
            count[nums[i]] += 1
            if i >= wlen - 1:
                res = min(count[0], res)
                count[nums[l]] -= 1
                l += 1
        i = 0
        while l < len(nums):
            count[nums[i]] += 1
            res = min(count[0], res)
            count[nums[l]] -= 1
            l += 1
            i += 1
        return res