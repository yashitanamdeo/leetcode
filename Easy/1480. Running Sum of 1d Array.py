# Problem Statement: https://leetcode.com/problems/running-sum-of-1d-array/

# Solution 1
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums

#Solution 2
class Solution:
    def runningSum(self, nums):
        result = [nums[0]] + [0] * (len(nums) - 1)
        for i, num in enumerate(nums[1:]):
            result[i + 1] += result[i] + num
        return result