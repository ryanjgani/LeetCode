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
        # DP solution
        
        dp = [[0] * n for _ in range(n)]
        dp[row][column] = 1
        for p in range(k):
            temp = [[0] * n for _ in range(n)]
            for r in range(n):
                for c in range(n):
                    for i, j in moves:
                        if r + i < n and c + j < n and r + i >= 0 and c + j >= 0:
                            temp[r + i][c + j] += dp[r][c] / 8
            dp = temp
        res = 0
        for row in dp:
            res += sum(row)
        return res
                    
                    
                    