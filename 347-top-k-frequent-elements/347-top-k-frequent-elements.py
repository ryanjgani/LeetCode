class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        array = [[] for _ in range(len(nums) + 1)]
        
        for n in nums:
            if n in hmap:
                hmap[n] += 1
            else:
                hmap[n] = 1
        for i in hmap:
            array[hmap[i]].append(i)
        count = 0
        res = []
        for i in range(len(array) - 1, -1, -1):
            if array[i]:
                res.extend(array[i])
                if len(res) == k:
                    return res
        