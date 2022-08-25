class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while stack and int(stack[-1]) > int(n) and k:
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        return str(int("".join(["0"] + stack)))
        
        
        
        
        
        
#         n = len(num) - k
#         res = float('inf')
#         dp = {}
#         def dfs(i, comb):
#             if (i, comb) in dp:
#                 return dp[(i, comb)]
#             if i == len(num):
#                 if len(comb) == n:
#                     return int("0" + comb)
#                 return float('inf')
#             dp[(i, comb)] = min(dfs(i + 1, comb + num[i]), dfs(i + 1, comb))
#             return dp[(i, comb)]
            
#         return str(dfs(0, ""))
