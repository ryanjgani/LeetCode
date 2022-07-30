class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        
        for t in range(len(matrix)):
            r = len(matrix[0]) - 1
            if matrix[t][r] >= target:
                while r >= 0:
                    if matrix[t][r] == target:
                        return True
                    r -= 1
        return False
                
        
        
        
        
        
        # (nlogm) solution
        for row in matrix:
            l, r = 0, len(row)
            while l < r:
                mid = l + (r - l) // 2
                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid 
                else:
                    return True
        return False