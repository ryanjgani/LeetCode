class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        asc = dec = 0
        for i, n in enumerate(rating):
            leftSmall = leftBig = rightSmall = rightBig = 0
            
            for j in rating[:i]:
                if j < n:
                    leftSmall += 1
                else:
                    leftBig += 1
            for j in rating[i + 1:]:
                if j < n:
                    rightSmall += 1
                else:
                    rightBig += 1
            asc += leftSmall * rightBig
            dec += leftBig * rightSmall
        return asc + dec
        
        
        
        
        
#         dp = {}
#         def dfs(i, prev, step, d):
#             if step == 3:
#                 return 1
#             if i >= len(rating):
#                 return 0
#             if (step, prev, d) in dp:
#                 return dp[(step, prev, d)]
#             temp = dfs(i + 1, prev, step, d)
#             if d == 'asc' and rating[i] > prev:
#                 temp += dfs(i + 1, rating[i], step + 1, d)
#             elif d == 'dec' and rating[i] < prev:
#                 temp += dfs(i + 1, rating[i], step + 1, d)
                
#             dp[(step, prev, d)] = temp
#             return temp
#         return dfs(0, -1, 0, "asc") + dfs(0, float('inf'), 0, "dec")
