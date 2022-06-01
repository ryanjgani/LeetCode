class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(idx, substring):
            if idx == len(s):
                res.append(substring[:])
                return
            
            for i in range(idx, len(s)):
                currentString = s[idx: i + 1]
                if currentString == currentString[::-1]:
                    substring.append(currentString)
                    dfs(i + 1, substring)
                    substring.pop()
        dfs(0, [])
        return res