class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = {}
        res = []
        
        for word in strs:
            temp = str(sorted(word))
            if temp in hmap:
                hmap[temp].append(word)
            else:
                hmap[temp] = [word]
        for h in hmap:
            res.append(hmap[h])
        return res