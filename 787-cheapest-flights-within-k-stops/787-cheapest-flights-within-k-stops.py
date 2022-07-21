class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        queue = [flights[0]]
        
        while k + 1:
            n = len(queue)
            temp = prices[:]
            for s, d, p in flights:
                temp[d] = min(temp[d], prices[s] + p)
            prices = temp
            k -= 1
        return prices[dst] if prices[dst] < float('inf') else -1
        
        
        
        