class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        memo[len(s)] = True
        def dfs(i):
            if i in memo:
                return memo[i]
            temp = False
            for word in wordDict:
                n = len(word)
                if i + n <= len(s) and word == s[i:i+n]:
                    if dfs(i + n):
                        temp = True
            memo[i] = temp
            return temp
        return dfs(0)