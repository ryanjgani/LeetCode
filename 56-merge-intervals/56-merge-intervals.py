class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for start, end in intervals:
            top = res.pop()
            if top[1] >= start:
                top = [min(top[0], start), max(top[1], end)]
                res.append(top)
            else:
                res.append(top)
                res.append([start, end])
        return res