# Problem Statement: https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i]+[n])
        return result
    
'''
# the set to iterate over/generate the power set for
input_set = [1, 2, 3]

# subset initially only has the empty set (empty list), []
subset = [[]]

# in each iteration, concatenate each element/list in subset with the list [n], then extend the results into subset
# element -> subset list after each iteration

# in the first iteration, subset's only element is []
# [ []  + [1] ] = [ [1] ]
num = 1 -> [[], [1]]  

# in the second iteration, we concatenate [] with [2] and [1] with [2]
# [ [] + [2] ] = [ [2] ], [ [1] + [2] ] = [ [1, 2] ]
num = 2 -> [[], [1], [2], [1, 2]]

# in the third iteration, we concatenate [3] with each element in subset
# [ [] + [3] ] = [ [3] ], [ [1] + [3] ] = [ [1, 3] ], [ [2] + [3] ] = [ [2, 3] ], [ [1, 2] + [3] ] = [ [1, 2, 3] ]
num = 3 -> [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
'''