class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        length = 0
        res = len(nums)
        for n in nums:
            if n: length += 1
        n = len(nums)
        nums = nums + nums
        count = Counter(nums[:length])
        res = count[0]
        j = 0
        for i in range(1, n):
            if nums[j] == 0:
                count[0] -= 1
            if nums[i + length - 1] == 0:
                count[0] += 1
            res = min(res, count[0])
            j += 1
        return res
        
        
        