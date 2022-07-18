class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        moves = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        
        n = len(board)
        m = len(board[0])
        
        table = [0, 1, 0, 1]
        
        for r in range(n):
            for c in range(m):
                oneCounts = 0
                for i, j in moves:
                    if 0 <= r + i < n and 0 <= c + j < m and table[board[r + i][c + j]] == 1:
                        oneCounts += 1
                if board[r][c] == 1:
                    if oneCounts < 2 or oneCounts > 3:
                        board[r][c] = 1
                    else:
                        board[r][c] = 3
                else:
                    if oneCounts == 3:
                        board[r][c] = 2
                    else:
                        board[r][c] = 0
        table = [0, 0, 1, 1]
        for r in range(n):
            for c in range(m):
                board[r][c] = table[board[r][c]]
                
                
                