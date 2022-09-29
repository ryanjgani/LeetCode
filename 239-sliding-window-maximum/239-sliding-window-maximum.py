class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        stack = []
        l = 0
        for r in range(len(nums)):
            while stack and stack[-1] < nums[r]:
                stack.pop()
            stack.append(nums[r])
            if r - l + 1 == k:
                res.append(stack[0])
                if stack[0] == nums[l]:
                    stack.pop(0)
                l += 1
        return res
            