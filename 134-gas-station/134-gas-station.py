class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        rem = [gas[i] - cost[i] for i in range(len(gas))]
        res = 0
        if sum(gas) - sum(cost) < 0: return -1
        cur = 0
        for i in range(len(gas)):
            cur += rem[i]
            if cur < 0:
                cur = 0
                res = i + 1
        return res
        