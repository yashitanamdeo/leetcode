# Problem Statement: https://leetcode.com/problems/burst-balloons/

# Explaination: https://www.youtube.com/watch?v=uG_MtaCJIrM

class Solution:
    def maxCoins(self, nums):
        nums, N = [1] + nums + [1], len(nums) + 2 #array with 1,1 balloons at the end and length as N
        dp = [[0] * N for _ in range(N)] # table full of zeros
        
        for left in range(N - 2, -1, -1):
            for right in range(left + 2, N):
                dp[left][right] = max(nums[left]*nums[i]*nums[right] + dp[left][i] + dp[i][right] for i in range(left + 1, right))
        
        return dp[0][N-1]