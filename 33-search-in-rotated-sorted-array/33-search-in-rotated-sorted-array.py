class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] >= nums[l] and nums[mid] >= nums[r]:
                l = mid + 1
            else:
                r = mid
        l1, r1 = 0, l - 1
        l2, r2 = l, len(nums) - 1
        print(l)
        while l1 <= r1:
            mid = l1 + (r1 - l1) // 2
            if target > nums[mid]:
                l1 = mid + 1
            elif target < nums[mid]:
                r1 = mid - 1
            else:
                return mid

        while l2 <= r2:
            mid = l2 + (r2 - l2) // 2
            if target > nums[mid]:
                l2 = mid + 1
            elif target < nums[mid]:
                r2 = mid - 1
            else:
                return mid
        return -1
        
                