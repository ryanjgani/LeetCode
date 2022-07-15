class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # def dfs(i, comb, total):
        #     if total > target: return
        #     if total == target:
        #         res.append(comb[:])
                
        
        
        
        
        
        res = []
        candidates.sort()
        def dfs(idx, comb, total):
            if total > target: return
            if total == target:
                res.append(comb[:])
                return
            for i in range(idx, len(candidates)):
                dfs(i, comb + [candidates[i]], total + candidates[i])
        dfs(0, [], 0)
        return res