class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        res = []
        prev_end = intervals[0][0]
        prev_start = intervals[0][0]
        print("***")
        for interval in intervals:
            if interval[0] <= prev_end:
                if res and interval[1] > prev_end:
                    top = res.pop()
                    res.append([top[0], interval[1]])
                    print('top')
                elif res and interval[1] <= prev_end:
                    continue
                else:
                    print("just append")
                    res.append(interval)
            else:
                res.append(interval)
            prev_start, prev_end = interval[0], interval[1]
        return res            