class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Bottom Up
        dp = {}
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            dp[i] = False
            for word in wordDict:
                n = len(word)
                if i + n <= len(s) and word == s[i:i+n]:
                    dp[i] = dp[i + n]
                if dp[i]:
                    break
        
        
        
        
        
        return dp[0]
        
        
        
        # Top Down memo
        # memo = {}
        # memo[len(s)] = True
        # def dfs(i):
        #     if i in memo:
        #         return memo[i]
        #     temp = False
        #     for word in wordDict:
        #         n = len(word)
        #         if i + n <= len(s) and word == s[i:i+n] and dfs(i + n):
        #             temp = True
        #     memo[i] = temp
        #     return temp
        # return dfs(0)