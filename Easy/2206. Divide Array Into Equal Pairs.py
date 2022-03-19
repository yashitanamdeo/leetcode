# Problem Statement: https://leetcode.com/problems/divide-array-into-equal-pairs/

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
		#counting appearances
        count = collections.Counter(nums)
		#if a number has an odd frequency, it can't be split as the constraints require, so we can just return false
        for k, v in count.items():
            if v % 2:
                return False
        return True  