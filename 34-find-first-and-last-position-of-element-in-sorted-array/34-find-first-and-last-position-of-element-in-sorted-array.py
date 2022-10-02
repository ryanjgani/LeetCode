class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        res = [-1, -1]
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            if nums[mid] == target:
                p = mid
                while l < p:
                    m = l + (p - l) // 2
                    if nums[m] < target:
                        l = m + 1
                    else: p = m
                res[0] = p
                p = mid
                while p < r:
                    add = 1 if (r - p) % 2 else 0
                    m = add + p + (r - p) // 2
                    if nums[m] > target:
                        r = m - 1
                    else: p = m
                res[1] = r
                break
        return res
        
        
        
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
            