class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        comb = []
        
        def dfs(i, total):
            if total == target:
                res.append(comb[:])
                return
            if i >= len(candidates) or total > target:
                return
            comb.append(candidates[i])
            dfs(i, total + candidates[i])
            comb.pop()
            dfs(i + 1, total)
    
        # def dfs_long(idx, comb, total):
        #     if total == target:
        #         res.append(comb[:])
        #         return
        #     if total > target:
        #         return
        #     for i in range(idx, len(candidates)):
        #         if total + candidates[i] > target: break
        #         dfs(i, comb + [candidates[i]], total + candidates[i])
        dfs(0, 0)
        return res
            