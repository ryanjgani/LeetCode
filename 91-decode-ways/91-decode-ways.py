class Solution:
    def numDecodings(self, s: str) -> int:
        alphabets = "&ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha = {letter: idx for idx, letter in enumerate(alphabets)}
        memo = {len(s): 1}
        
        def dfs(i):
            if i in memo:
                return memo[i]
            # if i == len(s):
            #     return 1
            if s[i] == '0':
                return 0
            count = dfs(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                count += dfs(i + 2)
            memo[i] = count
            return count
            
        res = dfs(0)
        return res