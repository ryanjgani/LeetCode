class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        visit = set()
        count = 0
        for i in range(len(s)):
            if s[i] in visit:
                count = max(count, len(visit))
                while s[l] != s[i]:
                    l += 1
                l += 1
                visit = set(s[l: i + 1])
            else:
                visit.add(s[i])
        count = max(count, len(visit))
        return count
            