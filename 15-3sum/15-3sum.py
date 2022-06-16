class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue
            l, r = i + 1, len(nums) - 1

            while l < r:
                total = nums[l] + nums[r] + nums[i]
                if total == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if total < 0: l += 1
                else: r -= 1
                
        # for i in range(len(nums)):
        #     if nums[i] in dp: continue
        #     target = nums[i] * -1
        #     print(target)
        #     hmap = {}
        #     for j in range(i + 1, len(nums)):
        #         if target - nums[j] in hmap:
        #             res.append([nums[i], nums[j], nums[hmap[target - nums[j]]]])
        #         hmap[nums[j]] = j
        return res