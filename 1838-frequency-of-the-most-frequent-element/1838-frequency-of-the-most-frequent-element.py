class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        wlen = total = res = 0
        for r in range(len(nums)):
            total += nums[r]
            wlen += 1
            while nums[r] * wlen > total + k:
                total -= nums[l]
                l += 1
                wlen -= 1
            res = max(res, wlen)
            r += 1
        return res
                