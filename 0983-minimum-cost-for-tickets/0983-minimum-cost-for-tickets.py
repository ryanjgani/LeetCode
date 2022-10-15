class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        daily, weekly, monthly = costs
        
        dp = {}
        def dfs(i, covered):
            if i == len(days): return 0
            if (i, covered) in dp: return dp[(i, covered)]
            if i > len(days): return float('inf')
            
            if covered < days[i]:
                d = dfs(i + 1, days[i] + 1 - 1) + daily
                w = dfs(i + 1, days[i] + 7 - 1) + weekly
                m = dfs(i + 1, days[i] + 30 - 1) + monthly
                dp[(i, covered)] = min(d,w,m)
            else:
                dp[(i, covered)] = dfs(i + 1, covered)
            return dp[(i, covered)]
            
        res = dfs(0, 0)
        return res