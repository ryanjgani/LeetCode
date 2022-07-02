class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        hmap = {}
        hmap[0] = 1
        curSum = 0
        for n in nums:
            curSum += n
            if curSum - k in hmap:
                res += hmap[curSum - k]
            if curSum in hmap:
                hmap[curSum] += 1
            else:
                hmap[curSum] = 1
        return res
        
            