class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy O(n)
        
        if sum(gas) < sum(cost):
            return -1
        
        for i in range(len(gas)):
            gas[i] = gas[i] - cost[i]
        
        total = 0
        for i, n in enumerate(gas):
            if total == 0 and total + n >= 0:
                res = i
            total += n
            if total < 0:
                total = 0
        return res