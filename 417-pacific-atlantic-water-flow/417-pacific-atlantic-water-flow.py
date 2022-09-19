class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        pac, atl = set(), set()
        
        rows, cols = len(heights), len(heights[0])
        
        
            
        steps = [[1, 0], [-1, 0], [0, 1], [0, -1]]    
        
        def dfs(r, c, visit):
            if (r, c) in visit:
                return
            visit.add((r, c))
            for i, j in steps:
                if 0 <= r + i < rows and 0 <= c + j < cols and heights[r + i][c + j] >= heights[r][c]:
                    dfs(r + i, c + j, visit)
        
        for i in range(cols):
            dfs(0, i, pac)
            dfs(rows - 1, i, atl)
            
        for i in range(rows):
            dfs(i, 0, pac)
            dfs(i, cols - 1, atl)
        
        return list(atl.intersection(pac))
            
            
            
            
            
            
        