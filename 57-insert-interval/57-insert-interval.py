class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            prev_end = res[-1][1]
            if start <= prev_end:
                res[-1][1] = max(prev_end, end)
            else:
                res.append([start, end])
        return res   
    
        # res = [intervals[0]]
        # for start, end in intervals[1:]:
        #     prev_end = res[-1][1]
        #     if newInterval[0] <= end:
        #         if newInterval[1] > interval[1]:
        #             res.append([])