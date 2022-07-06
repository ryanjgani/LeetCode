class Solution:
    def isHappy(self, n: int) -> bool:
        arr = set()
        def helper(n):
            if n == 1:
                return True
            if n in arr:
                return False
            arr.add(n)
            # break down
            new_total = 0
            while n > 0:
                tmp = n % 10
                new_total += tmp * tmp
                n = n // 10
            return helper(new_total)
        return helper(n)