class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # O(n^2) time
        boxes = [int(n) for n in boxes]
        left = [0] * len(boxes)
        right = [0] * len(boxes)
        ones = boxes[-1]
        for i in range(len(boxes) - 2, -1, -1):
            right[i] = (ones + right[i + 1]) if ones else 0
            ones += boxes[i]
        ones = boxes[0]
        for i in range(1, len(boxes)):
            left[i] = (ones + left[i - 1]) if ones else 0
            ones += boxes[i]
        res = [left[i] + right[i] for i in range(len(boxes))]
        return res
        
        
        # for i, n in enumerate(boxes):
        #     if n: ones.append(i)
        # for i in range(len(boxes)):
        #     for j in ones:
        #         res[i] += abs(i - j)
        return res