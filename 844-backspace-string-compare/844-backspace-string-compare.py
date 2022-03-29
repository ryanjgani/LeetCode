class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        S, T = [], []
        for i, c in enumerate(s):
            if c == "#":
                S = S[:-1]
            else: S.append(c)
        for i, c in enumerate(t):
            if c == "#":
                T = T[:-1]
            else: T.append(c)
     
        return T == S