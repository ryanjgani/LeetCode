class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time: O(n^k) where k = target
        # Space: O(k) -> max space of comb, not counting the output array res
        
        res = []
        comb = []
        
        def dfs(i):
            if sum(comb) >= target or i >= len(candidates):
                if sum(comb) == target:
                    res.append(comb[:])
                return
            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                dfs(j)
                comb.pop()

        dfs(0)
        return res
        