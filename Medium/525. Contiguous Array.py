# Problem Statement: https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {}
        max_len = 0
        suma = 0
        n = len(nums)
        for i in range(n):
            suma += -1 if nums[i] == 0 else 1
            if suma == 0: # max_len would be from start to ith index
                if max_len < i+1:
                    max_len = i + 1
            elif suma in hashmap:  # max_len would be ith index - previous value of that sum from hashmap
                if max_len < i-hashmap[suma]: 
                    max_len = i - hashmap[suma]
            else:
                hashmap[suma] = i # if sum not occured previously, add it in hashmap
        return max_len
            