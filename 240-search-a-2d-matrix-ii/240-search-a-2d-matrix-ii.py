class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = 0, len(matrix[0]) - 1
        
        while r < len(matrix) and c >= 0:
            if target > matrix[r][c]:
                r += 1
            elif target < matrix[r][c]:
                c -= 1
            else:
                return True
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