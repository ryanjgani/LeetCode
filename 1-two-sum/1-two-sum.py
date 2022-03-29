class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in d:
                return [d[dif], i]
            d[nums[i]] = i
