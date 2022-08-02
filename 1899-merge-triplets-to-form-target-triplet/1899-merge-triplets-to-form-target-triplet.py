class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        temp = target[:]
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            for i in range(3):
                if t[i] == target[i]:
                    temp[i] = 0
                
        # for i in range(rows):
        #     for j in range(3):
        #         if target[j] and arr[i][j] == target[j]:
        #             target[j] = 0
        return sum(temp) == 0