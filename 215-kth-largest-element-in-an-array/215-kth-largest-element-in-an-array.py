class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n^2) worst but O(n) average time, Quick Select method (using quick sort)
        target = len(nums) - k
        def quicksort(start, end):
            partition = nums[end]
            l = start
            for i in range(start, end):
                if nums[i] < partition:
                    nums[i], nums[l] = nums[l], nums[i]
                    l += 1
            nums[end], nums[l] = nums[l], nums[end]
            if l == target:
                return nums[l]
            return quicksort(l + 1, end) if target > l else quicksort(start, l - 1)
        return quicksort(0, len(nums) - 1)
        
        # O(n + klogn) time and O(n) space
        # heap = []
        # for n in nums:
        #     heappush(heap, -1 * n)
        # while k - 1:
        #     heappop(heap)
        #     k -= 1
        # return heap[0] * -1