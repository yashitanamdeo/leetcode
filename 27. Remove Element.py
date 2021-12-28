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

'''
Similar to question 26. Remove duplicate element from sorted array
Isme bas hume nums[rp-1] ki jagah us value se compare karna hai ki
Kya hamara right pointer ki position wali value question ki value jisey remove karna hai usey different hai?
Agar hai toh hum us different value ko left pointer ki jagah par store kardenge 
This will automatically remove question wali value.
'''