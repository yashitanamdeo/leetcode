# Problem Statement: https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if len(nums) == 0:
            return 0
        else:
            lp = 0
            for rp in range(0,len(nums)):
                if nums[rp] != val:
                    nums[lp] = nums[rp]
                    lp += 1
            return lp