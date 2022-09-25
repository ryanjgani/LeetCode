class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)
        # cycle = set()
        # def dfs(n):
        #     if len(graph[n]) == 0: return True
        #     if n in cycle: return False
        #     cycle.add(n)
        #     for node in graph[n]:
        #         if not dfs(node): return False
        #     cycle.remove(n)
        #     graph[n] = []
        #     return True
        # for i in range(numCourses):
        #     if not dfs(i): return False
        # return True
    
        visit = [0] * numCourses
        def dfs(n):
            if visit[n] == 1: return True
            if visit[n] == -1: return False
            visit[n] = -1
            for node in graph[n]:
                if not dfs(node): return False
            visit[n] = 1
            return True
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True

