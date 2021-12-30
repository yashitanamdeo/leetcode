# Problem Statement: https://leetcode.com/problems/maximum-subarray/


# Brute Force Solution : Complexity - O(n^2)
class Solution:
    def maxSubArray(self, nums):
        ans = -inf
        for i in range(len(nums)):
            cur_sum = 0
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                ans = max(ans, cur_sum)
        return ans