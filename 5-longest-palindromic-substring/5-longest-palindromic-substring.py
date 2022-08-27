class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = (0, "")
        for i in range(len(s)):
            count = 1
            j = 1
            while i - j >= 0 and i + j < len(s) and s[i - j] == s[i + j]:
                count += 2
                j += 1
            j -= 1
            if count > res[0]:
                res = (count, s[i - j: i + j + 1])
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]: continue
            count = 2
            j = 1
            while i - j >= 0 and i + 1 + j < len(s) and s[i - j] == s[i + 1 + j]:
                count += 2
                j += 1
            j -= 1
            if count > res[0]:
                res = (count, s[i - j: i + 1 + j + 1])            
            
        return res[1]