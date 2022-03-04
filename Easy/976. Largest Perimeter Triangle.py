# Problem Statement: https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort(reverse = True)
        for i in range(3,len(A)+1):
            if(A[i-3] < A[i-2] + A[i-1]):
                return sum(A[i-3:i])
        return 0

'''
1. Sort the List to get the top 3 lengths
2. Check if the largest length is less than sum of other two
    * If 2 is false, drop the max length take next 3 largest length and repeat 1-2
    * if 2 is true, return sum of all lengths
3. if loop ends, and no possible combination found, return 0
'''