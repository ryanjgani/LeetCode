class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        res = []
        
        def dfs(start, end):
            res = []
            for i in range(start, end):
                if expression[i] in "-+*/":
                    left = dfs(start, i)
                    right = dfs(i + 1, end)
                    for l in left:
                        for r in right:
                            if expression[i] == "+":
                                res.append(l + r)
                            elif expression[i] == "-":
                                res.append(l - r)
                            elif expression[i] == "*":
                                res.append(l * r)
                            else:
                                res.append(l / r)
            if len(res) == 0:
                res.append(int(expression[start:end]))
            return res
        return dfs(0, len(expression))