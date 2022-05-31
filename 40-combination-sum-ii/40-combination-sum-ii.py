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
                idx = j + skipvalue
                if idx == len(candidates):
                    break
                comb.append(candidates[idx])
                dfs(idx + 1)
                comb.pop()
                while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                    skipvalue += 1
                    idx += 1
        dfs(0)
        return res