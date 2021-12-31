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

""" https://leetcode.com/problems/maximum-subarray/discuss/1595195/C%2B%2BPython-7-Simple-Solutions-w-Explanation-or-Brute-Force-%2B-DP-%2B-Kadane-%2B-Divide-and-Conquer """