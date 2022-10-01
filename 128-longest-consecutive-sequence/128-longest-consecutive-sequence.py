class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        allnums = set(nums)
        hmap = {}
        res = 0
        for n in nums:
            if n - 1 not in allnums:
                count = 1
                nextNum = n + 1
                while nextNum in allnums:
                    count += 1
                    nextNum += 1
                res = max(res, count)
        return res
        
        
        
                
        
        