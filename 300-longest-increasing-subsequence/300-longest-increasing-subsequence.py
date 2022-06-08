class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # bottom up dp
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        
        # Top down memoization
#         def helper(prev_i, i):
#             if i == len(nums): return 0
#             if memo[prev_i + 1] >= 0:
#                 return memo[prev_i + 1]
#             add, notAdd = 0, 0
#             if prev_i < 0 or nums[i] > nums[prev_i]:
#                 add = 1 + helper(i, i + 1)
#             notAdd = helper(prev_i, i + 1)
#             memo[prev_i + 1] = max(add, notAdd)
#             return memo[prev_i + 1]
			
#         N = len(nums)
#         memo = [-1 for _ in range(N)]
#         return helper(-1, 0)