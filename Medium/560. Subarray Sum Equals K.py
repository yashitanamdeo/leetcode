# Problem Statement: https://leetcode.com/problems/subarray-sum-equals-k/

# Solution 1 - Complexity: O(n^2) [Time Limit Exceeded]
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if sum(nums[i:j+1]) == k:
                    count += 1
        return count