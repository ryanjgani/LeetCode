class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target: return mid
            
            if nums[mid] >= nums[l]:
                if target > nums[mid]: l = mid + 1
                else:
                    if target < nums[l]: l = mid + 1
                    else: r = mid - 1
            else:
                if target < nums[mid]: r = mid - 1
                else:
                    if target <= nums[r]: l = mid + 1
                    else: r = mid - 1
        return - 1
            
            # if mid on the left portion and target > mid: l = mid + 1
            # if mid on the left portion and target < mid: target can be on left or right
            
            # if mid on right and target < mid: r = mid - 1
            # if mid on right and target > mid: target can be on left or right
            #   if target <= r: l = mid + 1
            #   else: r = mid - 1
            