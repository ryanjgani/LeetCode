class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(comb, left, right):
            if len(comb) == 2 * n:
                res.append(comb[:])
                return
            if left < n:
                dfs(comb + "(", left + 1, right)
            if right < n and left > right:
                dfs(comb + ")", left, right + 1)
        dfs("", 0, 0)
        return res