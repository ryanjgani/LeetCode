class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                if mid % 2 == 0: 
                    r = mid - 2
                else:
                    l = mid + 1
            elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                if mid % 2:
                    r = mid - 1
                else:
                    l = mid + 2
                
            else:
                return nums[mid]
