class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        hmap = {c: 0 for c in alphabets}
        target = {c: 0 for c in alphabets}
        l, n = 0, len(s1)
        
        matches = 0
        for i in range(len(s1)):
            target[s1[i]] += 1
            hmap[s2[i]] += 1
        for c in alphabets:
            if target[c] == hmap[c]: matches += 1
         
        for r in range(n, len(s2)):
            if matches == 26: 
                return True            
            i = s2[r]
            hmap[i] += 1
            if hmap[i] == target[i]:
                matches += 1
            elif hmap[i] - 1 == target[i]:
                matches -= 1
            i = s2[l]
            hmap[i] -= 1
            if hmap[i] == target[i]:
                matches += 1
            elif hmap[i] + 1 == target[i]:
                matches -= 1
            l += 1
            
        return matches == 26
        
        # alphabets = "abcdefghijklmnopqrstuvwxyz"
        # hmap = {c: 0 for c in alphabets}
        # target = {c: 0 for c in alphabets}
        # for c in s1:
        #     target[c] += 1
        # l, n = 0, len(s1)
        # for r in range(len(s2)):
        #     hmap[s2[r]] += 1
        #     if r >= n - 1:
        #         ans = True
        #         if hmap == target: return True
        #         hmap[s2[l]] -= 1
        #         l += 1
        # return False
        
        