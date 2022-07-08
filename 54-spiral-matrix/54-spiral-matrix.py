class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0])
        t, d = 0, len(matrix)

        while l < r and t < d:
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
     
            for j in range(t, d):
                res.append(matrix[j][r - 1])
            r -= 1
            
            if l >= r or t >= d:
                break
          
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[d - 1][i])
            d -= 1
            
            for j in range(d - 1, t - 1, -1):
                res.append(matrix[j][l])
            l += 1
        return res