class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, total, comb, prev):
            if total == target:
                res.append(comb[:])
                return
            if total > target or i >= len(candidates):
                return  # backtrack
            if candidates[i] != prev:
                dfs(i + 1, total + candidates[i], comb + [candidates[i]], prev)
            dfs(i + 1, total, comb, candidates[i])
        dfs(0, 0, [], 0)
        return res
        