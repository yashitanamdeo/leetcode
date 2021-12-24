# Problem Link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums):
        return (len(nums) > len(set(nums)))

# Alternate Method
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        array = set(nums)
        return (len(array) != len(nums))