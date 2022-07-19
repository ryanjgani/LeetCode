class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count = {'U': 0, 'D': 0, "L": 0, "R": 0}
        for m in moves:
            count[m] += 1
        
        if count['U'] != count['D']: return False
        if count['L'] != count['R']: return False 
        return True