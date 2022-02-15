# Problem Statement: https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num