class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        hmap = {}
        l = 0
        
        for r, f in enumerate(fruits):
            if f not in hmap:
                hmap[f] = 1
            else:
                hmap[f] += 1
            
            while len(hmap) > 2:
                hmap[fruits[l]] -= 1
                if hmap[fruits[l]] == 0:
                    hmap.pop(fruits[l])
                l += 1
            
            res = max(res, r - l + 1)
        return res