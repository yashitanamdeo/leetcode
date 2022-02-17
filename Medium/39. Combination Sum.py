# Problem Statement: https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort to terminate early when target < 0
        
        def backtracking(i, target, path):
            if target == 0:
                ans.append(path)
                return
            if i == len(candidates) or target < candidates[i]:
                return
            backtracking(i, target - candidates[i], path + [candidates[i]]) # Choose ith candidate
            backtracking(i + 1, target, path) # Skip ith candidate
        
        ans = []
        backtracking(0, target, [])
        return ans