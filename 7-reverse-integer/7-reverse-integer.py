class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647
        MIN = -2147483648
        
        res = 0
        while x:
            last = int(math.fmod(x, 10))
            x = int(x / 10)
            
            if res > MAX // 10 or (res == MAX // 10 and last >= MAX % 10):
                return 0
            if res < MIN // 10 or (res == MIN // 10 and last <= MIN % 10):
                return 0
            
            res = (res * 10) + last
        return res