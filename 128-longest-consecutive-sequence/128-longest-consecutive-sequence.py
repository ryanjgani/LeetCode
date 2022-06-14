class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        res = 0
        for n in nums:
            # if start
            if n - 1 not in numbers:
                temp = 1
                for i in range(1, len(nums)):
                    if n + i not in numbers:
                        break
                    temp += 1
                res = max(res, temp)
        return res