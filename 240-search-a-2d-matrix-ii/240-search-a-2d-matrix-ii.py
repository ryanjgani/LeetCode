class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            l, r = 0, len(row)
            print(row)
            while l < r:
                mid = l + (r - l) // 2
                print(l, r, mid)
                if target > row[mid]:
                    l = mid + 1
                elif target < row[mid]:
                    r = mid 
                else:
                    return True
        return False