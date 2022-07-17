class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        res = 0
        if k == 0:
            for c in hmap:
                if hmap[c] > 1:
                    res += 1
            return res
        for key, val in hmap.items():
            if key + k in hmap:
                res += 1
        return res
