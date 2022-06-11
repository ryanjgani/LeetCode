class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        def dfs(i, rem):
            if (i, rem) in dp:
                return dp[(i, rem)]
            
            if rem == 0:
                return True
            if rem < 0 or i >= len(nums):
                return False

            dp[(i, rem)] = dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)
            return dp[(i, rem)]
        
        target = sum(nums) / 2
        return False if sum(nums) % 2 else dfs(0, target)
