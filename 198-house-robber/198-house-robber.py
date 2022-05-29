class Solution:
    def rob(self, nums: List[int]) -> int:

        # bottom up with hashmap - Kevin Naughton
#         if not nums:
#             return 0
#         if len(nums) == 1:
#             return nums[0]
#         if len(nums) == 2:
#             return max(nums[0], nums[1])
        
#         dp = {}
#         dp[0] = nums[0]
#         dp[1] = max(nums[0], nums[1])
#         for i in range(2, len(nums)):
#             dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
#         return dp[len(nums) - 1]
    
        # bottom up without hashmap - Neetcode
        # since we only use dp[i], dp[i - 1], and dp[i - 2], we don't need a hashmap
        # and just store three variables: temp, rob1, rob2
        
        
        rob1 = rob2 = 0
        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2