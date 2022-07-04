class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        hmap = {}
        
        for r, letter in enumerate(s):
            hmap[letter] = hmap.get(letter, 0) + 1
            
            while (r - l + 1) - max(hmap.values()) > k:
                hmap[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res