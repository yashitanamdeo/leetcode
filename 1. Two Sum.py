# Problem Statement: https://leetcode.com/problems/two-sum/

# General Solution : Complexity - O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return i,j

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, value in enumerate(nums):
            required_num = target - nums[index]
            if required_num in d:
                return [d[required_num],index] 
            else:
                d[value] = index

'''
Hum ek empty dictionary banayenge, 
phir enumerate se index and values ajayegi nums array ki 
then hum check karenge ki target - index or target - nums[index] kya hai 
That is required number. Agar woh already dictionary me hai then we will return it
warna we will put (eg) d[2] = 0 matlab 2:0
Phir jab iske sath ka target hoga then we will return d[2] i.e 0 and index means 
us time ka present index ie. 1
'''