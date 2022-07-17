class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        
        moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2)]
#         position = [(row, column, 0, 1)]
#         res = 0

#         while position:
#             r, c, step, prob = position.pop()
#             if step == k:
#                 res += prob
#                 continue
#             for i, j in moves:
#                 if r + i < n and c + j < n and r + i >= 0 and c + j >= 0 and step < k:
#                     position.append((r + i, c + j, step + 1, prob / 8))
#         return res
        # graph solution O(8^k) time and space (TLE)
       
        # DP solution O(n^2 * k) time and O(n^2) space
        
        # dp = [[0] * n for _ in range(n)]
        # dp[row][column] = 1
        # for p in range(k):
        #     temp = [[0] * n for _ in range(n)]
        #     for r in range(n):
        #         for c in range(n):
        #             for i, j in moves:
        #                 if r + i < n and c + j < n and r + i >= 0 and c + j >= 0:
        #                     temp[r + i][c + j] += dp[r][c] / 8
        #     dp = temp
        # res = 0
        # for row in dp:
        #     res += sum(row)
        # return res
        
        mem = {}
        def dfs(r, c, prob, step):
            p = 0
            if 0 <= r < n and 0 <= c < n:
                if step < k:
                    for i, j in moves:
                        nextR, nextC = r + i, c + j
                        if (nextR, nextC, step + 1) not in mem:
                            mem[(nextR, nextC, step + 1)] = dfs(nextR, nextC, prob / 8, step + 1)
                        p += mem[(nextR, nextC, step + 1)] 
                else:
                    p = prob # step == k (base case)
            return p
        return dfs(row, column, 1, 0)    
    
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                    
                    
                    