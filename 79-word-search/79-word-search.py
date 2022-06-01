class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        path = set()
        
        def dfs(i, r, c):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != word[i] or (r, c) in path:
                return False
            path.add((r, c))
            res = dfs(i + 1, r, c + 1) or dfs(i + 1, r + 1, c) or dfs(i + 1, r, c - 1) or dfs(i + 1, r - 1, c)
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        return False
