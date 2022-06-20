class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        prev_start, prev_end = intervals[0]
        
        for i, interval in enumerate(intervals):
            if i == 0: continue
            if interval[0] <= prev_end:
                if interval[1] > prev_end:
                    top = res.pop()
                    res.append([top[0], interval[1]])
                else:
                    continue
            else:
                res.append(interval)
            prev_start, prev_end = interval
        return res            