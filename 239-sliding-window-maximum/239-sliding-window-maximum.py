class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        deque = []
        for r in range(len(nums)):
            while deque and deque[-1] < nums[r]:
                deque.pop()
            deque.append(nums[r])
            if r + 1 >= k:
                res.append(deque[0])
                if nums[l] == deque[0]:
                    deque.pop(0)
                l += 1
        return res
                