class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        hmap = {}
        for x, y in points:
            d = (x ** 2) + (y ** 2)
            heap.append([d, x, y])
        heapq.heapify(heap)
        res = []
        while k:
            d, x, y = heappop(heap)
            res.append([x, y])
            k -=1 
        return res