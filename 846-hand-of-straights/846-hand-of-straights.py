class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        counter = Counter(hand)
        arr = list(counter.keys())
        heapify(arr)
        count = 0
        while arr:
            count += 1
            n = arr[0]
            counter[n] -= 1
            if counter[n] == 0: heappop(arr)
            for _ in range(groupSize - 1):
                n += 1
                if counter.get(n, 0) == 0:
                    return False
                counter[n] -= 1
                if counter[n] == 0: heappop(arr)
        return True
        
