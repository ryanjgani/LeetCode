class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        nums = []
        queue = []
        for key, value in count.items():
            nums.append(-1 * value)
        heapify(nums)
        time = 0
        
        while nums or queue:
            if queue and queue[0][1] == time:
                heappush(nums, queue.pop(0)[0])
            time += 1
            if nums:
                pop = heappop(nums) * -1
                pop -= 1
                if pop:
                    queue.append([pop * -1, time + n])
        return time