class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(comb, op, close):
            if len(comb) == 2*n:
                res.append(comb[:])
                return
            
            if op < n:
                dfs(comb + "(", op + 1, close)
                
            if close < op and close < n:
                dfs(comb + ")", op, close + 1)
                
            return res
        
        dfs("", 0, 0)
        return res