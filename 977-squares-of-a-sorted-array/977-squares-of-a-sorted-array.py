class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        res = []
        for _ in range(len(nums)):
            if abs(nums[l]) > abs(nums[r]):
                res.append(abs(nums[l])**2)
                l += 1
            else:
                res.append(abs(nums[r])**2)
                r -= 1
        return res[::-1]