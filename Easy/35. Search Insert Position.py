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

""" to learn::-- https://leetcode.com/problems/search-insert-position/discuss/1596603/C%2B%2BPython-Simple-Solutions-w-Explanation-or-Recursive-and-Iterative-Binary-Search """