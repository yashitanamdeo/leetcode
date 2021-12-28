# Problem Statement:https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        else:
            lp = 1 #left pointer
            for rp in range(1,len(nums)): #right pointer
                if nums[rp] != nums[rp-1]:
                    nums[lp] = nums[rp]
                    lp += 1
            return lp
'''
Isme hum 2 pointers lenge left and right aur dono ko 1st index par rakhenge
Because unique element ka count chahiye so 1st element will always be unique
Then for loop se right pointer increment hota jayega jabtak ki hume dusri unique value nhi milti
Matlab ki jabtak nums[1] == nums[0] tab tak right pointer will just increase
Jaise hi nums[rp or 2] != nums[rp-1 or 1] matlab ki different / unique value
Tab hum us unique value ko first unique value ke baad wali position par store kardenge 
Matlab ki jaha par hamara left pointer tha
Because left pointer 1st position par hai starting me toh second unique value waha par hi ayegi after 0 position.
And then end me hum left pointer ko isiliye return kar rhe hai kyuki uska count = total unique elements.
'''