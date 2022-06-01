class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def isPalindrome(s):
            return s == s[::-1]
        
        def dfs(idx, substring):
            if idx == len(s):
                res.append(substring[:])
                return
            
            # if not isPalindrome(substring)
            
            for i in range(idx, len(s)):
                print(s[idx: i + 1])
                if isPalindrome(s[idx: i + 1]):
                    print("is palindrome", i)
                    substring.append(s[idx: i + 1])
                    dfs(i + 1, substring)
                    substring.pop()
        dfs(0, [])
        return res