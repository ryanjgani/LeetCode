class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack and stack[-1] >= 0 and s[stack[-1]] == '(':
                    stack.pop()
                    res = max(res, i - stack[-1])
                else:
                    stack.append(i)
        return res
        
        
    
            
            
            
            