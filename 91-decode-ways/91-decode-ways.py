class Solution:
    def numDecodings(self, s: str) -> int:
        # res = 0
        alphabets = "&ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alpha = {letter: idx for idx, letter in enumerate(alphabets)}
        memo = {len(s): 1}
        
        def dfs(idx, comb):
            nonlocal res
            if idx in memo:
                return memo[idx]
            count = 0
            for i in range(idx + 1, len(s) + 1):
                if s[idx: i][0] != '0' and int(s[idx: i]) <= 26:
                    count += dfs(i, comb + [s[idx: i]])
            memo[idx] = count
            return count
                
        res = dfs(0, [])
        return res