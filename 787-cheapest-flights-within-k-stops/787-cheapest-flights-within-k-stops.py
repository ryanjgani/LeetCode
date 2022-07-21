class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        dp = {}
        for s, d, p in flights:
            if s in dp:
                dp[s].append((d, p))
            else:
                dp[s] = [(d, p)]
                
        queue = [(src, 0, -1)]
        
        while queue:
            pos, cost, step = queue.pop(0)
            if pos == dst or step == k or pos not in dp: continue
            for dest, price in dp[pos]:
                if cost + price < prices[dest]:
                    prices[dest] = cost + price
                    queue.append((dest, cost + price, step + 1))

        # while k + 1:
        #     n = len(queue)
        #     temp = prices[:]
        #     for s, d, p in flights:
        #         temp[d] = min(temp[d], prices[s] + p)
        #     prices = temp
        #     k -= 1
        return prices[dst] if prices[dst] < float('inf') else -1
        
        
        
        