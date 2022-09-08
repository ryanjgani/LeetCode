class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {}
        hmap[0] = 1
        res = 0
        count = 0
        for n in nums:
            count += n
            if count - k in hmap:
                res += hmap[count - k]
            hmap[count] = hmap.get(count, 0) + 1
        return res