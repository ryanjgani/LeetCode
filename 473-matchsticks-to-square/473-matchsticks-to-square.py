class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4:
            return False
        target = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)
        memo = {}
        
    
        def dfs(i, comb):
            if (i, tuple(comb)) in memo:
                return memo[(i, tuple(comb))]
            if i == len(matchsticks):
                return True
            temp = False
            for j in range(4):
                if comb[j] + matchsticks[i] <= target:
                    comb[j] += matchsticks[i]
                    if dfs(i + 1, comb):
                        temp = True
                        break
                    comb[j] -= matchsticks[i]
            memo[(i, tuple(comb))] = temp
            return temp
        return dfs(0, [0]*4)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# [5969561,8742425,2513572,3352059,9084275,2194427,1017540,2324577,6810719,8936380,7868365,2755770,9954463,9912280,4713511]
#         def dfs(i, comb, step):
#             if i == len(matchsticks):
#                 if comb == target and step == 3:
#                     return True
#                 return False
#             if step == 4:
#                 return True
            
#             if comb > target:
#                 return False
#             if comb == target:
#                 return dfs(i + 1, matchsticks[i], step + 1)
            
#             if comb + matchsticks[i] <= target:
#                 return dfs(i + 1, comb + matchsticks[i], step)
#             return False
        
#         return dfs(0, 0, 0)
            