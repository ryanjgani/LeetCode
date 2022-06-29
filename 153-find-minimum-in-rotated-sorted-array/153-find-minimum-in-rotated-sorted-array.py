class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            print(nums[mid])
            if nums[l] <= nums[mid] and nums[r] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]        