class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        
        while t <= b:
            y_mid = t + (b - t) // 2
            if target < matrix[y_mid][l]:
                b = y_mid - 1
            elif target > matrix[y_mid][r]:
                t = y_mid + 1
            else:
                while l <= r:
                    mid = l + (r - l) // 2
                    if target == matrix[y_mid][mid]:
                        return True
                    elif target > matrix[y_mid][mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False