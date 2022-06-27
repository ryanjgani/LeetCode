class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        
        prev = float('-inf')
        for l in range(len(nums) - 1):
            r = l + 1
            if nums[r] >= nums[l]:
                prev = nums[l]
                continue
            if changed:
                return False
            changed = True
            if nums[r] < prev:
                nums[r] = nums[l]
            else:
                nums[l] = nums[r]
            prev = nums[l]
        return True
        
            
            