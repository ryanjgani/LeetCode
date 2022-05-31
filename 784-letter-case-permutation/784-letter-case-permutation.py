class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # BFS solution - iterative
        res = [s]
        for i in range(len(s)):
            temp = []
            if s[i].isalpha():
                while res:
                    string = res.pop(0)
                    left = string[:i]
                    right = string[i + 1:]
                    temp.append(left + s[i].upper() + right)
                    temp.append(left + s[i].lower() + right)
                res = temp
        return res