class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # [a, b] must take class b first then a
        hmap = {i: [] for i in range(numCourses)}
        visit = set()
        
        for a, b in prerequisites:
            hmap[a].append(b)
        
        def dfs(n):
            if n in visit:
                return False
            if hmap[n] == []:
                return True
            visit.add(n)
            for prereq in hmap[n]:
                if not dfs(prereq):
                    return False
            visit.remove(n)
            hmap[n] = []
            return True
        for n in range(numCourses):
            if len(hmap) and not dfs(n):
                return False
        return True
        