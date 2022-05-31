class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            print(n)
            if n - 1 not in numSet:
                i = 1
                while n + i in numSet:
                    i += 1
                longest = max(longest, i)
        return longest
        