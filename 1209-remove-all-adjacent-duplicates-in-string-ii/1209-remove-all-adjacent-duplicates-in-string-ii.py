class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][1] == k:
                stack.pop()
            if stack and c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
        
        if stack and stack[-1][1] == k:
            stack.pop()
        res = ""
        for node in stack:
            for _ in range(node[1]):
                res += node[0]
        return res
                
                
                