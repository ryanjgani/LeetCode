class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        visit = [0] * numCourses
        
        def dfs(i):
            if visit[i] == 1: return True
            if visit[i] == -1: return False
            
            visit[i] = -1
            for node in graph[i]:
                if not dfs(node): return False
            visit[i] = 1
            res.append(i)
            return True
        for n in range(numCourses):
            if not dfs(n): return []
        return res
        