class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        
        
        for i, n in enumerate(nums1):
            for j, m in enumerate(nums2):
                if n == m:
                    temp = -1
                    for k in range(j + 1, len(nums2)):
                        if m < nums2[k]:
                            temp = nums2[k]
                            break
                    res.append(temp)
                    break
        return res
    