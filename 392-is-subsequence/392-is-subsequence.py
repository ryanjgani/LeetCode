class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i = j = 0
        # while i < len(s) and j < len(t):
        #     if s[i] == t[j]: i += 1
        #     j += 1
        # return i == len(s)
        
        i = 0
        if i == len(s): return True
        for j, c in enumerate(t):
            if s[i] == c: i += 1
            if i == len(s): return True
        return False
