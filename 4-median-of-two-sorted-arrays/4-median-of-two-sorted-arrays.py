class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        p = q = 0
        while p < len(nums1) and q < len(nums2):
            if nums1[p] < nums2[q]:
                arr.append(nums1[p])
                p += 1
            else:
                arr.append(nums2[q])
                q += 1
        if p < len(nums1): arr.extend(nums1[p:])
        if q < len(nums2): arr.extend(nums2[q:])
         
        mid = len(arr) // 2
        if len(arr) % 2:
            return arr[mid]
        else:
            return (arr[mid] + arr[mid - 1]) / 2