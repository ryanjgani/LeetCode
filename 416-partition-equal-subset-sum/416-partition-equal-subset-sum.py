class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#       bottom up
        target = sum(nums) / 2
        if sum(nums) % 2: return False
        
        dp = set()
        dp.add(0)
        for n in nums:
            temp = set()
            for i in dp:
                temp.add(i)
                temp.add(i + n)
            dp = temp
        return True if target in dp else False
        
        
        
        
#       Top down memoization
#         dp = {}
#         def dfs(i, rem):
#             if (i, rem) in dp:
#                 return dp[(i, rem)]
            
#             if rem == 0:
#                 return True
#             if rem < 0 or i >= len(nums):
#                 return False

#             dp[(i, rem)] = dfs(i + 1, rem - nums[i]) or dfs(i + 1, rem)
#             return dp[(i, rem)]
        
#         target = sum(nums) / 2
#         return False if sum(nums) % 2 else dfs(0, target)
