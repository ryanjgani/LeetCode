class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        comb = []
        
        def dfs(idx, target):
            if target == 0 and len(comb) == k:
                res.append(comb[:])
                return
            if target < 0:
                return # backtrack
            for i in range(idx, 10):
                comb.append(i)
                dfs(i + 1, target - i)
                comb.pop()
        
        
        dfs(1, n)
        return res
        