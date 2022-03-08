# Problem Statement: https://leetcode.com/problems/reshape-the-matrix/

class Solution:
    def matrixReshape(self,nums, r, c):
        flat_list = []
        matrix = []

        for sublist in nums:
            for item in sublist:
                flat_list.append(item)

        if len(flat_list) != r * c:
            return nums
        else:
            for i in range(0,len(flat_list),c):
                matrix.append(flat_list[i:i+c])
            return matrix