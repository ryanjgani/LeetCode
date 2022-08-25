class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        for i in range(len(nums)):
            nums[i] *= -1
        heapify(nums)
        print(nums)
        while k:
            res = heappop(nums)
            k -= 1
        return res * -1