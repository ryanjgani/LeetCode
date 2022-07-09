class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [num for num in range(1, n + 1)]
        
        while len(queue) > 1:
            for _ in range(k - 1):
                pop = queue.pop(0)
                queue.append(pop)
            queue.pop(0)
        return queue[0]