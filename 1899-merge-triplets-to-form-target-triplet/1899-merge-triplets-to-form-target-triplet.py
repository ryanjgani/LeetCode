class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        arr = []
        for tri in triplets:
            arr.append(tri)
            for j in range(3):
                if tri[j] > target[j]:
                    arr.pop()
                    break
        rows = len(arr)
        cols = 3
        for i in range(rows):
            for j in range(3):
                if target[j] and arr[i][j] == target[j]:
                    target[j] = 0
        return sum(target) == 0