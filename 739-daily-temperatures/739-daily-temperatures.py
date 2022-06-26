class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                top = stack.pop()
                difference = i - top[1]
                res[top[1]] = difference
            stack.append([temp, i])
        
        
        return res