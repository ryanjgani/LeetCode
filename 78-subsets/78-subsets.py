class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(i, comb):
            if i >= len(nums):
                res.append(comb[:])
                return
            dfs(i + 1, comb + [nums[i]])
            dfs(i + 1, comb)
        dfs(0, [])
        return res
        