class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        initial = [0, 0]
        directions = ['N', 'E', 'S', 'W']
        key = 0
        
        
        for i in instructions:
            if i == 'G':
                if directions[key] == 'N':
                    initial[1] += 1
                elif directions[key] == 'S':
                    initial[1] -= 1
                elif directions[key] == 'E':
                    initial[0] += 1
                else:
                    initial[0] -= 1
            elif i == 'L':
                key -= 1
                key = key % 4
            else:
                key += 1
                key = key % 4
        if initial == [0, 0] or directions[key] != 'N':
            return True
        return False
        
        
        
        