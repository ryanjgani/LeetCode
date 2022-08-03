class Solution:
    def checkValidString(self, s: str) -> bool:
        # Greedy O(n) TC and constant space
        left = right = 0
        for c in s:
            if c == "*":
                left += 1
                right -= 1
            else:
                left += 1 if c == "(" else -1
                right += 1 if c == "(" else -1
            if left < 0: return False
            if right < 0: right = 0
        return right == 0
        
        # O(n^3) TC and O(n^2) SC
        memo = {}
        def dfs(i, count):
            if (i, count) in memo:
                return memo[(i, count)]
            if i == len(s) or count < 0:
                return count == 0
            if s[i] == "*":
                temp = dfs(i + 1, count + 1) or dfs(i + 1, count) or dfs(i + 1, count - 1)
            else:
                temp = dfs(i + 1, count + 1) if s[i] == "(" else dfs(i + 1, count - 1)
            memo[(i, count)] = temp
            return temp
        return dfs(0, 0)
                