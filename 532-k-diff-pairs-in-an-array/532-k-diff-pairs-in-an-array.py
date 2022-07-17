class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hmap = Counter(nums)
        res = 0
        if k == 0:
            for c in hmap:
                res += 1 if hmap[c] > 1 else 0
        else:
            for key, val in hmap.items():
                res += 1 if key + k in hmap else 0
        return res
