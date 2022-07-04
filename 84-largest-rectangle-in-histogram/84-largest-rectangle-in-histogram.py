class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # monotonic increasing stack
        stack = []
        res = 0
        
        for i, h in enumerate(heights):
            idx = i
            while stack and stack[-1][1] > h:
                top = stack.pop()
                curArea = (i - top[0]) * top[1]
                res = max(res, curArea)
                idx = top[0]
            stack.append([idx, h])
            
        while stack:
            top = stack.pop()
            curArea = (len(heights) - top[0]) * top[1]
            res = max(res, curArea)
        return res
        
#         l = 0
#         res = 0
#         prev = float('inf')
        
#         for r, h in enumerate(heights):
#             # drop
#             if r > 0 and heights[r] < heights[r - 1]:
#                 tempL = l
#                 while heights[l] < heights[r]:
#                     l += 1
#                 while l < r:
#                     curArea = (r - l) * min(heights[l:r])
#                     res = max(res, curArea)
#                     l += 1
#                 l = tempL
#         r += 1
#         while l < r:
#             curArea = (r - l) * min(heights[l:])
#             res = max(res, curArea)
#             l += 1
#         return res