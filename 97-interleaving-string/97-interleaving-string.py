class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}
        if len(s3) != len(s1) + len(s2):
            return False
        def dfs(i, j, comb):
            if (i, j, comb) in memo:
                return memo[(i, j, comb)]
            if comb and comb[-1] != s3[len(comb) - 1]:
                return False
            if i == len(s1) and j == len(s2):
                return comb == s3
            if i == len(s1):
                return comb + s2[j:] == s3
            if j == len(s2):
                return comb + s1[i:] == s3
            
            memo[(i, j, comb)] = dfs(i + 1, j, comb + s1[i]) or dfs(i, j + 1, comb + s2[j])
            return memo[(i, j, comb)]
        return dfs(0, 0, "")
            
            