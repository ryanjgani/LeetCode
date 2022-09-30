class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # O(n^2) time
        boxes = [int(n) for n in boxes]
        res = [0] * len(boxes)
        left = [0] * len(boxes)
        right = [0] * len(boxes)
        prev = 0
        ones = 0
        for i in range(len(boxes) - 1, -1, -1):
            if i == len(boxes) - 1: 
                if boxes[i]: ones += 1
                continue
            right[i] = (ones + right[i + 1]) if ones else 0
            if boxes[i]: ones += 1
        ones = 0
        for i in range(len(boxes)):
            if i == 0: 
                if boxes[i]: ones += 1
                continue
            left[i] = (ones + left[i - 1]) if ones else 0
            if boxes[i]: ones += 1
        res = [left[i] + right[i] for i in range(len(boxes))]
        return res
        
        
        # for i, n in enumerate(boxes):
        #     if n: ones.append(i)
        # for i in range(len(boxes)):
        #     for j in ones:
        #         res[i] += abs(i - j)
        return res