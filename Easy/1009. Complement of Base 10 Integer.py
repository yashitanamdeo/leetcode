## Problem Statement: https://leetcode.com/problems/complement-of-base-10-integer/

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            result = 0
            factor = 1
            
            while(n > 0):
                result += factor * (1 if n%2 == 0 else 0)
                factor *= 2
                n //= 2
            return result