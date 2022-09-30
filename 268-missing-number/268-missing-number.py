class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0
        count = 0
        for i in range(1, len(nums) + 1):
            xor ^= i
        
        for n in nums:
            count ^= n
        return xor^count