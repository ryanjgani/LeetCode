class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        candidates.sort()
        print(candidates)
        def dfs(i):
            if sum(comb) >= target or i >= len(candidates):
                if sum(comb) == target:
                    res.append(comb[:])
                return
            skipvalue = 0
            for j in range(i, len(candidates) - skipvalue):
                if j + skipvalue == len(candidates):
                    break
                print(j + skipvalue, candidates[j + skipvalue])
                comb.append(candidates[j + skipvalue])
                print(comb)
                dfs(j + skipvalue + 1)
                comb.pop()
                while j + skipvalue + 1 < len(candidates) and candidates[j + skipvalue] == candidates[j + skipvalue + 1]:
                    print("here", j + skipvalue, i)
                    skipvalue += 1
                    print("j becomes", j + skipvalue)
        dfs(0)
        print("***", res)
        return res