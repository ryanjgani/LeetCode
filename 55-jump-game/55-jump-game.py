class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Greedy O(n)
        goalpost = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] >= goalpost - i:
                goalpost = i
        return True if goalpost == 0 else False
        
        # top down memoization O(n^2) - TLE
        cache = {}
        def cache_dfs(idx):
            if idx in cache:
                return cache[idx]
            if idx == len(nums) - 1:
                return True
            if idx >= len(nums):
                return False
            
            for i in range(1, nums[idx] + 1):
                if cache_dfs(idx + i):
                    cache[idx] = True
                    return True
            cache[idx] = False
            return False
        return cache_dfs(0)
        
        
        
        
        # Brute force approach O(n ^ n) - TLE
        def brute_dfs(idx):
            if idx == len(nums) - 1:
                return True
            if idx >= len(nums):
                return False
            
            for i in range(1, nums[idx] + 1):
                if brute_dfs(idx + i):
                    return True
            return False
        return brute_dfs(0)