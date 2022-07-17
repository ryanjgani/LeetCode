class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        
        for c in s[1:]:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)
        