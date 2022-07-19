class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        hmap = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        res = []
        def dfs(i, comb):
            if i == len(digits):
                res.append(comb[:])
                return
            for letter in hmap[int(digits[i])]:
                dfs(i + 1, comb + letter)
        dfs(0, "")
        return res if len(digits) else []
        
        