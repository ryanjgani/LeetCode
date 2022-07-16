class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        for start, end in intervals:
            if newInterval and newInterval[0] <= end and newInterval[1] >= start:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
                continue  
            if newInterval and newInterval[1] < start:
                res.append(newInterval)
                newInterval = None
            res.append([start, end])
        
        return res + [newInterval] if newInterval else res
           
                
                
                
                
