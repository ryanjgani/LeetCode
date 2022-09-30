class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        boxes = [int(n) for n in boxes]
        res = [0] * len(boxes)
        ones = []
        for i, n in enumerate(boxes):
            if n: ones.append(i)
        for i in range(len(boxes)):
            for j in ones:
                res[i] += abs(i - j)
        return res