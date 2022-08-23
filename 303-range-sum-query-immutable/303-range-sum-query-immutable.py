class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.accu = [0]
        for n in nums:
            self.accu.append(self.accu[-1] + n)

    def sumRange(self, left: int, right: int) -> int:
        return self.accu[right + 1] - self.accu[left]
        
        
        return sum(self.nums[left: right + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)