class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for n in stones:
            heappush(heap, -1 * n)
        print(heap)
        
        while len(heap) > 1:
            y = -1 * heappop(heap)
            x = -1 * heappop(heap)
            if x == y: continue
            else: y = y - x
            heappush(heap, -1 * y)
        return -1 * heap[0] if len(heap) else 0
                
            
            