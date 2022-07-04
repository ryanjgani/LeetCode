class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memory = set()
        res = 0
        l = 0
        for r, letter in enumerate(s):
            if letter in memory:
                while s[l] != letter:
                    memory.remove(s[l])
                    l += 1
                memory.remove(s[l])
                l += 1
            memory.add(letter)
                
            res = max(res, r - l + 1)
        return res