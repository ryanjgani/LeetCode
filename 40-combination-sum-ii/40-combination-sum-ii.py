class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        comb = []
        
        candidates.sort()
        print("**")
        
        def dfs(idx, target, nums):
            print("target", target)
            if target == 0:
                print('here')
                res.append(comb[:])
                return
            
            if target < 0:
                return # backtrack
            
            print(comb)
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                
                comb.append(nums[i])
                dfs(i + 1, target - nums[i], nums)
                comb.pop()
        
        dfs(0, target, candidates)
        return res
    
    
    

        # Time: O(n*n^n)
        # Space: O(k) where k = target
        def dfs_long(i):
            if sum(comb) >= target or i >= len(candidates):
                if sum(comb) == target:
                    res.append(comb[:])
                return
            for j in range(i, len(candidates)):
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                comb.append(candidates[j])
                dfs(j + 1)
                comb.pop()
        
        
