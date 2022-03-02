# Problem Statement: https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

class Solution:
    def average(self, salary: List[int]) -> float:
        minimum = min(salary)
        maximum = max(salary)
        salary.remove(minimum)
        salary.remove(maximum)
        
        average = sum(salary) / len(salary)
        
        return average