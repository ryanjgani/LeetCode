class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        prev_end = intervals[0][1]
        print(intervals)
        for start, end in intervals[1:]:
            # overlap
            if start < prev_end:
                count += 1
                prev_end = min(prev_end, end)
            else:
                prev_end = end
        return count
                
        