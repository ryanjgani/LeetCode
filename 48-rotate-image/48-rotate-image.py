class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1
        t, b = 0, len(matrix) - 1
        
        while l <= r and t <= b:
            for i in range(r-l):
                matrix[t][l + i], matrix[t + i][r], matrix[b][r - i], matrix[b - i][l] = matrix[b - i][l], matrix[t][l + i], matrix[t + i][r], matrix[b][r - i]
            t += 1
            l += 1
            b -= 1
            r -= 1
        