class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        hmap = {c: 0 for c in alphabets}
        target = {c: 0 for c in alphabets}
        for c in s1:
            target[c] += 1
        
        l, n = 0, len(s1)
        for r in range(len(s2)):
            hmap[s2[r]] += 1
            if r >= n - 1:
                ans = True
                if hmap == target: return True
                hmap[s2[l]] -= 1
                l += 1
        return False
        
        