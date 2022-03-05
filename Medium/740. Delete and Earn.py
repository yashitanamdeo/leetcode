# Problem Statement: https://leetcode.com/problems/delete-and-earn/

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        # score is the storage to collect all the copies of distinct integers in input array
        score = [0] * (max(nums)+1)
        
        # score[i] save all the copies of corresponding number in input array
        for number in nums:
            score[number]+= number
            
        
        # Reduce to the House Robbery Problem I
        # Leetcode #198: https://leetcode.com/problems/house-robber/
        size = len(score)
        
        if size <= 2:
            return max(score)
        
        max_points = [0 for _ in range(size)]
        max_points[0] = score[0]
        max_points[1] = max(score[0], score[1])
        
        for i in range(2, size):
            
            take_integer_i = max_points[i-2] + score[i]
            not_to_take_integer_i = max_points[i-1] + 0 
            
            max_points[i] = max( take_integer_i, not_to_take_integer_i)
        
        return max_points[-1]

'''
Given nums = [2,2,3,3,3,4]

reduce it to House Robbery problem

score = [0, 0, 2+2, 3+3+3, 4] = [0, 0, 4, 9, 4]

Max points of Delete and Eran with [2,2,3,3,3,4]
= Max value of Leetcode 198: House Robbery with [0, 0, 4, 9, 4]
= 9
'''