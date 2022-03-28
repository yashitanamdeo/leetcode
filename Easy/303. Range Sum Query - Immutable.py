# Problem Statement: https://leetcode.com/problems/range-sum-query-immutable/

class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = [0]
        for num in nums: 
            self.accu += self.accu[-1] + num,

    def sumRange(self, left: int, right: int) -> int:
        return self.accu[right + 1] - self.accu[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

'''
create an array accu that stores the accumulated sum for nums such that accu[i] = nums[0] + ... + nums[i - 1] in the initializer of NumArray. Then just return accu[j + 1] - accu[i] in sumRange. 
'''