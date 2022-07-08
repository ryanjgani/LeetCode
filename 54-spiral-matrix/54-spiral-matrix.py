class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, len(matrix[0])
        t, d = 0, len(matrix)

        def helper(l, r, t, d):
            # base case
            if l >= r or t >= d:
                return

            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            if l >= r or t >= d:
                return
            for j in range(t, d):
                res.append(matrix[j][r - 1])
            r -= 1
            if l >= r or t >= d:
                return
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[d - 1][i])
            d -= 1
            if l >= r or t >= d:
                return
            for j in range(d - 1, t - 1, -1):
                res.append(matrix[j][l])
            l += 1
            if l >= r or t >= d:
                return
            return helper(l,r,t,d)
        helper(l,r,t,d)
        return res