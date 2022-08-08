class Solution:
    def countVowelPermutation(self, n: int) -> int:
        hmap = {
            'a': 'e',
            'e': 'ai',
            'i': 'aeou',
            'o': 'iu',
            'u': 'a'
        }
        vowels = 'aeiou'
        res = 0
        memo = {}
        def dfs(i, comb, count):
            if (i, count) in memo:
                return memo[(i, count)]
            if count == n:
                return 1
            temp = 0
            for idx in range(5):
                if not comb or vowels[idx] in hmap[comb]:
                    temp += dfs(idx, vowels[idx], count + 1)
            memo[(i, count)] = temp % 1000000007
            return memo[(i, count)]
        return dfs(0, "", 0)
        
        
        
        