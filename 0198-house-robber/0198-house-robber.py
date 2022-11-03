class Solution:
    def rob(self, nums: List[int]) -> int:
        prev = 0
        prev2 = 0
        for n in nums:
            temp = max(n + prev2, prev)
            prev2 = prev
            prev = temp
        return prev