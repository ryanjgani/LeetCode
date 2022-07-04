class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hmap = {}
        
        for r, letter in enumerate(s):
            hmap[letter] = hmap.get(letter, 0) + 1
            
            _max = 0
            for h in hmap:
                _max = max(_max, hmap[h])
            
            wlen = r - l + 1
            while wlen - _max > k:
                hmap[s[l]] -= 1
                l += 1
                wlen = r - l + 1
                for h in hmap:
                    _max = max(_max, hmap[h])
                
            res = max(res, wlen)
        return res