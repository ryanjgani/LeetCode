class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for t in tokens:
            if t.isnumeric():
                stack.append(int(t))
            elif len(t) > 1 and t[0] == '-':
                stack.append(int(t[1:]) * -1)
            else:
                s2 = stack.pop()
                s1 = stack.pop()
                if t == '+':
                    temp = s1 + s2
                elif t == '-':
                    temp = s1 - s2
                elif t == '*':
                    temp = s1 * s2
                else:
                    temp = int(s1 / s2)
                stack.append(temp)
        return stack[0]