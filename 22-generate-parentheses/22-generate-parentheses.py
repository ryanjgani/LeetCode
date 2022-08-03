class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(count, comb):
            if len(comb) == (2 * n):
                if count == 0:
                    res.append(comb[:])
                return
            if count < n:
                dfs(count + 1, comb + "(")
            if count:
                dfs(count - 1, comb + ")")
        dfs(0, "")
        return res