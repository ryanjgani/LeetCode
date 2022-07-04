class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [[0, temperatures[0]]]
        
        for i in range(1, len(temperatures)):
            t = temperatures[i]
            while stack and stack[-1][1] < t:
                top = stack.pop()
                res[top[0]] = i - top[0]
            stack.append([i, t])
        return res
            
        