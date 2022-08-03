class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")": "(", "}": "{", "]": "["}
        

        
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if stack and hmap[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
            
        
        