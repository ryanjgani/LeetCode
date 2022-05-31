class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        candidates.sort()

        # Time: O(n*n^n)
        # Space: O(k) where k = target
        # def dfs(i):
        #     if sum(comb) >= target or i >= len(candidates):
        #         if sum(comb) == target:
        #             res.append(comb[:])
        #         return
        #     skipvalue = 0
        #     for j in range(i, len(candidates) - skipvalue):
        #         idx = j + skipvalue
        #         if idx == len(candidates):
        #             break
        #         comb.append(candidates[idx])
        #         dfs(idx + 1)
        #         comb.pop()
        #         while j + skipvalue + 1 < len(candidates) and candidates[j + skipvalue] == candidates[j + skipvalue + 1]:
        #             skipvalue += 1
        
        def dfs(i):
            if sum(comb) >= target or i >= len(candidates):
                if sum(comb) == target:
                    res.append(comb[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                comb.append(candidates[j])
                dfs(j + 1)
                comb.pop()
        
        
        dfs(0)
        return res