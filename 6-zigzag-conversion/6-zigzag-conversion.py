class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # O(n) TC
        if numRows == 1: return s
        res = ""
        for r in range(numRows):
            jump = 2 * (numRows - 1)
            for i in range(r, len(s), jump):
                res += s[i]
                if 0 < r < numRows - 1 and i + jump - 2 * r < len(s):
                    res += s[i + jump - 2 * r]
        return res
        