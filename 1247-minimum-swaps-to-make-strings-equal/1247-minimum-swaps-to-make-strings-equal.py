class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y, y_x = 0, 0
        res = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x' and s2[i] == 'y':
                    x_y += 1
                else:
                    y_x += 1
        if (x_y + y_x) % 2: return -1
        
        res += x_y // 2 + y_x // 2
        x_y = x_y % 2
        y_x = y_x % 2
        if x_y and y_x:
            res += 2
        return res
        
