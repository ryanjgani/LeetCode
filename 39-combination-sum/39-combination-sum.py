class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        def dfs(idx, total):
            if total > target: return
            if total == target:
                res.append(comb[:])
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(i, total + candidates[i])
                comb.pop()
        dfs(0, 0)
        return res