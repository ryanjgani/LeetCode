class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2: return False
        target = sum(nums) / 2
        dp = set()
        dp.add(0)
        
        for n in nums:
            temp = dp.copy()
            for d in dp:
                temp.add(n + d)
            dp = temp
        return target in dp
        
        
        
        
        
        # def dfs(i, comb):
        #     if i in dp:
        #         return dp[(i, comb)]
        #     if i == len(nums):
        #         return comb == target
        #     dp[(i, comb)] = dfs(i + 1, comb + nums[i]) or dfs(i + 1, comb)
        #     return dp[(i, comb)]
        # return dfs(0, 0)
            