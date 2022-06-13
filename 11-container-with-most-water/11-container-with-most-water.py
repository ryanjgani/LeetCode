class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            curArea = min(height[l], height[r])* (r - l)
            res = max(res, curArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res