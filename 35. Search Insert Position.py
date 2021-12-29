# Problem Statement: https://leetcode.com/problems/search-insert-position/

# first try solution
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if value == target:
                return index
        else:
            for index, value in enumerate(nums):
                if value > target:
                    return index
            else:
                return len(nums)