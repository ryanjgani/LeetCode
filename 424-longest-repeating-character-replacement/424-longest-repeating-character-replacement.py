class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        r = 0
        hmap = {}
        hmap[s[0]] = 1
        res = 0
        for l in range(1, len(s)):
            if s[l] in hmap: hmap[s[l]] += 1
            else: hmap[s[l]] = 1
            wlen = l - r + 1
            maxCount = 0
            for c in hmap: 
                maxCount = max(maxCount, hmap[c])
            if wlen - maxCount <= k:
                res = max(res, wlen)
            else:
                hmap[s[r]] -= 1
                r += 1
        return res
            