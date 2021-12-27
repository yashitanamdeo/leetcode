# Problem Statement: https://leetcode.com/problems/build-array-from-permutation/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        num = nums
        arr = []
        for i in range(len(num)):
            arr.append(num[num[i]])
        return arr