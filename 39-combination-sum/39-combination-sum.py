class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        candidates.sort()
        
        def dfs(i, remaining):
            if remaining == 0:
                res.append(comb[:])
                return
            if i >= len(candidates) or remaining < 0:
                return # backtrack
            
            comb.append(candidates[i])
            dfs(i, remaining - candidates[i])
            comb.pop()
            dfs(i + 1, remaining)
        
    
    
    
        # Time: O(n^k) where k = target
        # Space: O(k) -> max space of comb, not counting the output array res
        def dfs_long(idx):
            if sum(comb) == target:
                res.append(comb[:])
                return
            if sum(comb) > target:
                return # backtrack

            for i in range(idx, len(candidates)):
                if sum(comb) + candidates[i] > target:
                    break
                comb.append(candidates[i])
                dfs(i)
                comb.pop()
        dfs(0, target)
        return res