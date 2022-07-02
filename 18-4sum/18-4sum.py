class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def threeSum(nums, target):
            res = []
            nums.sort()
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]: continue
                l, r = i + 1, len(nums) - 1
                while l < r:
                    total = nums[l] + nums[r] + nums[i]
                    if total == target:
                        res.append([nums[i], nums[l], nums[r]])
                        l += 1
                        while nums[l] == nums[l - 1] and l < r:
                            l += 1
                    if total < target:
                        l += 1
                    else:
                        r -= 1
            return res
        
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            three = threeSum(nums[i + 1:], target - nums[i])
            for t in three:
                res.append([nums[i]] + t)
            
            
            
        return res
                    
                