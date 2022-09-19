class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(i, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or i >= len(candidates):
                return
            dfs(i, comb + [candidates[i]], total + candidates[i])
            dfs(i + 1, comb, total)
    
        def dfs_long(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target:
                return
            for i in range(idx, len(candidates)):
                if total + candidates[i] > target: break
                dfs(i, comb + [candidates[i]], total + candidates[i])
        dfs(0, [], 0)
        return res
            