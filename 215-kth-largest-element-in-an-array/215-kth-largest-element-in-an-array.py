class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        count = 0
        def quicksort(start, p):
            partition = nums[p]
            l, r = start, p - 1
            for i in range(start, p):
                if nums[i] < partition:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
            nums[p], nums[l] = nums[l], nums[p]
            if l == target:
                return nums[l]
            return quicksort(l + 1, p) if target > l else quicksort(start, l - 1)
        return quicksort(0, len(nums) - 1)
        
        
        
        
        
        
        # O(n + klogn) time and O(n) space
        # heap = []
        # for n in nums:
        #     heappush(heap, -1 * n)
        # while k - 1:
        #     heappop(heap)
        #     k -= 1
        # return heap[0] * -1