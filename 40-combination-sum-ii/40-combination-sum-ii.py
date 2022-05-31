class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        candidates.sort()

        def dfs(i):
            if sum(comb) >= target or i >= len(candidates):
                if sum(comb) == target:
                    res.append(comb[:])
                return
            skipvalue = 0
            for j in range(i, len(candidates) - skipvalue):
                if j + skipvalue == len(candidates):
                    break
                comb.append(candidates[j + skipvalue])
                dfs(j + skipvalue + 1)
                comb.pop()
                while j + skipvalue + 1 < len(candidates) and candidates[j + skipvalue] == candidates[j + skipvalue + 1]:
                    skipvalue += 1
        dfs(0)
        return res