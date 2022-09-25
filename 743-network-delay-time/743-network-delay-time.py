class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {}
        for src, target, time in times:
            graph[src] = graph.get(src, []) + [(target, time)]
            
        heap = [(0, k)]
        heapify(heap)
        visit = set()
        res = 0
        while heap and len(visit) < n:
            path, node = heappop(heap)
            visit.add(node)
            res = max(res, path)
            if node in graph:
                for target, time in graph[node]:
                    if target not in visit:
                        heappush(heap, (path + time, target))

        return res if len(visit) == n else -1
            