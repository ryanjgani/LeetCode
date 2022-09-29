class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        maxLeft, maxRight = [], []
        prev = 0
        for h in height:
            maxLeft.append(prev)
            prev = max(prev, h)
        prev = 0
        for i in range(len(height) - 1, -1, -1):
            maxRight.append(prev)
            prev = max(prev, height[i])
        maxRight = maxRight[::-1]
        
        for i, h in enumerate(height):
            count = min(maxLeft[i], maxRight[i]) - h
            if count > 0: res += count
        return res
            
            