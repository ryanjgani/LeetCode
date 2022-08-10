class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        memo = {}
        @lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            temp = 0
            for i in range(l, r + 1):
                temp = max(temp, dfs(i + 1, r) + dfs(l, i - 1) + nums[l - 1] * nums[i] * nums[r + 1])
            memo[(l, r)] = temp
            return temp
        return dfs(1, len(nums) - 2)
        
        
        
        
        
#         def dfs(arr, total):
#             if (tuple(arr), total) in memo:
#                 return memo[(tuple(arr), total)]
#             if len(arr) == 2:
#                 return total
#             temp = 0
#             for i in range(1, len(arr) - 1):
#                 temp = max(temp, dfs(arr[:i] + arr[i + 1:], total + (arr[i - 1] * arr[i] * arr[i + 1])))
#             memo[tuple(arr), total] = temp
#             return temp
        
#         return dfs(arr, 0)
