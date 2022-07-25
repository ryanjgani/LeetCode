class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rem = [gas[i] - cost[i] for i in range(len(gas))]
        print(rem)
        if sum(gas) < sum(cost): return -1
        current = 0
        res = 0
        for i in range(len(rem)):
            current += rem[i]
            if current < 0:
                current = 0
                res = i + 1
        return res