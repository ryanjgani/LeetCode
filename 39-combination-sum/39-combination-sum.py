class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(idx, rem):
            if rem == 0:
                res.append(comb[:])
            if rem < 0:
                return
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(i, rem - candidates[i])
                comb.pop()
        dfs(0, target)
        return res