class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        top, down = 0, m - 1
        print("**")
        while down >= top:
            mid = top + (down - top) // 2
            print(matrix[mid][0], matrix[mid][-1])
            if target < matrix[mid][0]:
                down = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                l, r = 0, n - 1
                while l <= r:
                    center = l + (r - l) // 2
                    if target < matrix[mid][center]:
                        r = center - 1
                    elif target > matrix[mid][center]:
                        l = center + 1
                    else:
                        return True
                break
        return False