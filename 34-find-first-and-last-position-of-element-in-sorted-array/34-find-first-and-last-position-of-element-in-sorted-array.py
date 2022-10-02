class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # O(log(m+n)) time
        def helper(pos):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] < target: l = mid + 1
                elif nums[mid] > target: r = mid - 1
                else:
                    i = mid
                    if pos == "start":
                        r = mid - 1
                    else:
                        l = mid + 1
            return i
        return [helper('start'), helper('end')]
        
        # O(n/2) time
        while l <= r:
            if nums[l] == nums[r] == target:
                return [l, r]
            if nums[l] == target:
                r -= 1
            elif nums[r] == target:
                l += 1
            else:
                r -= 1
                l += 1
        return [-1, -1]
            