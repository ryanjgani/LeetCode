class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1 , -1):
            j = i + 1
            while j < len(nums):
                if nums[i] <nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                j += 1
        return max(dp)
        
        def dfs(i, prev, count):
            # if count in dp:
            #     return dp[count]
            if i == len(nums):
                return count
            temp = 1
            for j in range(i, len(nums)):
                if nums[j] > prev:
                    temp = max(temp, dfs(j, nums[i], count + 1))
            return temp
                
                
#             if nums[i] > prev:
#                 temp = max(temp, dfs(i + 1, nums[i], count + 1))
#             dp[count] = temp
#             return temp
        # return dfs(0, float('-inf'), 0)
