class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        l = 0
        for r in range(len(heights)):
            idx = r
            while stack and stack[-1][0] > heights[r]:
                h, idx = stack.pop()
                area = (r - idx) * h
                res = max(res, area)
            stack.append((heights[r], idx))
            
        while stack:
            h, idx = stack.pop()
            area = (len(heights) - idx) * h
            res = max(res, area)
        return res
        