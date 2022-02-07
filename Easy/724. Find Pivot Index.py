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