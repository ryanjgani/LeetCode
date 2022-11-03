class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numbers = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []
        def helper(i, comb):
            if i >= len(digits):
                if len(comb):
                    res.append(comb[:])
                return
            for c in numbers[digits[i]]:
                helper(i + 1, comb + c)
        helper(0, "")
        return res