class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(key=lambda x: x[0])
        stack = []
        for p, s in cars[::-1]:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)
        