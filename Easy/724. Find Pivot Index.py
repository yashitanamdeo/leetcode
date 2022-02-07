# Problem Statement: https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum, rightSum = 0,sum(nums)
        for index,num in enumerate(nums):
            rightSum -= num
            if rightSum == leftSum:
                return index
            leftSum += num
        return -1

# Alternate Solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftsum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if leftsum == total_sum - leftsum - nums[i]:
                return i
            leftsum += nums[i]
        return -1