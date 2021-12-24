# Problem Link: https://leetcode.com/problems/contains-duplicate/
class Solution:
    def containsDuplicate(self, nums):
        return (len(nums) > len(set(nums)))

# Alternate Method