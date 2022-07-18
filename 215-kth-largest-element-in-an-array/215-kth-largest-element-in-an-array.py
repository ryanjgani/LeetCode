class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap, -1 * n)
        while k - 1:
            heappop(heap)
            k -= 1
        return heap[0] * -1