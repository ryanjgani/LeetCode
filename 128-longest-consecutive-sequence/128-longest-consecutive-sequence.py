class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0
        for n in nums:
            # if start
            if n - 1 not in numbers:
                length = 0
                while n + length in numbers:
                    length += 1
                res = max(res, length)
        return res