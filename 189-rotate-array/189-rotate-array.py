class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # res = nums[:]
        # for i in range(len(nums)):
        #     res[(i + k) % len(nums)] = nums[i]
        # for i in range(len(nums)):
        #     nums[i] = res[i]
        
        # linear time and constant space
        k = k % len(nums)
        nums.reverse()
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
            