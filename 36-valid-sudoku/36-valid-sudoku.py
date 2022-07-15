class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # for row in board:
        #     temp = set()
        #     for n in row:
        #         if n == '.': continue
        #         if int(n) not in temp:
        #             temp.add(int(n))
        #         else:
        #             return False
                    
        for c in range(len(board[0])):
            temp = set()
            for r in range(len(board)):
                if board[r][c] == '.': continue
                n = int(board[r][c])
                if n not in temp:
                    temp.add(n)
                else:
                    return False
                
        hmap = {}
        for i in range(3):
            for j in range(3):
                hmap[(i, j)] = set()
        
        for r in range(len(board)):
            temp = set()
            for c in range(len(board[0])):
                if board[r][c] == '.': continue
                key = (r // 3, c // 3)
                number = int(board[r][c])
                if number in hmap[key] or number in temp:
                    return False
                else:
                    hmap[key].add(number)
                    temp.add(number)
        return True
                