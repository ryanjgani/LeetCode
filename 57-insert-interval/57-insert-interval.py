class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newStart, newEnd = newInterval
        
        # if not intervals: return [newInterval]
        # if newEnd < intervals[0][0]:
        #     return newInterval + intervals
        # if newStart > intervals[-1][1]:
        #     return intervals + newInterval
        
        res = []
    
               
        for start, end in intervals:
            if newInterval and newEnd >= start and newStart <= end:
                newInterval = [min(start, newStart), max(end, newEnd)]
                newStart, newEnd = newInterval
                continue
            if newInterval and newEnd < start: 
                res.append(newInterval)
                newInterval = None
            res.append([start, end])
        if newInterval:
            res.append(newInterval)
        return res
