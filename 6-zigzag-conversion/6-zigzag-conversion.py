class Solution:
    def convert(self, s: str, numRows: int) -> str:
        distance = numRows - 2
        jump = (numRows - 1) * 2
        arr = [[""] * len(s) for _ in range(len(s))]
        i = 0
        startR = numRows - 2
        startC = distance
        startI = jump - 1
        if numRows == 1: return s
        for r in range(numRows):
            c = 0
            temp = i
            while i < len(s):
                arr[r][c] = s[i]
                i += jump
                c += distance + 1
            i = temp + 1
        i = startI
        for r in range(1, numRows - 1):
            c = startC
            temp = i
            print(i, r, c)
            while i < len(s):
                arr[r][c] = s[i]
                i += jump
                c += distance + 1
            startC -= 1
            i = temp - 1
        res = ""
        for r in range(len(s)):
            for c in range(len(s)):
                res += arr[r][c]
        return res
        