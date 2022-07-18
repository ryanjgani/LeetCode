class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        hmap = {}
        for x, y in points:
            d = (x ** 2) + (y ** 2)
            distance.append(d)
            if d in hmap: hmap[d].append([x, y])
            else: hmap[d] = [[x, y]]
        heap = []
        heapq.heapify(heap)
        for d in distance:
            heappush(heap, -1 * d)
        while len(heap) > k:
            heappop(heap)
        res = []
        prev = None
        while heap:
            top = -1 * heappop(heap)
            if prev and top == prev: continue
            prev = top
            res.extend(hmap[top])
        return res