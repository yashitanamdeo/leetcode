# Problem Statement: https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

# Alternate Solution
class Solution:
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        c = 0
        while n:
            n &= n - 1
            c += 1
        return c
    
'''
Using bit operation to cancel a 1 in each round

Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111. n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
'''