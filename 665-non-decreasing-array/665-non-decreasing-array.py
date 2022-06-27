class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        changed = False
        
        for l in range(len(nums) - 1):
            r = l + 1
            if nums[r] >= nums[l]:
                prev = nums[l]
                continue
            if changed:
                return False
            changed = True
            if l == 0 or nums[r] >= nums[l - 1]:
                nums[l] = nums[r]
            else:
                nums[r] = nums[l]
        return True
        
            
            