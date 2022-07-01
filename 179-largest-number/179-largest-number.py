class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # merge sort
        
        def compare(n1, n2):
            return str(n1) + str(n2) > str(n2) + str(n1)
        
        def mergeSort(nums):
            if len(nums) == 1:
                return nums
            if len(nums) < 1:
                return
            mid  = len(nums) // 2
            left = mergeSort(nums[: mid])
            right = mergeSort(nums[mid:])
            return merge(left, right)
        
        def merge(left, right):
            res, i, j = [], 0, 0
            while i < len(left) and j < len(right):
                if not compare(left[i], right[j]):
                    res.append(right[j])
                    j += 1
                else:
                    res.append(left[i])
                    i += 1
            res.extend(left[i:] or right[j:])
            return res
        
        nums = mergeSort(nums)
        return str(int("".join(map(str, nums))))
    
        
        
        
        
        
        # built-in sort method
        # for i, n in enumerate(nums):
        #     nums[i] = str(n)
        # def compare(n1, n2):
        #     if n1 + n2 > n2 + n1:
        #         return -1
        #     else:
        #         return 1
        # nums = sorted(nums, key=cmp_to_key(compare))
        # return str(int("".join(nums)))