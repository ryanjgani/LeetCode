class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        res = [float('inf'), ""]
        tmap = Counter(t)
        smap = {}
        have = 0
        need = len(tmap)
        l = 0
        
        for r in range(len(s)):
            smap[s[r]] = smap.get(s[r], 0) + 1
            if s[r] in tmap and smap[s[r]] == tmap[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < res[0]:
                    res = [r - l + 1, s[l: r + 1]]
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        return res[1]
                        
                