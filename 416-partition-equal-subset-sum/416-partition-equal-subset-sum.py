class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) / 2
        dp = {}
        
        def dfs(i, comb):
            if (i, comb) in dp:
                return dp[(i, comb)]
            if i == len(nums):
                return comb == target
            dp[(i, comb)] = dfs(i + 1, comb + nums[i]) or dfs(i + 1, comb)
            return dp[(i, comb)]
        return dfs(0, 0)
            