class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        
        def dfs(idx):
            if sum(comb) == target:
                res.append(comb[:])
                return
            if sum(comb) > target:
                return # backtrack
            
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(i)
                comb.pop()
        dfs(0)
        return res