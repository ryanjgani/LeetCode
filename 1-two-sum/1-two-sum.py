class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for i in range(len(nums)):
            if (target - nums[i]) in cache:
                return [i, cache[target - nums[i]]]
            else:
                cache[nums[i]] = i