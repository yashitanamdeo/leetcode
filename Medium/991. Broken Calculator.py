# Problem Statement: https://leetcode.com/problems/broken-calculator/

class Solution:
    def brokenCalc(self, X, Y):
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1
        
    #https://leetcode.com/problems/broken-calculator/discuss/1076046/Python-Greedy-solution-explained