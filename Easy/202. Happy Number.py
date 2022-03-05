# Problem Statement: https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        while(n > 6 and n!=1):
            squareSum = 0
            num = str(n)
            for i in range(len(num)):
                squareSum += int(num[i])**2
            n = squareSum
            
        if n == 1:
            return True
        return False