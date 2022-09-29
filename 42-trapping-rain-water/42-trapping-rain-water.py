class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                prev = stack.pop()
                if stack:
                    minHeight = min(height[stack[-1]], h)
                    count = (minHeight - height[prev]) * (i - stack[-1] - 1)
                    if count > 0: res += count
            stack.append(i)
        return res
        # O(n) time and constant space using two pointers
        # res = 0
        # l, r = 0, len(height) - 1
        # maxLeft, maxRight = height[l], height[r]
        # while l < r:
        #     if height[l] < height[r]:
        #         count = maxLeft - height[l]
        #         maxLeft = max(maxLeft, height[l])
        #         l += 1
        #     else:
        #         count = maxRight - height[r]
        #         maxRight = max(maxRight, height[r])
        #         r -= 1
        #     if count > 0: res += count
        # return res
        
        # res = 0
        # maxLeft, maxRight = [], []
        # prev = 0
        # for h in height:
        #     maxLeft.append(prev)
        #     prev = max(prev, h)
        # prev = 0
        # for i in range(len(height) - 1, -1, -1):
        #     maxRight.append(prev)
        #     prev = max(prev, height[i])
        # maxRight = maxRight[::-1]
        # for i, h in enumerate(height):
        #     count = min(maxLeft[i], maxRight[i]) - h
        #     if count > 0: res += count
        # return res
            
            