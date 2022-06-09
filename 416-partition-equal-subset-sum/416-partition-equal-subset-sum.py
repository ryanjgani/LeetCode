class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom up
        if sum(nums) % 2: return False
        dp = set()
        dp.add(0)
        target = sum(nums) / 2
        
        for i in range(len(nums) - 1, -1, -1):
            temp = set()
            for n in dp:
                temp.add(n + nums[i])
                temp.add(n)
            dp = temp
        return True if target in dp else False
        
        
        # Brute force O(2^n)
        # target = sum(nums) // 2
        # if target != sum(nums) / 2: return False
        # comb = []
        # def dfs(i):
        #     if sum(comb) == target:
        #         return True
        #     if sum(comb) > target or i >= len(nums):
        #         return False
        #     comb.append(nums[i])
        #     add = dfs(i + 1)
        #     comb.pop()
        #     not_add = dfs(i + 1)
        #     return add or not_add
        # return dfs(0)