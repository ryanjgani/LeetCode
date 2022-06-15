class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        for word in strs:
            temp = sorted(word)
            if str(temp) in hmap:
                hmap[str(temp)].append(word)
            else:
                hmap[str(temp)] = [word]
        res = []
        for words in hmap:
            res.append(hmap[words])
        return res