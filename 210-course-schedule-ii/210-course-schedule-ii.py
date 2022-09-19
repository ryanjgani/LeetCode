class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premap = {i: [] for i in range(numCourses)}
        res = []
        visit = set()
        crossed = set()
        
        for a, b in prerequisites:
            premap[a].append(b)
        
        def dfs(n):
            if n in crossed:
                return True
            if n in visit:
                return False
            if premap[n] == []:
                res.append(n)
                crossed.add(n)
                return True
            visit.add(n)
            for prereq in premap[n]:
                if not dfs(prereq): return False
            visit.remove(n)
            crossed.add(n)
            res.append(n)
            premap[n] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
        
                
        