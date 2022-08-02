class Solution:
    def partitionLabels(self, s: str) -> List[int]:
#         count = {}
#         for i, c in enumerate(s):
#             count[c] = count.get(c, []) + [i]
#         intervals = []
#         for c in count.values():
#             start, end = c[0], c[-1]
#             intervals.append([c[0], c[-1]])
#         intervals.sort(key = lambda x: x[0])
#         arr = [intervals[0]]
        
#         for start, end in intervals:
#             s, e = arr[-1][0], arr[-1][1]
#             if start > e:
#                 arr.append([start, end])
#             else:
#                 arr[-1] = [min(start, s), max(end, e)]
#         res = [(a[1] - a[0] + 1) for a in arr]
        # return res
        hmap = {}
        for i, c in enumerate(s):
            hmap[c] = i
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, hmap[c])
            if i == end:
                res.append(size)
                size = 0
        return res            
            
            
            