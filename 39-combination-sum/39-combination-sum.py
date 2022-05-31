class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        def dfs(i):
            print(candidates[i])
            if sum(comb) >= target or i >= len(candidates):
                print(">>>", comb)
                if sum(comb) == target:
                    print("target", comb)
                    res.append(comb[:])
                return
            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                dfs(j)
                comb.pop()



        dfs(0)
        return res
        