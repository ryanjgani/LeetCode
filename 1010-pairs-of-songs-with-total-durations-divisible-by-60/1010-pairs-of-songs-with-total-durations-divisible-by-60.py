class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        res = 0
        rem = {}
        for t in time:
            if t % 60 == 0 and 0 in rem:
                res += rem[0]
            elif 60 - (t % 60) in rem:
                res += rem[60 - (t % 60)]
            rem[t % 60] = rem.get(t % 60, 0) + 1
        return res
    