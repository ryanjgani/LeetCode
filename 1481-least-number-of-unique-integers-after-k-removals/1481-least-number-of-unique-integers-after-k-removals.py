class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        hmap = Counter(arr)
        v = [(hmap[i], i) for i in hmap]
        v.sort()
        res = len(v)
        for value, key in v:
            if value <= k:
                k -= value
                res -= 1
            else:
                return res
        return res
        
        