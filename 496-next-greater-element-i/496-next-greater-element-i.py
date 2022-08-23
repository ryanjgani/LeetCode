class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        
        hmap = {}
        stack = []
        for i, n in enumerate(nums1):
            hmap[n] = i
            
        for n in nums2:
            while stack and n > stack[-1]:
                res[hmap[stack.pop()]] = n
                
            if (not stack or stack[-1] > n) and n in hmap:
                stack.append(n)
        return res
        
        # for i, n in enumerate(nums2):
        #     if n in hmap:
        #         for j in range(i + 1, len(nums2)):
        #             if n < nums2[j]:
        #                 res[hmap[n]] = nums2[j]
        #                 break
        # return res
    