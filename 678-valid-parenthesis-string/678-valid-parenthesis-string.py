class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = 0
        for c in s:
            if c == "*":
                left += 1
                right -= 1
            else:
                left += 1 if c == "(" else -1
                right += 1 if c == "(" else -1
            if left < 0: return False
            if right < 0: right = 0
        return right == 0
        
        
        # memo = {}
        # memo[(len(s), 0)] = True
        # def dfs(i, count):
        #     if (i, count) in memo:
        #         return memo[(i, count)]
        #     if i >= len(s): return False
        #     if s[i] == "*":
        #         temp = dfs(i + 1, count + 1) or dfs(i + 1, count) or dfs(i + 1, count - 1)
        #     else:
        #         temp = dfs(i + 1, count + 1) if s[i] == "(" else dfs(i + 1, count - 1)
        #     memo[(i, count)] = temp
        #     return temp
        # return dfs(0, 0)
      
        
        
        
        
        
        
        # "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
                