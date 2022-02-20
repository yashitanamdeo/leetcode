# Problem Statement: https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        PairCount = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if 0 <= i < j < len(nums):
                    if nums[i] == nums[j]:
                        if (i*j) % k == 0:
                            PairCount += 1
        return PairCount