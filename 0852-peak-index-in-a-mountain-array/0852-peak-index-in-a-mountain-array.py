class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if mid > 0 and arr[mid] >= arr[mid - 1] and arr[mid] <= arr[mid + 1]:
                l = mid
            elif mid > 0 and arr[mid] <= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                r = mid
            else:
                return mid
            
        
        