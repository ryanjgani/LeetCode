class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # l, r = 0, len(nums) - 1
        
        # Bucket Sort
        bucket = [0] * 3
        for n in nums:
            bucket[n] += 1
        idx = 0
        for i in range(len(nums)):
            while bucket[idx] == 0:
                idx += 1
            nums[i] = idx
            bucket[idx] -= 1
            
        
        
        
                